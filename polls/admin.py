from django.contrib import admin

# Register your models here.
from .models import Question, Choice


class ChoiceInLine(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_data'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInLine]
    list_filter = ['pub_data']
    list_display = ('question_text', 'pub_data', 'was_published_recently')
    search_fields = ['question_text']

admin.site.site_header = 'polls'
admin.site.register(Question, QuestionAdmin)
