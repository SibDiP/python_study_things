# notes_app.py
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

class NoteIn(BaseModel):
    title: str
    content: str

class Note(BaseModel):
    id: int
    title: str
    content: str

# Имитация базы данных
notes_db: dict[int, Note] = {}
next_id = 1

@app.post("/notes", response_model=Note, status_code=status.HTTP_201_CREATED)
def create_note(note: NoteIn):
    global next_id
    new_note = Note(id=next_id, **note.model_dump())
    notes_db[next_id] = new_note
    next_id += 1
    return new_note

@app.get("/notes", response_model=list[Note])
def get_all_notes():
    return list(notes_db.values())

@app.get("/notes/{note_id}", response_model=Note)
def get_note(note_id: int):
    note = notes_db.get(note_id)
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    return note

@app.put("/notes/{note_id}", response_model=Note)
def update_note(note_id: int, note_in: NoteIn):
    if note_id not in notes_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    updated_note = Note(id=note_id, **note_in.model_dump())
    notes_db[note_id] = updated_note
    return updated_note

@app.delete("/notes/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id: int):
    if note_id not in notes_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    del notes_db[note_id]
    return