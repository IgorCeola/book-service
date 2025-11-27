from fastapi import APIRouter, HTTPException
from usecases.book_usecase import BookUseCase
from repository.book_repository import BookRepository

router = APIRouter()
repo = BookRepository()
usecase = BookUseCase(repo)

@router.get("/livros")
def listar_livros():
    return usecase.listar_livros()

@router.get("/livros/{id}")
def buscar_livro(id: str):
    livro = usecase.buscar_livro(id)
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado.")
    return livro

@router.post("/livros")
def adicionar_livro(dados: dict):
    return usecase.adicionar_livro(dados)

@router.put("/livros/{id}")
def atualizar_livro(id: str, dados: dict):
    atualizado = usecase.atualizar_livro(id, dados)
    if not atualizado:
        raise HTTPException(status_code=404, detail="Livro não encontrado.")
    return atualizado

@router.delete("/livros/{id}")
def remover_livro(id: str):
    removido = usecase.remover_livro(id)
    if not removido:
        raise HTTPException(status_code=404, detail="Livro não encontrado.")
    return {"mensagem": "Livro removido com sucesso"}
