from fastapi import FastAPI, HTTPException
from pydantic import BaseModel # <--- 新增這一行
from app.redis_utils import set_key, get_key, delete_key

app = FastAPI()

class SetValueRequest(BaseModel): # <--- 新增這個 class
    value: str

@app.post("/set")
def set_value(key: str, request_body: SetValueRequest):
  set_key(key, request_body.value)
  return {"message": f"Key '{key}' set successfully"}

@app.get("/get")
def get_value(key: str):
    value = get_key(key)
    if value is None:
        raise HTTPException(status_code=404, detail="Key not found")
    return {"key": key, "value": value}

@app.post("/delete")
def delete_value(key: str ):
    delete_key(key)
    return {"status": "deleted","key": key}