from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from contextlib import asynccontextmanager
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table, Boolean
from databases import Database
from sqlalchemy import text

DATABASE_URL = "sqlite:///./test.db"
database = Database(DATABASE_URL)
metadata = MetaData()

# Определение схемы таблицы
todos = Table(
    "todos",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(50)),
    Column("description", String(200)),
    Column("completed", Boolean)
)

engine = create_engine(DATABASE_URL)
metadata.create_all(engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()


class To_do(BaseModel):
    id: int
    name: str
    done: bool


app = FastAPI(lifespan=lifespan)

ggvp = {}


@app.get("/")
async def root():
    return {"УБЕЙТЕ": "МЕНЯ"}


@app.post("/add")
async def add(to_do: To_do):
    if to_do.id in ggvp:
        raise HTTPException(status_code=400, detail="Todo with this ID already exists")
    else:
        ggvp[to_do.id] = to_do


@app.get("/items")
async def items():
    return ggvp
