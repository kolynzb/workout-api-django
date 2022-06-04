from django.contrib import admin
from django.urls import path,include

admin.site.site_header = 'Workout Admin'
admin.site.index_title = 'Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/',include('djoser.urls')),
]
