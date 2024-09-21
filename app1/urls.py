
from django.contrib import admin
from django.urls import path
from .views import test, mail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', test, name='test '),
    path('mail/', mail, name='mail '),
]
