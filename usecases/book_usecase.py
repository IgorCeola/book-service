from domain.book import Book

class BookUseCase:
    def __init__(self, repository):
        self.repository = repository

    def listar_livros(self):
        return self.repository.listar()

    def buscar_livro(self, id: int):
        return self.repository.buscar_por_id(id)

    def adicionar_livro(self, dados: dict):
        novo = Book(**dados)
        return self.repository.adicionar(novo)

    def atualizar_livro(self, id: int, dados: dict):
        return self.repository.atualizar(id, dados)

    def remover_livro(self, id: int):
        return self.repository.remover(id)
