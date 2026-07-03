from django.contrib import admin
from .models import Alumnos
from .models import Comentario
from .models import ComentarioContacto

# Register your models here.
class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display=('matricula','nombre','carrera','turno')
    search_fields=('matricula','nombre','carrera','turno')
    date_hierachy='created'
    list_filter=('carrera','turno')
    #Las nuevas q puse yo 
    list_per_page = 5
    list_display_links = ('matricula', 'nombre') 
    list_editable = ('turno',)

admin.site.register(Alumnos, AdministrarModelo)

class AdministrarComentarios(admin.ModelAdmin):
    list_display=('id','coment')
    search_fields=('id','created')
    list_filter=('created',)
    date_hierachy='created'
    readonly_fields=('created', 'id')

admin.site.register(Comentario, AdministrarComentarios)

class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display = ('id', 'mensaje')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')
admin.site.register(ComentarioContacto, AdministrarComentariosContacto)