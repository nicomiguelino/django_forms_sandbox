from django.urls import path
from .views import (
    IndexView,
    Example01,
    Example02,
    Example03
)

app_name = 'main'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('example_01/', Example01.as_view(), name='example_01'),
    path('example_02/', Example02.as_view(), name='example_02'),
    path('example_03/', Example03.as_view(), name='example_03')
]
