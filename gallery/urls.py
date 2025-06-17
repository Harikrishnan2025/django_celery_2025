from django.urls import path
from . import views


urlpatterns = [
    path("",views.gallery,name="gallery"),
    path("upload/",views.upload,name='upload'),
    path("register/",views.register,name="register"),
    path("login/",views.login_view,name="login"),
    path("logout/",views.logout_view,name="logout"),
    path('media-protected/<path:path>/', views.protected_media, name='protected_media')
   
]