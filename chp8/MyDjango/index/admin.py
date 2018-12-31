from django.contrib import admin
from .models import *

admin.site.site_title = 'MyDjango chp8 backend'
admin.site.site_header = 'MyDjango'

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'weight', 'size', 'type', 'colored_type']

    search_fields = ['id', 'name', 'weight', 'size', 'type__type_name']

    list_filter = ['id', 'name', 'weight', 'size', 'type__type_name']

    ordering = ['id']

    fields = ['name', 'weight', 'size', 'type']

    readonly_fields = ['name']

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            self.readonly_fields = []

        return self.readonly_fields

    def get_queryset(self, request):
        qs = super(ProductAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs.filter(id__lt=10)
        else:
            return qs.filter(id__lt=6)