from django.contrib import admin
from django.urls import path
from larak_app.apiviews import (ProductsList, CategoriesList, SingleCategory,
                                UserInfoFromToken,
                                AddProductAPI, ClientProductsListAPI,
                                ClientOrdersListAPI,AddOrderAPI,UpdateOrderAPI)
from django.conf import settings
from django.conf.urls.static import static
from core.serializers import CustomUserSerializer
from core.apiviews import UsersListAPI, BikersListAPI, AddUserAPI
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf.urls import include

admin.site.site_header = "Larak Admin"
admin.site.site_title = "Larak Admin Portal"
admin.site.index_title = "Welcome to Larak Portal"


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
    # products api
    path('products/', ProductsList.as_view(), name="all Products"),
    path('client_products/', ClientProductsListAPI.as_view(), name="all Products"),
    path('add_product/', AddProductAPI.as_view(), name="add product"),
    # categories api
    path('categories/', CategoriesList.as_view(), name="all Categories"),
    path('add_category/', CategoriesList.as_view(), name="add category"),

    path('client_orders/', ClientOrdersListAPI.as_view(), name="client orders list"),
    path('client_submit_order/', AddOrderAPI.as_view(), name="client submit new order"),
    path('admin_update_order/<uuid:pk>', UpdateOrderAPI.as_view(), name="admin update order"),

    path('users/', UsersListAPI.as_view(), name='users list'),
    path('bikers/', BikersListAPI.as_view(), name='bikers list'),
    path('add_user/', AddUserAPI.as_view(), name='add user'),

    path('user-info/', UserInfoFromToken.as_view(), name='user_info_from_token'),

    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # path('users/', UsersList.as_view(), name="Users List"),
    # path('users/<int:pk>', UserDetails.as_view(), name="Users List"),
    # path('product/<uuid:pk>', ProductsList.as_view(), name="Single Product Products"),
    # path('api-auth/', include('rest_framework.urls'))

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
