from fastapi import FastAPI
from controllers.book_controller import router
# import threading 
# from consumer.book_validation_consumer import start_consumer

app = FastAPI(title="Book Service")

app.include_router(router)

@app.get("/")
def root():
    return {"mensagem": "Book Service ativo, Capitão!"}


# def start_background():
#     thread = threading.Thread(target=start_consumer)
#     thread.daemon = True
#     thread.start()

# start_background()