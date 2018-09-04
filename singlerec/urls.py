from django.conf.urls import url
from .views import SingleRecView

urlpatterns = [
    url(r'^single-rec', SingleRecView.as_view()),
]