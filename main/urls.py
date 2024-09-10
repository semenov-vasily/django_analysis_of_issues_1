from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostsList.as_view()),
    path('category/<slug:category_id>', views.CategoryDetails.as_view()),
]