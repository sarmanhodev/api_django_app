from django.urls import path
from . import views

urlpatterns = [
    path('produtos/', views.listar_produtos),
    path('produtos/<int:pk>/', views.detalhes_produto),
    path('produtos/criar/', views.criar_produto),
    path('produtos/<int:pk>/atualizar/', views.atualizar_produto),
    path('produtos/<int:pk>/excluir/', views.excluir_produto),
]
