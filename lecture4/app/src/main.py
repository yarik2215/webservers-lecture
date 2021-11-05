from fastapi import FastAPI
import socket

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/test/{id}")
async def test(id: int):
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return {"message": f"Test example {id}", "ip": local_ip}