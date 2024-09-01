from django.db import models


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=100, null=False)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name="car_brand")
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to="cars/", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    # função responmsável por retornar o nome/string da minha classe e não da do models.Model
    def __str__(self):
        return self.model


class CarInventory(models.Model):
    cars_count = models.IntegerField(blank=True, null=True)
    cars_value = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(null=True, auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]  # ordenar de forma decrescente

    def __str__(self):
        return f"{self.cars_count} - {self.cars_value}"
