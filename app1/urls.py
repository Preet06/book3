from django.urls import path
from . import views
from .views import BookCreateView , BookDetailView
from .views import HomePageView


urlpatterns = [
   # path('home', views.home_page, name='home_page'),
    path('add', BookCreateView.as_view(), name='add'),
    path('', HomePageView.as_view(), name='home2'),
    path('post/<int:pk>/', BookDetailView.as_view(),name='post_detail')
]