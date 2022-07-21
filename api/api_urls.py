from django.urls import path
from api import views

urlpatterns = [
    path('', views.ArticleView.as_view()),
    path('details/<int:id>/', views.ArticleGenericView.as_view()),
]