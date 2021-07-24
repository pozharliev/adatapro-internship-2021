from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LogoutView

from api import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', include('api.signUpView.urls')),
    path('login/', include('api.logInView.urls')),
    path('', include('api.homeView.urls')),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('account/', include('api.accountView.urls', namespace='account')),
    path('info', include('api.informationView.urls'))


]
