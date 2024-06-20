#What is Django URLs?make program to create django urls
'''
->  in Django, URLs are a way to map specific web addresses (URLs)
    to views in your application.
->  Views are the components of your application that handle the logic for
    rendering web pages, processing forms, and handling other user interactions


    *******Example*******
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.home, name='home'),
        path('about/', views.about, name='about'),
    ]

'''
