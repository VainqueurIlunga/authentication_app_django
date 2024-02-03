from django.urls import path
#from django.contrib.auth.views import LoginView
from blog_app.views import home



# from . views import LoginView

urlpatterns = [
    path('', home, name='home')
]
# urlpatterns = [
#     path('', LoginView.as_view(
#         template_name='blog/index.html',
#         redirect_authenticated_user=True
#     ), name='index'),
#     # path('logout/',)
# ]
