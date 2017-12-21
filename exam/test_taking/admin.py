from django.contrib import admin
from .models import *


class TestAdmin(admin.ModelAdmin):
    list_display = ['course', 'total_score', 'intro', 'stage', 'order']
    # 顶部搜索框
    search_fields = ['course']
    # 右侧快速查找
    list_filter = ['stage']

class TestDetailAdmin(admin.ModelAdmin):
    list_display = ['id', 'questions', 'course_id', 'level', 'serial_number', 'score', 'questions_type', 'parent']
    search_fields = ['course_id', 'questions', 'questions_type']
    list_filter = ['course_id', 'questions_type', 'level']
    list_display_links = ['questions']

class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'create_user', 'course', 'question', 'update_user', 'user_answer', 'create_time', 'update_time']
    search_fields = ['create_user', 'course', 'question', 'user_answer']
    list_filter = ['course', 'question']
    list_display_links = ['question', 'user_answer']

admin.site.register(Test, TestAdmin)
admin.site.register(TestDetail, TestDetailAdmin)
admin.site.register(UserAnswer, UserAnswerAdmin)

