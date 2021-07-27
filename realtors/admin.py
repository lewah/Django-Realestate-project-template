from django.contrib import admin
from.models import Realtor

# Register your models here.
class RealtorsAdmin(admin.ModelAdmin):
    list_display = ('id','name','phone','email','is_mvp')
    list_display_links = ('id','name',)
    list_filter = ('is_mvp',)
    list_editable = ('is_mvp',)
    search_fields = ('name','email',)

admin.site.register(Realtor,RealtorsAdmin)