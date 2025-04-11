from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from produtos.views import ProdutoViewSet
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'produtos',ProdutoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
