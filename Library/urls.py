from django.urls import path
from .views import BookList, MemberList, BorrowList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('members/', MemberList.as_view(), name='member-list'),
    path('borrows/', BorrowList.as_view(), name='borrow-list'),
]
