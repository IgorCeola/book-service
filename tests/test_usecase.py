from usecases.book_usecase import BookUseCase
from domain.book import Book
from unittest.mock import MagicMock

def test_listar_livros():
    repo = MagicMock()
    repo.listar.return_value = [{"id": "1"}]

    usecase = BookUseCase(repo)
    result = usecase.listar_livros()
    assert result == [{"id": "1"}]

def test_buscar_livro():
    repo = MagicMock()
    repo.buscar_por_id.return_value = {"id": "1"}

    usecase = BookUseCase(repo)
    result = usecase.buscar_livro("1")
    assert result["id"] == "1"

def test_adicionar_livro():
    repo = MagicMock()
    repo.adicionar.return_value = Book(id="1", titulo="A", autor="B", ano=2020, preco=10)

    usecase = BookUseCase(repo)
    result = usecase.adicionar_livro({"titulo": "A", "autor": "B", "ano": 2020, "preco": 10})
    assert result.id == "1"

def test_atualizar_livro():
    repo = MagicMock()
    repo.atualizar.return_value = {"id": "1", "titulo": "Novo"}

    usecase = BookUseCase(repo)
    result = usecase.atualizar_livro("1", {"titulo": "Novo"})
    assert result["titulo"] == "Novo"

def test_remover_livro():
    repo = MagicMock()
    repo.remover.return_value = True

    usecase = BookUseCase(repo)
    assert usecase.remover_livro("1") == True
