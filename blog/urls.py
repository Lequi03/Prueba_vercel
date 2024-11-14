from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('detail/<int:article_id>', views.detail, name='detail'),  # Ruta para la vista de detalles con un parámetro dinámico 'article_id'
    path('edit/<int:article_id>/', views.edit, name='edit'),  # Agregado el '/' al final
    path('delete/<int:article_id>', views.delete, name='delete'),  # --- Apéndice
]