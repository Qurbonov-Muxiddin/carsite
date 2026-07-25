
from django.db import models
from django.urls import reverse
 
 
from django.contrib.auth.models import User
 
 
 
 
 
 
 
 
 
 
 
 
 
class Brand(models.Model):
    """Mashina brendi (masalan: Chevrolet, Toyota, BMW)"""
    name = models.CharField("Brend nomi", max_length=100, unique=True)
 
    class Meta:
        verbose_name = "Brend"
        verbose_name_plural = "Brendlar"
        ordering = ["name"]
 
    def __str__(self):
        return self.name
 
 
 
class Car(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="cars"
    )
 
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name="cars",
    )
 
    name = models.CharField(max_length=150)
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="cars/", blank=True, null=True)
    isActive = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
 
    class Meta:
        ordering = ["-created_at"]
 
    def __str__(self):
        return f"{self.brand.name} {self.name}"
 
    def get_absolute_url(self):
        return reverse("cars:car_detail", kwargs={"pk": self.pk})
    