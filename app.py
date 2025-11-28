from fastapi import FastAPI
from controllers.book_controller import router
from prometheus_fastapi_instrumentator import Instrumentator


app = FastAPI(title="Book Service")

app.include_router(router)

@app.on_event("startup")
def startup_event():
    Instrumentator().instrument(
        app, 
        exclude_paths=["/metrics"], 
    ).expose(app)

@app.get("/")
def root():
    return {"mensagem": "Book Service ativo, Capitão!"}

