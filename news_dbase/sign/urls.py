from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
# from .views import BaseRegisterView, make_author
from .views import BaseRegisterView, upgrade_me, make_author


urlpatterns = [
    path('login/', LoginView.as_view(template_name='sign/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='sign/logout.html'), name='logout'),
    path('signup/', BaseRegisterView.as_view(template_name='sign/signup.html'), name='signup'),
    path('author/', make_author, name='author'),
    path('upgrade/', upgrade_me, name='upgrade'),

]
