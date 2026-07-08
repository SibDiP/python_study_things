"""
class NoteIn(BaseModel):
    title: str
    content: str

class Note(BaseModel):
    id: int
    title: str
    content: str
"""

from fastapi import Depends

from schemas import Note, NoteIn
from repositories import AbstractNoteRepository
from services import NotesService

class InMemoryNoteRepository(AbstractNoteRepository):
    def __init__(self) -> None:
        self._notes : dict[int, Note] = {}
        self._next_id: int = 1
    
    def create_note(self, note_in: NoteIn) -> Note:
        new_note = Note(
            id=self._next_id, 
            **note_in.model_dump(),
            )
        self._notes[self._next_id] = new_note
        return new_note
    
    def get_all_notes(self) -> list[Note]:
        return list(self._notes.values())
    
    def get_note_by_id(self, note_id: int) -> Note:
        #TODO. Проверка на наличие
        return self._notes[note_id]
    
    def update_note(self, note_id: int, note_in: NoteIn) -> Note:
        update_note = Note(
            id=note_id,
            **note_in.model_dump(),
            )
        self._notes[update_note.id] = update_note

        return update_note
    
    def del_note(self, note_id: int) -> None:
        self._notes.pop(note_id)
        return None

def get_note_repository() -> AbstractNoteRepository:
    return InMemoryNoteRepository()

def get_notes_service(notes_repo: AbstractNoteRepository = Depends(get_note_repository)):
    return NotesService(notes_repo)
