from django.contrib import admin
import time
import os

from .models import Question
from .models import Choice
from .models import Company

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3


class QuestionAdmin(admin.ModelAdmin):

	fieldsets = [
		(None, {'fields': ['question_text']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']})
	]
	inlines = [ChoiceInline]
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question_text']


class CompanyAdmin(admin.ModelAdmin):

	exclude = ['created', 'updated']
	add_form_template = os.path.dirname(os.path.dirname(__file__)) + 'template/admin/company.html'

	def save_model(self, request, obj, form, change):
		print(obj)
		if not obj.pk:
			obj.created = int(time.time())
		else:
			obj.updated = int(time.time())
		obj.save()


admin.site.register(Question, QuestionAdmin)
admin.site.register(Company, CompanyAdmin)


# Register your models here.
