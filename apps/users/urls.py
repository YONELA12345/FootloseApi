from django import views
from django.urls import path, re_path

from apps.users.views import auth_login_viewset, auth_register_staff_viewset, party_role_viewset


urlpatterns  = [
    path('login/',auth_login_viewset.as_view()),
    path('staff/register/',auth_register_staff_viewset.as_view()),
    path('staff/role/', party_role_viewset.as_view()),


]
