from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Livro, Categoria
# Create your views here.

def index(request):
    return render(request, 'home/index.html', {'livros': get_list_or_404(Livro)})

def sobre(request):
    return render(request, 'home/sobre.html')

def categoria(request):
	return render(request, 'home/categorias.html', {'categorias': get_list_or_404(Categoria)})

def show_book(request, livro_id):
	return render(request, 'home/show_book.html', {'livro': get_object_or_404(Livro,pk=livro_id)})
