from django.contrib import admin
from .models import Author, Book, BookInstance, Genre

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
	fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'display_genre')
	list_filter = ('author',)
	search_fields = ('title', 'author__last_name', 'author__first_name')

	@admin.display(description='Genre')
	def display_genre(self, obj):
		return ', '.join(genre.name for genre in obj.genre.all())

class BookInstanceAdmin(admin.ModelAdmin):
	list_display = ('book', 'status', 'due_back', 'id')
	list_filter = ('status', 'due_back')

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(Genre)
# Register your models here.
