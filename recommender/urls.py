from django.urls import path
from .views import RecommenderAPIView

urlpatterns = [
    path('', RecommenderAPIView.as_view()),
]
