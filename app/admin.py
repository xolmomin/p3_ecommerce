from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

from app.models import Category


class CustomMPTTModelAdmin(DraggableMPTTAdmin):
    exclude = ('slug', )
    # specify pixel amount for this ModelAdmin only:
    mptt_level_indent = 20

admin.site.register(Category, CustomMPTTModelAdmin)