from django.contrib import admin
from django.urls import path
from larak_app.apiviews import SingleProduct, ProductsList, CategoriesList, SingleCategory
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('users/', UsersList.as_view(), name="Users List"),
    # path('users/<int:pk>', UserDetails.as_view(), name="Users List"),
    path('products/', ProductsList.as_view(), name="All Products"),
    path('product/<uuid:pk>', ProductsList.as_view(), name="All Products"),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
