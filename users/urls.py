from django.urls import path

from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register('', views.UserViewSet)


urlpatterns = [
    path('signup/', views.SignUpUserView.as_view(), name='signup'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('profile/', views.ManageUserView.as_view(), name='profile'),

]
urlpatterns += router.urls
