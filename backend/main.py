from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import models, database, crud, schemas

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or set specific domain like ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create the database tables
database.create_tables()

@app.post("/tasks")
def create_task(task: schemas.TaskCreate):
    db = database.SessionLocal()
    try:
        return crud.create_task(db, task.title)
    finally:
        db.close()

@app.get("/tasks")
def read_tasks():
    db = database.SessionLocal()
    try:
        tasks = crud.get_tasks(db)
        return [{"id": t.id, "title": t.title} for t in tasks]
    finally:
        db.close()
