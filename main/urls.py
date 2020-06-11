from django.urls import path
from .views import (
    IndexView,
    Example01,
    Example02
)

app_name = 'main'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('example_01/', Example01.as_view(), name='example_01'),
    path('example_02/', Example02.as_view(), name='example_02')
]
