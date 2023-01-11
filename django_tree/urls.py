import debug_toolbar
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from django_tree import settings
from menu.views import HomeView, BlogView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^__debug__/', include(debug_toolbar.urls)),
    url(r'^blog/', BlogView.as_view(), name='blog'),
    url(r'^', HomeView.as_view(), name='home'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
