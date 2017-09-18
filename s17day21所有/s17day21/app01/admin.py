from django.contrib import admin
from app01 import models

class DepartAdmin(admin.ModelAdmin):
    list_display = ['id','title']

admin.site.register(models.Depart,DepartAdmin)

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','pwd']
    empty_value_display = "这里没数据"
    # #list_display_links = ['email','name']
    # list_filter = ['name','dp']
    # list_editable = ['name',]
    # search_fields = ['name',]
    #
    # def func(self, request, queryset):
    #     print(self, request, queryset)
    #     queryset.delete()
    #     print(request.POST.getlist('_selected_action'))
    #
    # func.short_description = "xxxxxx"
    # actions = [func, ]
    #
    # # change_list_template = "login.html"
    # raw_id_fields = ['dp']
    # exclude = ('name','email')
    # readonly_fields = ['phone']

    # fieldsets = (
    #     ('基本数据', {
    #         'fields': ('name', 'pwd', 'email',)
    #     }),
    #     ('其他', {
    #         'classes': ('collapse', 'wide', 'extrapretty'),  # 'collapse','wide', 'extrapretty'
    #         'fields': ('phone', 'dp'),
    #     }),
    # )
    # filter_vertical = ("roles",)  # 或filter_horizontal = ("m2m字段",)
    filter_horizontal = ("roles",)  # 或filter_horizontal = ("m2m字段",)
    ordering = ['id']

    # def view_on_site(self, obj):
    #     return 'https://www.baidu.com'

    # radio_fields = {"dp": admin.VERTICAL}
    # radio_fields = {"dp": admin.HORIZONTAL}
    # prepopulated_fields = {'phone':('name','email')}
admin.site.register(models.UserInfo,UserInfoAdmin)

admin.site.register(models.Role)
