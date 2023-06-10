from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.Login, name='login'),
    path('logout', views.Logout, name='logout'),

    path('reset_password/',
         views.CustomPasswordResetView.as_view(template_name='password_reset.html'),
         name='password_reset'),
    # men7et as_view() la2enno class base views

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name='password_reset_sent.html'),
         name='password_reset_done'),
    # hayde lseccus messege iza zebit 2aw la2

    path('reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_form.html'),
         name='password_reset_confirm'),
    # heda link li ra7 yousalo 3al email taba3o , uibd64 ma3neto user id incoded
    # token sheck if that the pass is valid

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'),
         name='password_reset_complete'),
    # heda bi5aberna enno kel shi sa7 w sar fina na3mil login
]
