from django.urls import path
from .views import all_posts, book_create_add, book_detail

urlpatterns = [
    path('', all_posts, name='home'),
    path('create/', book_create_add, name="create"),
    path('create/<int:book_id>', book_create_add, name="update"),
    path('detail/<int:book_id>', book_detail, name="detail")

]
