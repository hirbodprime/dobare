# app/views.py

from django.shortcuts import render
from django.http import JsonResponse
from .models import SubmittedCloth, Product # مدل Product اضافه شد
import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .models import Product, SubmittedCloth
def products_page(request):
    products = Product.objects.all().order_by("-created_at")
    return render(request, "products.html", {"products": products})

# صفحه جزئیات/داستان محصول با لینک عمومی
def product_detail_public(request, public_id):
    product = get_object_or_404(Product, public_id=public_id)
    return render(request, "product_detail.html", {"product": product})

# (اختیاری) QR کد به‌صورت PNG
def product_qr(request, public_id):
    product = get_object_or_404(Product, public_id=public_id)
    import qrcode
    from io import BytesIO

    url = request.build_absolute_uri(product.get_absolute_url())
    img = qrcode.make(url)  # ساده و مستقیم

    buf = BytesIO()
    img.save(buf, format="PNG")
    return HttpResponse(buf.getvalue(), content_type="image/png")

# API فعلی برای مودال (با pk)
def product_story(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return JsonResponse({"id": product.id, "name": product.name, "story": product.story or ""})

def home_view(request):
    """
    صفحه اصلی + دریافت فرم (POST) + ارسال لیست محصولات به قالب.
    """
    if request.method == 'POST':
        try:
            brand = request.POST.get('brand', '')
            size = request.POST.get('size', '')
            issues = request.POST.get('issues', '')

            full_photo  = request.FILES.get('full_photo')
            fabric_photo = request.FILES.get('fabric_photo')
            brand_photo  = request.FILES.get('brand_photo')

            if not size or not full_photo or not fabric_photo:
                return JsonResponse({'status': 'error', 'message': 'لطفا فیلدهای ضروری را پر کنید.'}, status=400)

            SubmittedCloth.objects.create(
                brand=brand,
                size=size,
                issues=issues,
                full_photo=full_photo,
                fabric_photo=fabric_photo,
                brand_photo=brand_photo
            )
            return JsonResponse({'status': 'success', 'message': 'اطلاعات با موفقیت ثبت شد.'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    # GET: داده‌های لازم برای رندر صفحه
    products = Product.objects.all()

    # ← لیست سبک برای بابل‌های «پیوند دوباره با نخ»
    product_bubbles = list(
        Product.objects.order_by('-created_at')
        .values('id', 'name')[:16]   # سقف معقول برای کارایی انیمیشن
    )

    context = {
        'products': products,
        'product_bubbles': product_bubbles,
    }
    return render(request, 'index.html', context)


