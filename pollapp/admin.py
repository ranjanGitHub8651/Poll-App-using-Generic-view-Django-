from django.contrib import admin
from .models import Question, Choice

admin.site.site_header = "Polls Admin"
admin.site.site_title = "Polls Admin Portal"
admin.site.index_title = "Welcome to Polls Portal"


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmit(admin.ModelAdmin):

    list_display = ("question_text", "pub_date", "was_published_recently")
    list_filter = ["pub_date"]
    search_fields = ["question_text"]
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmit)
