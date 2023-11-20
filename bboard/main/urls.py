from django.urls import path
from .views import index, CreateApplicationView, ApplicationListView, DeleteApplicationView, UserProfile
from .views import BBLoginView
from .views import RegisterDoneView, RegisterUserView
from .views import user_activate
from .views import profile
from .views import BBLogoutView
from . import views

app_name = 'main'


urlpatterns = [
   path('', index, name='index'),
   path('accounts/login', BBLoginView.as_view(), name='login'),
   path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
   path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
   path('accounts/register/', RegisterUserView.as_view(), name='register'),
   path('accounts/register/activate/<str:sign>/', user_activate, name='register_activate'),
   path('accounts/profile/', profile, name='profile'),
   path('accounts/create/', CreateApplicationView.as_view(), name='create_application'),
   path('applications/', ApplicationListView.as_view(), name='application_list'),
   path('applications/delete/<int:pk>/', DeleteApplicationView.as_view(), name='application_delete'),
   path('applications/status_app', views.UserProfile, name='profile'),
]