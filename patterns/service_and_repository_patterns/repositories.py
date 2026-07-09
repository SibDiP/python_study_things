from abc import ABC, abstractmethod
from schemas import Note, NoteIn, NoteUpdate

class AbstractNoteRepository(ABC):
    @abstractmethod
    def create_note(self, note_in: NoteIn) -> Note:
        pass

    @abstractmethod
    def get_all_notes(self) -> list[Note]:
        pass

    @abstractmethod
    def get_note_by_id(self, note_id: int) -> Note | None:
        pass
    
    @abstractmethod
    def update_note(self, note_id: int, note_update: NoteUpdate) -> Note | None:
        pass

    @abstractmethod
    def del_note(self, note_id: int) -> None:
        pass
