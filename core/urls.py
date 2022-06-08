from django.urls import include,path

urlpatterns =[
    path('register',include('core.urls')),
]