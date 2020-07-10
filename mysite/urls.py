from django.urls import path

from mysite.views import (
                    home,
                    registration_view,
                    logout_view,
                    login_view
                )



urlpatterns = [

    path('register/',registration_view, name="register" ),
    path('logout/',logout_view, name="logout" ),
    path('login/',login_view, name="login" ),
    path("home", home,name="home"),
]
