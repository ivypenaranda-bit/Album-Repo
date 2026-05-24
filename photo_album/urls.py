from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('', include('albums.urls')),
]

if not settings.DEBUG and hasattr(settings, 'MEDIA_URL'):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
