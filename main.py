from fastapi import FastAPI
from routes import meshroom

app = FastAPI()
app.include_router(meshroom.meshroom_router)