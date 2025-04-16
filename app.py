
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import sqlite3
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/", StaticFiles(directory="frontend", html=True), name="static")

DB_PATH = "backend/db.sqlite"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            telegram_id INTEGER PRIMARY KEY,
            username TEXT,
            coins INTEGER DEFAULT 0,
            infected_by INTEGER
        )
    ''')
    conn.commit()
    conn.close()

init_db()

class InitRequest(BaseModel):
    telegram_id: int
    username: str
    ref: int | None = None

@app.post("/init")
def init_user(data: InitRequest):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE telegram_id = ?", (data.telegram_id,))
    user = c.fetchone()

    if not user:
        if data.ref and data.ref != data.telegram_id:
            c.execute("UPDATE users SET coins = coins + 1000 WHERE telegram_id = ?", (data.ref,))
        c.execute("INSERT INTO users (telegram_id, username, coins, infected_by) VALUES (?, ?, ?, ?)",
                  (data.telegram_id, data.username, 0, data.ref))
        conn.commit()

    c.execute("SELECT telegram_id, username, coins FROM users WHERE telegram_id = ?", (data.telegram_id,))
    user = c.fetchone()
    conn.close()
    return {"user": {"telegram_id": user[0], "username": user[1], "coins": user[2]}}

class ClickRequest(BaseModel):
    telegram_id: int

@app.post("/click")
def click(data: ClickRequest):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("UPDATE users SET coins = coins + 1 WHERE telegram_id = ?", (data.telegram_id,))
    conn.commit()
    c.execute("SELECT coins FROM users WHERE telegram_id = ?", (data.telegram_id,))
    coins = c.fetchone()[0]
    conn.close()
    return {"coins": coins}
