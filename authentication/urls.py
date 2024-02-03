from django.urls import path
from django.contrib.auth.views import LoginView

import authentication.views
from authentication.views import logout_view

from . views import SignupView


urlpatterns = [
    path('', LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True
    ), name='login'),

    path('logout/', logout_view, name='logout'),
    path('signup', SignupView.as_view(), name='signup')
]
