# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
from django.urls import include, path
from articles import views
urlpatterns = [
    path('lot/<int:num>/', views.lot,name='lot'),
    path('', views.start,name='start'),
]