from django.contrib import admin
from .models import Note_middle, Perfume, Review, Note_base, Note_top, Note_middle, Perfumer
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin

class PerfumeAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Perfume, PerfumeAdmin)
admin.site.register(Review)
admin.site.register(Note_top)
admin.site.register(Note_middle)
admin.site.register(Note_base)
admin.site.register(Perfumer)



