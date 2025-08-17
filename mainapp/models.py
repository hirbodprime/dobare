# app/models.py

from django.db import models
from django.urls import reverse
import uuid

# مدلی برای ذخیره اطلاعات لباس‌های ارسال شده
class SubmittedCloth(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    brand = models.CharField(max_length=100, blank=True, null=True, verbose_name="برند لباس")
    size = models.CharField(max_length=50, verbose_name="سایز")
    issues = models.TextField(blank=True, null=True, verbose_name="پارگی یا خوردگی")
    full_photo = models.ImageField(upload_to='clothes/full/', verbose_name="عکس کلی")
    fabric_photo = models.ImageField(upload_to='clothes/fabric/', verbose_name="عکس پارچه")
    brand_photo = models.ImageField(upload_to='clothes/brand/', blank=True, null=True, verbose_name="عکس برند")
    submitted_at = models.DateTimeField(auto_now_add=True, verbose_name="زمان ثبت")

    def __str__(self):
        return f"لباس {self.brand or 'بدون برند'} - سایز {self.size}"

    class Meta:
        verbose_name = "لباس ارسال شده"
        verbose_name_plural = "لباس‌های ارسال شده"
        ordering = ['-submitted_at']

# مدل جدید برای محصولات فروشگاه
class Product(models.Model):
    name  = models.CharField(max_length=200, verbose_name="نام محصول")
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="قیمت (تومان)")
    image = models.ImageField(upload_to='products/', verbose_name="تصویر محصول")
    story = models.TextField(blank=True, null=True, verbose_name="داستان لباس")  # اگر نداشتی اضافه کن
    public_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, db_index=True,null=True,blank=True,
                                 verbose_name="کد عمومی (برای لینک/QR)")       # 👈 لینک عمومی
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="زمان ایجاد")

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_detail_public", args=[self.public_id])
