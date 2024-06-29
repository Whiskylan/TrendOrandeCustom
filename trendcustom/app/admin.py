from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from app.models import Brand, Color, Keycap, Keycap_Material, Keycap_Profile, Switch, Case, Completed_Keyboard, Plate, Form_Factor, Plata, Stabilizer, Case_Material

@admin.register(Brand)
class AdminBrand(ImportExportModelAdmin, admin.ModelAdmin):
    pass

@admin.register(Color)
class AdminColor(ImportExportModelAdmin, admin.ModelAdmin):
    pass

@admin.register(Keycap)
class AdminKeycap(ImportExportModelAdmin, admin.ModelAdmin):
    pass

@admin.register(Keycap_Material)
class AdminKeycap_Material(ImportExportModelAdmin, admin.ModelAdmin):
    pass

@admin.register(Keycap_Profile)
class AdminKeycap_Profile(ImportExportModelAdmin, admin.ModelAdmin):
    pass

@admin.register(Switch)
class AdminSwitch(ImportExportModelAdmin, admin.ModelAdmin):
    pass

@admin.register(Case)
class AdminCase(ImportExportModelAdmin, admin.ModelAdmin):
    pass

@admin.register(Completed_Keyboard)
class AdminCompleted_Keyboard(ImportExportModelAdmin, admin.ModelAdmin):
    pass

@admin.register(Plate)
class AdminPlate(ImportExportModelAdmin, admin.ModelAdmin):
    pass

@admin.register(Form_Factor)
class AdminForm_Factor(ImportExportModelAdmin, admin.ModelAdmin):
    pass

@admin.register(Plata)
class AdminPlata(ImportExportModelAdmin, admin.ModelAdmin):
    pass

@admin.register(Stabilizer)
class AdminStabilizer(ImportExportModelAdmin, admin.ModelAdmin):
    pass

@admin.register(Case_Material)
class AdminCase_Material(ImportExportModelAdmin, admin.ModelAdmin):
    pass