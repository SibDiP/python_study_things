from fastapi import FastAPI, HTTPException, status, Depends

from schemas import Note, NoteIn, NoteUpdate
from services import NotesService, NoteNotFoundError
from dependencies import get_notes_service

app = FastAPI()

@app.post('/notes', response_model=NoteIn, status_code=status.HTTP_201_CREATED)
def create_note(
    note_in: NoteIn, 
    notes_service: NotesService = Depends(get_notes_service)
    ) -> Note:
    return notes_service.create_note(note_in)

@app.get("/notes", response_model=list[Note])
def get_all_notes(
    notes_service: NotesService = Depends(get_notes_service)
    ) -> list[Note]:
    return notes_service.get_all_notes()
    
@app.get("/notes/{note_id}", response_model=Note)
def get_note(
    note_id: int,
    notes_service: NotesService = Depends(get_notes_service)
    ) -> Note | None:
    try:
        return notes_service.get_note_by_id(note_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")

@app.put("/notes/{note_id}", response_model=Note)
def update_note(
    note_id: int, 
    note_update: NoteUpdate,
    notes_service: NotesService = Depends(get_notes_service)
    ) -> Note:
    try:
        return notes_service.update_note(note_id, note_update)
    except NoteNotFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")

@app.delete("/notes/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(
    note_id: int,
    note_service: NotesService = Depends(get_notes_service)
    ):
    try:
        note_service.del_note(note_id)
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    return None
