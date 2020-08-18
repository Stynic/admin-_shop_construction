from django.contrib import admin
from .models import Image, Video


class AdminCatalogImage(admin.ModelAdmin):
    list_display = ['image',
                    'image_img']
    readonly_fields = ['image_img']
    fields = ['image', 'image_img']


admin.site.register(Image, AdminCatalogImage)
admin.site.register(Video)
