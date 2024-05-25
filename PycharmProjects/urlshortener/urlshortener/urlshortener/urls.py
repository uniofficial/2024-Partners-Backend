from django.contrib import admin
from django.urls import path, include
from urlshortenerapp.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # 빈 경로에 대한 URL 패턴 추가
    path('', include('urlshortenerapp.urls')),
]
