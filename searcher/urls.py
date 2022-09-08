from django.urls import path
from . import views
app_name = "searcher"

urlpatterns = [
    path('', views.searchbox, name='search_box')
]
