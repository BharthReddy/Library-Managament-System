from django.urls import path
from . import views

urlpatterns = [
    # User Module
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('books/', views.books, name='books'),
    path('search/', views.search, name='search'),

    # Admin Module
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-book/', views.add_book, name='add_book'),
    path('members/', views.members, name='members'),
    path('issue-book/', views.issue_book, name='issue_book'),
    path('history/', views.history, name='history'),
]
path('update-book/', views.update_book, name='update_book'),
path('delete-book/', views.delete_book, name='delete_book'),
path('borrow/', views.borrow, name='borrow'),