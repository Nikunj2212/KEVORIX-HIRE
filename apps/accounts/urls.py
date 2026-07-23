from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [

    path("register/",views.register,name="register"),
    path("login/",views.login_view,name="login"),
    path("verify-otp/", views.verify_otp, name="verify_otp"),
    path("resend-otp/", views.resend_otp, name="resend_otp"),
    path("forgot-password/", views.forgot_password, name="forgot_password"),

    path("forgot-password/verify-otp/", views.forgot_password_verify_otp, name="forgot_password_verify_otp"),

    path("reset-password/", views.reset_password, name="reset_password"),
    path("logout/", views.logout_view, name="logout"),
    path("access-denied/", views.access_denied, name="access_denied"),
        

]