from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def books():
    return {"bookname" : "the novels"}