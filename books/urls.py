from django.urls import path
from .views import all_posts,book_create_add

urlpatterns = [
    path('', all_posts, name='home'),
    path('create/', book_create_add, name="create")

]