from django.conf.urls import url
import authentication

urlpatterns = [
    url(r'^login', authentication.hk_login, name='login'),
    url(r'^logout', authentication.hk_logout, name='logout'),
    url(r'^register', authentication.hk_register, name='register')
]
