from fastapi.testclient import TestClient
from controllers.book_controller import usecase
from unittest.mock import MagicMock

def test_listar_livros(client):
    usecase.listar_livros = MagicMock(return_value=[{"id": "1", "titulo": "A", "autor": "B", "ano": 2020, "preco": 10.0}])

    resp = client.get("/livros")
    assert resp.status_code == 200
    assert len(resp.json()) == 1

def test_buscar_livro_encontrado(client):
    usecase.buscar_livro = MagicMock(return_value={"id": "1", "titulo": "A"})

    resp = client.get("/livros/1")
    assert resp.status_code == 200
    assert resp.json()["id"] == "1"

def test_buscar_livro_nao_encontrado(client):
    usecase.buscar_livro = MagicMock(return_value=None)

    resp = client.get("/livros/123")
    assert resp.status_code == 404

def test_adicionar_livro(client):
    usecase.adicionar_livro = MagicMock(return_value={"id": "1", "titulo": "Test", "autor": "X", "ano": 2023, "preco": 50})

    resp = client.post("/livros", json={"titulo": "Test", "autor": "X", "ano": 2023, "preco": 50})
    assert resp.status_code == 200
    assert resp.json()["id"] == "1"

def test_atualizar_livro(client):
    usecase.atualizar_livro = MagicMock(return_value={"id": "1", "titulo": "Novo"})

    resp = client.put("/livros/1", json={"titulo": "Novo"})
    assert resp.status_code == 200

def test_atualizar_livro_nao_encontrado(client):
    usecase.atualizar_livro = MagicMock(return_value=None)

    resp = client.put("/livros/999", json={"titulo": "Teste"})
    assert resp.status_code == 404

def test_remover_livro(client):
    usecase.remover_livro = MagicMock(return_value=True)

    resp = client.delete("/livros/1")
    assert resp.status_code == 200
    assert resp.json()["mensagem"] == "Livro removido com sucesso"

def test_remover_livro_nao_encontrado(client):
    usecase.remover_livro = MagicMock(return_value=False)

    resp = client.delete("/livros/1")
    assert resp.status_code == 404
