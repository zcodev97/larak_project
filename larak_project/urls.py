from django.contrib import admin
from django.urls import path
from larak_app.apiviews import (ProductsList, CategoriesList, SingleCategory,
                                UserInfoFromToken,
                                AddProductAPI, ClientProductsListAPI,
                                ClientOrdersListAPI,AddOrderAPI,
                                EmployeeOrderListAPI,
                                UpdateOrderAPI,)

from core.apiviews import (GetUserInfoAPI,AddUserInfoAPI)
from django.conf import settings
from django.conf.urls.static import static
from core.serializers import CustomUserSerializer
from core.apiviews import (UsersListAPI, BikersListAPI,
                           AddUserAPI,UsersUnderManagerAPI,
                           AddEmployeeAPI,UpdatePasswordAPI)
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


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
    # api docs

    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    # products api
    path('products/', ProductsList.as_view(), name="all Products"),

    path('add_product/', AddProductAPI.as_view(), name="add product"),
    # categories api
    path('categories/', CategoriesList.as_view(), name="all Categories"),
    path('add_category/', CategoriesList.as_view(), name="add category"),

    path('client_orders/', ClientOrdersListAPI.as_view(), name="client orders list"),
    path('client_submit_order/', AddOrderAPI.as_view(), name="client submit new order"),
    path('client_products/', ClientProductsListAPI.as_view(), name="all Products"),
    path('add_user_info/', AddUserInfoAPI.as_view(), name="add user info API"),
    # path('get_user_info/', GetUserInfoAPI.as_view(), name="get user info API"),

    path('admin_update_order/<uuid:pk>', UpdateOrderAPI.as_view(), name="admin update order"),
    path('get_user_info/<uuid:pk>', GetUserInfoAPI.as_view(), name="admin update order"),

    path('employee_orders/<str:client>', EmployeeOrderListAPI.as_view(), name="employee order list api"),

    path('users/', UsersListAPI.as_view(), name='users list'),
    path('bikers/', BikersListAPI.as_view(), name='bikers list'),
    path('users_under_managers/', UsersUnderManagerAPI.as_view(), name='employees list'),
    path('update_password/', UpdatePasswordAPI.as_view(), name='update_password'),

    path('user-info/', UserInfoFromToken.as_view(), name='user_info_from_token'),

    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('add_user/', AddUserAPI.as_view(), name='add user'),
    path('add_employee/', AddEmployeeAPI.as_view(), name='add user'),


    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # path('users/', UsersList.as_view(), name="Users List"),
    # path('users/<int:pk>', UserDetails.as_view(), name="Users List"),
    # path('product/<uuid:pk>', ProductsList.as_view(), name="Single Product Products"),
    # path('api-auth/', include('rest_framework.urls'))

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
