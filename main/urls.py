from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.views.decorators.cache import cache_page
from django.conf import settings
from allauth.account.views import confirm_email
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import SimpleRouter
from category.views import CategoryViewSet
from product.views import ProductViewSet

router = SimpleRouter()
router.register('categories', CategoryViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Rentik API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'^rest-auth/registration/account-confirm-email/(?P<key>[-:\w]+)/$', confirm_email, name='account_confirm_email'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('home/', TemplateView.as_view(template_name='dashboard/home.html'), name='home'),
    path('api/v1/accounts/', include('account_custom.urls')),
    path('api/v1/orders/', include('order.urls')),
    path('api/v1/reviews/', include('rating.urls')),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include('product.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
