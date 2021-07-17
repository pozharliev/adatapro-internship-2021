from django.urls import path, include
from django.contrib import admin
from .signUpView import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', include('api.signUpView.urls')),
    path('login/', include('api.logInView.urls')),
    path('', include('api.homeView.urls'))
]
