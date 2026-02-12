from django.urls import path
from . import views
from .constants import LIST_CREATE, RETRIEVE_UPDATE_DESTROY

urlpatterns = [
    path('categories/', views.CategoryViewSet.as_view(LIST_CREATE)),
    path('categories/<int:id>/', views.CategoryViewSet.as_view(RETRIEVE_UPDATE_DESTROY)),
    path('', views.ProductViewSet.as_view(LIST_CREATE)),
    path('<int:id>/', views.ProductViewSet.as_view(RETRIEVE_UPDATE_DESTROY)),
    path('reviews/', views.ReviewViewSet.as_view(LIST_CREATE)),
    path('reviews/<int:id>/', views.ReviewViewSet.as_view(RETRIEVE_UPDATE_DESTROY)),
]