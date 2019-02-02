from django.contrib.auth import views as auth_views
from django.urls import path, re_path
from .views import LoginForm

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', auth_views.LoginView.as_view(template_name='main/login_form.html', form_class=LoginForm, redirect_authenticated_user=True), name='login'),
    path('do-logout', auth_views.LogoutView.as_view()),
    path('register', views.Registration_view.as_view(), name='register'),
    path('profile', views.Profile_view.as_view(), name='profile'),
    path('test', views.test),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<stoken>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    path('<str:language_name>', views.get_sections, name='language'),
]