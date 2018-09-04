from django.conf.urls import url
from .views import ListRecView

urlpatterns = [
    url(r'^list-rec/', ListRecView.as_view()),
]
