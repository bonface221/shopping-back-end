from rest_framework_simplejwt.views import token_refresh

from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api-auth/',include('rest_framework.urls')),
    path('',include('shopping.urls')),

    # path('auth/login/', token_obtain_pair),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/signup/', include('dj_rest_auth.registration.urls')),
    path('auth/refresh-token/',token_refresh),

]
