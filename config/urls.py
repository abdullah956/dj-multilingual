from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
]

# Apply i18n_patterns for language support
urlpatterns += i18n_patterns(
    path('', include('multi.urls')),  # Include your app's URLs here
    path('i18n/', include('django.conf.urls.i18n')),  # URL for language switching
)
