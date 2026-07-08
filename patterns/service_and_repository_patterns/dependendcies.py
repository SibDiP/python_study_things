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

class InMemoryNoteRepository(AbstractNoteRepository):
    def __init__(self) -> None:
        self._notes : dict[int, Note] = {}
        self._next_id: int = 1
    
    def create_note(self, note = NoteIn) -> Note:
        new_note = Note(
            id=self._next_id, 
            title=note.title, 
            content=note.content
            )
        self._notes[self._next_id] = new_note
        return new_note