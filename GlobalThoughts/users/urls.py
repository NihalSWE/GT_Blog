from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [

        path('register/',views.register,name="Register"),
        path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='Login'),
        path('logout/',auth_views.LogoutView.as_view(next_page='Login'),name='Logout'),
        path('profile/',views.profile,name="Profile"),
        path('password-reset/',auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),name='password_reset'),
        path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
        path('password-reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='reset_pass_confirm'),
        path('password-reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='changepassword_complete'),

]
