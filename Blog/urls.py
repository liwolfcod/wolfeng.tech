from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from base import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls'))
]
urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language=False),
    path("set_language/<str:language>", views.set_language, name="set-language"),
]
