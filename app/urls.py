from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView

admin_str = 'Administración'
admin.site.site_header = admin_str
admin.site.site_title = admin_str

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',
    TemplateView.as_view(template_name='index.html'),
    name='home'
    )
]
