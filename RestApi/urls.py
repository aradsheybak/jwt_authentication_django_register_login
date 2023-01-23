from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import Register, Login

app_name = 'restApi'
urlpatterns = [
    path('user/register', Register.as_view(), name="register"),
    path('user/login', Login.as_view(), name="login"),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
