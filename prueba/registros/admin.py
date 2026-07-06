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
    list_per_page = 5
    list_display_links = ('matricula', 'nombre') 
    list_editable = ('turno',)

    def get_readonly_fields(self, request, obj=None):
        # Si el usuario pertenece al grupo "Usuarios"
        if request.user.groups.filter(name="usuarios").exists():
            # Bloquea los campos (la coma al final de la tupla es buena práctica)
            return ('matricula', 'carrera', 'turno')
        # Cualquier otro usuario que no pertenece al grupo usuarios
        else:
            # Bloquea campos
            return ('created', 'updated')    

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