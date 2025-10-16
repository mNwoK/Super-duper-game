from fastapi import FastAPI

app = FastAPI()

things_to_do = []


@app.get("/")
async def root():
    return {"УБЕЙТЕ": "МЕНЯ"}


@app.post("/add/{name}")
async def add(name):
    things_to_do.append(name)


@app.get("/items")
async def items():
    return things_to_do
