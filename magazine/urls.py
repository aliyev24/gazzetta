from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('registration/', views.RegisterUser.as_view(), name='registration'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_me, name='logout'),
    path('post/<slug:slug>/', views.ShowPost.as_view(), name='post'),
    path('category/<slug:slug>/', views.ShowCategory.as_view(), name='category'),
    path('search/', views.search, name='search'),
]