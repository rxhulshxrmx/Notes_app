from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from uuid import uuid4
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for dev only! later restrict it
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Pydantic model for a Note
class Note(BaseModel):
    title: str
    content: str

# ✅ Each stored note will have an ID
class NoteWithID(Note):
    id: str

# 🧠 In-memory "database"
notes_db: List[NoteWithID] = []

# 📝 Create a note
@app.post("/notes", response_model=NoteWithID)
def create_note(note: Note):
    new_note = NoteWithID(id=str(uuid4()), **note.dict())
    notes_db.append(new_note)
    return new_note

# 📋 Get all notes
@app.get("/notes", response_model=List[NoteWithID])
def get_notes():
    return notes_db

# 🔍 Get a single note by ID
@app.get("/notes/{note_id}", response_model=NoteWithID)
def get_note(note_id: str):
    for note in notes_db:
        if note.id == note_id:
            return note
    raise HTTPException(status_code=404, detail="Note not found")

# ❌ Delete a note
@app.delete("/notes/{note_id}")
def delete_note(note_id: str):
    for i, note in enumerate(notes_db):
        if note.id == note_id:
            del notes_db[i]
            return {"message": "Note deleted"}
    raise HTTPException(status_code=404, detail="Note not found")

# ✏️ Edit a note
@app.put("/notes/{note_id}", response_model=NoteWithID)
def edit_note(note_id: str, updated_note: Note):
    for i, note in enumerate(notes_db):
        if note.id == note_id:
            notes_db[i] = NoteWithID(id=note_id, **updated_note.dict())
            return notes_db[i]
    raise HTTPException(status_code=404, detail="Note not found")