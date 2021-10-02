from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/admin/'))
]
