from django.urls import path
from . import views


urlpatterns = [
    # path('books/',views.books),
    path('books/', views.BookList.as_view()),#must include trailing slash for endpoint to function
    path('books/<int:pk>', views.Book.as_view()),
    #"<int:pk>" - path converter that matches an integer in the url and can be used in the view
    # "as_view" - method call that creates an instance of the view class and returns the view function that can handle the HTTP request
]


