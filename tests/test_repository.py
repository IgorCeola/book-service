from repository.book_repository import BookRepository
from domain.book import Book
from unittest.mock import MagicMock
from bson.objectid import ObjectId

VALID_ID = "507f1f77bcf86cd799439011"

def test_listar():
    repo = BookRepository()
    repo_collection = MagicMock()
    repo_collection.find.return_value = [
        {"_id": "123", "titulo": "A", "autor": "B", "ano": 2020, "preco": 10}
    ]

    import repository.book_repository as module
    module.books_collection = repo_collection

    result = repo.listar()
    assert result[0]["id"] == "123"

def test_buscar_por_id():
        repo = BookRepository()
        repo_collection = MagicMock()
        
        repo_collection.find_one.return_value = {
            "_id": ObjectId(VALID_ID),
            "titulo": "A"
        }

        import repository.book_repository as module
        module.books_collection = repo_collection

        result = repo.buscar_por_id(VALID_ID)
        
        assert result["id"] == VALID_ID 

        repo_collection.find_one.assert_called_once_with({"_id": ObjectId(VALID_ID)})

def test_adicionar():
    repo = BookRepository()
    fake_result = MagicMock(inserted_id="123")

    repo_collection = MagicMock()
    repo_collection.insert_one.return_value = fake_result

    import repository.book_repository as module
    module.books_collection = repo_collection

    livro = Book(titulo="A", autor="B", ano=2020, preco=10)
    result = repo.adicionar(livro)
    assert result.id == "123"
