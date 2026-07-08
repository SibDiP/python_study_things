from schemas import Note, NoteIn
from repositories import AbstractNoteRepository

class NotesService:
    def __init__(self, notes_repo: AbstractNoteRepository) -> None:
        self.notes_repo = notes_repo

    def create_note(self, note_in: NoteIn) -> Note:
        return self.notes_repo.create_note(note_in)
    
    def get_all_notes(self) -> list[Note]:
        return self.notes_repo.get_all_notes()
    
    def get_note_by_id(self, note_id: int) -> Note:
        return self.notes_repo.get_note_by_id(note_id)
    
    def update_note(self, note_id: int, note_in: NoteIn) -> Note:
        return self.notes_repo.update_note(note_id, note_in)
    
    def del_note(self, note_id: int) -> None:
        return self.notes_repo.del_note(note_id)
    
    