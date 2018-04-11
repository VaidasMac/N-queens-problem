from django.urls import path
from . import views
app_name = 'queens'
urlpatterns=[

    path('index/', views.Index.as_view(), name='index'),

    path('', views.testing, name='testing'),
]