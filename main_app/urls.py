from django.urls import path

from . import views

urlpatterns = [
    path('', views.landing, name = 'landing'),
    path('beers/', views.feed, name = 'feed'),
    path('beer/add/', views.BeerCreate.as_view(), name = 'beer_add' ),
    path('blog/', views.blog, name = 'blog'),
    path('accounts/signup/', views.signup, name = 'signup'),
    path('beers/<int:pk>/update/', views.BeerUpdate.as_view(), name = 'beers_update'),
    path('beers/<int:pk>/delete/', views.BeerDelete.as_view(), name = 'beers_delete'),
    path('beers/<int:beer_id>/', views.beers_detail, name = 'detail'),
    path('beers/<int:beer_id>/add_photo', views.add_photo, name = 'add_photo')
]