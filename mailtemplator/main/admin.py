from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Users
from .models import SampleTemplates
from .models import Labels
from .models import Templates
from .models import MailAddresses
class UserAdmin(BaseUserAdmin):
    #inlines=(EmployeeInline,)
    #list_display = ('id','user_uuid','username','email')
    list_display = ('id','username','email')
    list_filter = []
class SampleTemplatesAdmin(admin.ModelAdmin):
    list_display = ('id','template_id','template_name')
    list_display = ('id','template_name')
    list_filter = []
class LabelsAdmin(admin.ModelAdmin):
    # list_display = ('id','label_id','label_name')
    list_display = ('id','label_name')
    list_filter = []
class TemplatesAdmin(admin.ModelAdmin):
    # list_display = ('id','template_id','template_name')
    list_display = ('id','template_name')
    list_filter = []
class MailAddressesAdmin(admin.ModelAdmin):
    # list_display = ('id','mailadd_id','mailaddress')
    list_display = ('id','mailaddress')
    list_filter = []
admin.site.register(Users, UserAdmin)
admin.site.register(SampleTemplates,SampleTemplatesAdmin)
admin.site.register(Labels,LabelsAdmin)
admin.site.register(Templates,TemplatesAdmin)
admin.site.register(MailAddresses,MailAddressesAdmin)
