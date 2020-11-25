from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('categorias/', views.categoria, name='categorias'),
    path('livro/<int:livro_id>/', views.show_book, name='show_book'),
]