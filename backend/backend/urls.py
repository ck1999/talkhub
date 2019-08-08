from django.contrib import admin
from django.urls import path
from admin_module import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/hello', views.hello),
    path('api/submit', views.submit_application),
    path('api/applications', views.getApplications),
]
