from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Produto
from .serializers import ProdutoSerializer

@api_view(['GET'])
def listar_produtos(request):
    produtos = Produto.objects.all()
    serializer = ProdutoSerializer(produtos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detalhes_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    serializer = ProdutoSerializer(produto)
    return Response(serializer.data)

@api_view(['POST'])
def criar_produto(request):
    serializer = ProdutoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def atualizar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    serializer = ProdutoSerializer(produto, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def excluir_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    produto.delete()
    return Response(status=204)
