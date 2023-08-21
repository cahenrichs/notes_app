from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('signup/', views.signup, name='signup'),
   path('signin/', views.signin, name='signin'),
   path('logout_user', views.logout_user, name='logout_user'),
   path('overview', views.overview, name='overview'),
   path('notes', views.notes, name='notes'),
]
