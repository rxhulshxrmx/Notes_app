# Simple Notes App

A minimalistic notes application built with FastAPI and vanilla JavaScript.

## Features

- Create, read, update, and delete notes
- Clean and minimalistic UI
- No external dependencies (except for the backend)
- Responsive design

## Tech Stack

- Backend: FastAPI (Python)
- Frontend: Vanilla JavaScript, HTML, CSS
- Database: In-memory storage (for demo purposes)

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/rxhulshxrmx/Notes_app.git
cd notes-app
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the backend server:
```bash
uvicorn main:app --reload
```

5. Open `index.html` in your browser or serve it using a local server.

## Project Structure

```
notes-app/
├── main.py           # FastAPI backend
├── index.html        # Frontend
├── requirements.txt  # Python dependencies
└── README.md        # This file
```

## API Endpoints

- `GET /notes` - Get all notes
- `POST /notes` - Create a new note
- `GET /notes/{note_id}` - Get a specific note
- `PUT /notes/{note_id}` - Update a note
- `DELETE /notes/{note_id}` - Delete a note

## Development

This project was built as a learning exercise to understand:
- FastAPI basics

## License

MIT License 
