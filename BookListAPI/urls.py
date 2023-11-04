from django.urls import path
from . import views

from rest_framework.routers import SimpleRouter, DefaultRouter


router = SimpleRouter(trailing_slash=False)
router.register('books', views.BookView, basename='books')
urlpatterns = router.urls




urlpatterns = [
    path('books/',views.books),
    path('orders/', views.Orders.listOrders),
    # path('books/<int:pk>', views.BookView.as_view()),
    path('books', views.BookView.as_view(
        {
            'get':'list',
            'post':'create',
        })
    ),
    path('books/<int:pk>', views.BookView.as_view(
        {
            'get':'retrieve',
            'put':'update',
            'patch':'"partial_update',
            'delete':'destroy',
        }
    ))
]


