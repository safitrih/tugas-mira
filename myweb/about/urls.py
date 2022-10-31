from django.urls import re_path
from .import views


from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('kamarku/', include ('kamarku.urls')),
    path('dapurcantik/', include('dapurcantik.urls')),
]