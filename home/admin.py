from django.contrib import admin
from .models import User, Categoria, Livro
# Register your models here.
class LivroAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'link')
    list_display_links = ('id',)
    list_editable = ('titulo', 'link',)

class UserAdmin(admin.ModelAdmin):
	pass

class CategoriaAdmin(admin.ModelAdmin):
	pass
admin.site.register(User,UserAdmin)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Livro,LivroAdmin)