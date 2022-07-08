from django.contrib import admin
from .models import Perfume
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin

class PerfumeAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Perfume, PerfumeAdmin)


