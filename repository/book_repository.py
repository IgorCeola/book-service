from bson import ObjectId
from domain.book import Book
from database import books_collection

class BookRepository:
    
    VALID_ID = "507f1f77bcf86cd799439011"
    
    def listar(self):
        livros = list(books_collection.find())
        for livro in livros:
            livro["id"] = str(livro["_id"])
            del livro["_id"]
        return livros

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

    def adicionar(self, livro: Book):
        data = livro.dict(exclude_unset=True)
        result = books_collection.insert_one(data)
        livro.id = str(result.inserted_id)
        return livro

    def atualizar(self, id: str, dados: dict):
        try:
            obj_id = ObjectId(id)
        except:
            return None
        result = books_collection.update_one({"_id": obj_id}, {"$set": dados})
        if result.modified_count == 0:
            return None
        return self.buscar_por_id(id)

    def remover(self, id: str):
        try:
            obj_id = ObjectId(id)
        except:
            return None
        result = books_collection.delete_one({"_id": obj_id})
        return result.deleted_count > 0
