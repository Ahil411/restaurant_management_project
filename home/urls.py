from django.urls import path
from .views import *

urlpatterns = [
    path('menu-categoires/',MenucategoryListView.as_view(), name='menu-category-list'), 
]