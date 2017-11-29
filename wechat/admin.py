from django.contrib import admin
from wechat.models import student
from wechat.models import grade
# Register your models here.
class student_admin(admin.ModelAdmin):

    list_display = ('open_id','xuehao','name')
    # list_editable = ['name','grades']
class grade_admin(admin.ModelAdmin):
    # def change_view(self, request, object_id, form_url='', extra_context=None):
    #     user = request.user
    #     if user.is_superuser:
    #         self.list_display = ['student','yuwen','shuxue','yingyu','zonghe']
    # # raw_id_fields = ("s",)
    #     else:
    #         self.list_display = ['student']

    list_display = ['student','yuwen','shuxue','yingyu','zonghe']


admin.site.register(student,student_admin)
admin.site.register(grade,grade_admin)