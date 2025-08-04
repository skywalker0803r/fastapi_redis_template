from fastapi import FastAPI, HTTPException
from app.redis_utils import set_key, get_key

app = FastAPI()

@app.post("/set")
def set_value(key: str, value: str):
    set_key(key, value)
    return {"message": f"Key '{key}' set successfully"}

@app.get("/get")
def get_value(key: str):
    value = get_key(key)
    if value is None:
        raise HTTPException(status_code=404, detail="Key not found")
    return {"key": key, "value": value}
