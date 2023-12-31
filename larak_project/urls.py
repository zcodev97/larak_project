from django.contrib import admin
from django.urls import path
from larak_app.apiviews import SingleProduct, ProductsList, CategoriesList, SingleCategory, UserInfoFromToken
from django.conf import settings
from django.conf.urls.static import static
from core.serializers import CustomUserSerializer
from core.apiviews import RecentRegisteredClients
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
   def validate(self, attrs):
      data = super().validate(attrs)
      # Assuming you have a serializer for your user model
      user_serializer = CustomUserSerializer(self.user).data
      data.update({'user': user_serializer})
      return data


class CustomTokenObtainPairView(TokenObtainPairView):
   serializer_class = CustomTokenObtainPairSerializer


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('users/', UsersList.as_view(), name="Users List"),
    # path('users/<int:pk>', UserDetails.as_view(), name="Users List"),
    path('products/', ProductsList.as_view(), name="All Products"),
    path('categories/', CategoriesList.as_view(), name="All Categories"),
    path('product/<uuid:pk>', ProductsList.as_view(), name="All Products"),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user-info/', UserInfoFromToken.as_view(), name='user_info_from_token'),
    path('new_clients/', RecentRegisteredClients.as_view(), name='new clients list'),

    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
