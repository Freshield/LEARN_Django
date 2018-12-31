from django.db import models
from django.utils.html import format_html

# Create your models here.
class Type(models.Model):
    id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=20)

    def __str__(self):
        return self.type_name

class Product(models.Model):
    id = models.AutoField('product_id',primary_key=True)
    name = models.CharField(max_length=50)
    weight = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'product information'

    def colored_type(self):
        if 'phone' in self.type.type_name:
            color_code = 'red'
        elif 'tablet' in self.type.type_name:
            color_code = 'blue'
        elif 'smart_wear' in self.type.type_name:
            color_code = 'green'
        else:
            color_code = 'yellow'

        return format_html(
            '<span style="color: {};">{}</span>', color_code, self.type
        )

    colored_type.short_description = 'colored product type'
