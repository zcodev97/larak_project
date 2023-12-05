from django.contrib import admin
from django.urls import path
# from larak_app.apiviews import Records, UsersList, UserDetails, LoginView

from rest_framework_simplejwt.views import (
   TokenObtainPairView,
   TokenRefreshView,
)


urlpatterns = [
   path('admin/', admin.site.urls),
   # path('users/', UsersList.as_view(), name="Users List"),
   # path('users/<int:pk>', UserDetails.as_view(), name="Users List"),
   # path('records/', Records.as_view(), name="All Records"),
   path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

