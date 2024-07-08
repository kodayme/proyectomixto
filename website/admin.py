from django.contrib import admin
from .models import *
# Register your models here.

class admin_cliente(admin.ModelAdmin):
    readonly_fields = ('created','update')
    search_fields = ('nombre',)
    list_filter = ('nombre',)

class admin_articulos(admin.ModelAdmin):
    list_display = ('nombre', 'seccion', 'precio')
    search_fields = ('nombre',)

class admin_pedido(admin.ModelAdmin):
    list_filter = ('fecha',)

admin.site.register(cliente,admin_cliente)
admin.site.register(articulos,admin_articulos)
admin.site.register(pedidos,admin_pedido)

# ====================================================ADMIN SERVICIOS ============================================================================

class admi_servicios(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
admin.site.register(Servicios,admi_servicios)



# ==================================================================================================================================================

# ====================================================ADMIN CONTENIDO Y CATEGORIAS ============================================================================

class admin_content(admin.ModelAdmin):
    readonly_fields = ("creado", "actualizado")

class admin_categorico(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(Contenido,admin_content)
admin.site.register(Categoria,admin_categorico)

# =========================================================================================================================================
# ====================================================ADMIN TIENDA Y CATEGORIAS ============================================================================

class admin_producto(admin.ModelAdmin):
    readonly_fields = ("creado", "actualizado")

class admin_categoria(admin.ModelAdmin):
    readonly_fields = ("creado", "actualizado")

admin.site.register(categoria_tienda,admin_categoria)
admin.site.register(Productos,admin_producto)




# =========================================================================================================================================

