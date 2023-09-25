from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('books/', views.books, name='books'),
    path('book/<int:book_id>', views.book, name='book'),
    path('book/prestamo-<int:book_id>', views.loan_book, name="loan"),
    path('register_user', views.create_user, name = 'register_user'),
    path('ver_prestamos', views.ver_prestamos, name = 'ver_prestamos'),
    path('ver_prestamos/<int:id_loan>', views.return_book, name = 'devolver'),
    path('create_book', views.register_book, name="create_book")
]
