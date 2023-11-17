from django.urls import path
from .views import index
from .views import BBLoginView

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('accounts/login', BBLoginView.as_view(), name='login'),
]
