from django.forms import ModelChoiceField
from django.contrib import admin

from .models import *

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class HeadphonesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='naushniki'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class ProtectiveGlassesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='zashitnye-stekla'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Headphones, HeadphonesAdmin)
admin.site.register(ProtectiveGlasses, ProtectiveGlassesAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
