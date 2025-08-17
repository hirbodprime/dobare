# project/urls.py

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home_view ,product_story,product_detail_public,product_qr,products_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'), # آدرس اصلی سایت
    # API مودال
    path('products/<int:pk>/story/', product_story, name='product_story'),

    # لینک عمومی و QR
    path('p/<uuid:public_id>/', product_detail_public, name='product_detail_public'),
    path('p/<uuid:public_id>/qr.png', product_qr, name='product_qr'),
    path("products/", products_page, name="products_page"),

]

# این بخش برای نمایش فایل‌های آپلود شده در حالت توسعه (Debug) ضروری است
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
