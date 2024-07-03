
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('fetch-data/',views.fetch_data,name="fetch-data"),
    path('edit-book/<int:pk>/', views.edit_book, name='edit-book'),
    path('delete-book/<int:book_id>/', views.delete_book, name='delete-book'),
]