from fastapi import FastAPI
from routes import router

app = FastAPI(title="DevSecOps Practice App")
app.include_router(router)
