from django.contrib import admin
from .models import Photo, User



#admin.ModelAdmin 클래스 상속받음
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'created', 'updated']
    raw_id_fields = ['author']
    list_filter = ['created', 'updated', 'author']
    search_fields = ['text', 'created']
    ordering = ['-updated', '-created']

admin.site.register(User) #User 모델 등록
admin.site.register(Photo, PhotoAdmin) #포토, 포토 어드민 테이블 등록

