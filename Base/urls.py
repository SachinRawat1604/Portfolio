from django.urls import path
from Portfolio import settings
from .import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact_view, name='contact'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)