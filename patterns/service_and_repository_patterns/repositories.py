# Имитация базы данных
# notes_db: dict[int, Note] = {}
# next_id = 1

from abc import ABC, abstractmethod
from schemas import Note, NoteIn

class AbstractNoteRepository(ABC):
    @abstractmethod
    def create_note(self, note_in: NoteIn) -> Note:
        pass

    @abstractmethod
    def get_all_notes(self) -> list[Note]:
        pass

    @abstractmethod
    def get_note_by_id(self, note_id: int) -> Note:
        pass
    
    @abstractmethod
    def update_note(self, note_id: int, note_in: NoteIn) -> Note:
        pass

    @abstractmethod
    def del_note(self, note_id: int) -> None:
        pass
