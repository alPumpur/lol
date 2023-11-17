from django.urls import path
from .views import index
from .views import BBLoginView
from .views import profile
from .views import BBLogoutView

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('accounts/login', BBLoginView.as_view(), name='login'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
]
