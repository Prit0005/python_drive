
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('delete/<int:user_id>',views.delete,name="delete"),
    path('update/<int:user_id>',views.update,name="update"),
]