from django.contrib import admin
from django.urls import path, include
admin.site.site_header="LeSp-Store"
admin.site.site_title ="Admin LeSp-Store"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls'))
]
