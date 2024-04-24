from django.test import TestCase, Client
from django.urls import reverse
from .models import Produto

class ProdutoViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.produtos_url = reverse('listar_produtos')
        # Supondo que tenha definido uma função 'criar_produto' que cria um novo produto para testar a atualização e exclusão
        self.criar_produto_url = reverse('criar_produto')
        self.produto = Produto.objects.create(nome='Produto Teste', descricao='Descrição do Produto Teste', preco=10.0)

    def test_listar_produtos(self):
        response = self.client.get(self.produtos_url)
        self.assertEqual(response.status_code, 200)

    def test_detalhes_produto(self):
        response = self.client.get(reverse('detalhes_produto', args=[self.produto.pk]))
        self.assertEqual(response.status_code, 200)

    def test_criar_produto(self):
        response = self.client.post(self.criar_produto_url, {'nome': 'Novo Produto', 'descricao': 'Descrição do Novo Produto', 'preco': 20.0})
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Produto.objects.filter(nome='Novo Produto').exists())

    def test_atualizar_produto(self):
        atualizar_produto_url = reverse('atualizar_produto', args=[self.produto.pk])
        response = self.client.put(atualizar_produto_url, {'nome': 'Produto Atualizado', 'descricao': 'Descrição Atualizada', 'preco': 15.0})
        self.assertEqual(response.status_code, 200)
        self.produto.refresh_from_db()
        self.assertEqual(self.produto.nome, 'Produto Atualizado')

    def test_excluir_produto(self):
        excluir_produto_url = reverse('excluir_produto', args=[self.produto.pk])
        response = self.client.delete(excluir_produto_url)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Produto.objects.filter(pk=self.produto.pk).exists())
