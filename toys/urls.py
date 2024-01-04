from django.urls import path
from .views import ToyList, ToyDetail


urlpatterns = [
    path("", ToyList.as_view()),
    path("<int:pk>/", ToyDetail.as_view()),
]
