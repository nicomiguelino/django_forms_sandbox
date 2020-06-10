from django.urls import path
from .views import (
    IndexView,
    Example01
)

app_name = 'main'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('example_01/', Example01.as_view(), name='example_01')
]
