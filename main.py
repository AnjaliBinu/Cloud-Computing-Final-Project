from fastapi import FastAPI
app = FastAPI()
@app.get("/get-message")
async def read_root():
  return {"Message" : "Congratulations on your first API"}
