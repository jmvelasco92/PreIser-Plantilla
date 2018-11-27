from django.urls import path
from .views import *

urlpatterns =[
	
	#INICIO 

	path('inicio/',vista_inicio,name='vista_inicio'),
	path('',vista_login,name='vista_login'),
	path('logout/',vista_logout,name="vista_logout"),
#---------------------------------------------------------------------------------------------------------------------
	#BODREGA MATERIAL

	path('ver_detalle',detalle_ver,name='detalle_ver'),
	path('agrr_bodega_material',agr_bodega_materiall,name='agr_bodega_materiall'),
	path('editar_bodega_material/<int:id_bdm>/',editar_bodega_material,name="editar_bodega_material"),
	path('eliminar_bodega_material/<int:id_bdm>/',eliminarr_bodega_material,name="eliminarr_bodega_material"),
#-----------------------------------------------------------------------------------------------------------------
#urls de nombre_material
	path('agregar_nombre_material/',vista_agregar_nombre_material,name="vista_agregar_nombre_material"),
	path('editar_nombre_material/<int:id_nm>/',vista_editar_nombre_material,name="vista_editar_nombre_material"),
	path('eliminar_nombre_material/<int:id_nm>/',vista_eliminar_nombre_material,name="vista_eliminar_nombre_material"),
	path('lista_nombre_material/',vista_lista_nombre_material,name="vista_lista_nombre_material"),
#---------------------------------------------------------------------------------------------------------------
	# Detalle_Prestamo

	path('ListaD/',lista_DetallePrestamo,name='lista_DetallePrestamo'),
	path('verD/<int:id_Dprest>/',ver_DetallePrestamo,name='ver_DetallePrestamo'),
	path('eliminarD/<int:id_Dprest>/',elimnar_DetallePrestamo,name='elimnar_DetallePrestamo'),
#----------------------------------------------------------------------------------------------------------------
	#urls de marca
	path('lista_marca/',vista_lista_marca,name="vista_lista_marca"),
	path('agregar_marca/',vista_agregar_marca,name="vista_agregar_marca"),
	path('editar_marca/<int:id_marca>/',vista_editar_marca,name="vista_editar_marca"),
	path('eliminar_marca/<int:id_marca>/',vista_eliminar_marca,name="vista_eliminar_marca"),
#----------------------------------------------------------------------------------------------------------------
	#urls de materiales
	path('agregar_material/',vista_agregar_material,name="vista_agregar_material"),
	path('lista_material/',vista_lista_material,name="vista_lista_material"),
	path('editar_material/<int:id_material>/',vista_editar_material,name="vista_editar_material"),
	path('eliminar_material/<int:id_material>/',vista_eliminar_material,name="vista_eliminar_material"),
	path('ver_material/<int:id_material>/',vista_ver_material,name="vista_ver_material"),
#----------------------------------------------------------------------------------------------------------
#urls de devoluciones
	path('devolucion/<int:id_prest>/',devolucion_prestamo,name='devolucion_prestamo'),
#------------------------------------------------------------------------------------------------------------------	
	#urls de prestamo
	path('Lista/',lista_prestamo,name='lista_prestamo'),
	path('Agregar/',agregar_prestamo,name='agregar_prestamo'),
	path('editar/<int:id_prest>/',editar_prestamo,name='editar_prestamo'),
	path('elimnar/<int:id_prest>/',eliminar_prestamo,name='eliminar_prestamo'),
#------------------------------------------------------------------------------------------------------------------
	#urls de la tabla categoria
	path('categoria/',nombre_categoria,name="nombre_categoria"),
	path('editar_categoria/<int:id_cat>/',editarr_categoria,name='editarr_categoria'),
	path('agregar_categoria/',agr_categoria,name='agr_categoria'),
	path('eliminar_categoria/<int:id_cat>/',eliminarr_categoria,name='eliminarr_categoria'),

#--------------------------------------------------------------------------------------------------------------------
	# AQUI INICIAN LAS URLS DE BODEGA-----
	path('lista_bodega/',vista_lista_bodega, name='vista_lista_bodega'),
	path('ver_bodega/<int:id_bod>/',vista_ver_bodega,name='vista_ver_bodega'),
	path('agregar_bodega/',vista_agregar_bodega,name='vista_agregar_bodega'),
	path('editar_bodega/<int:id_bod>/',vista_editar_bodega, name= 'vista_editar_bodega'),
	path('eliminar_bodega/<int:id_bod>/',vista_eliminar_bodega, name= 'vista_eliminar_bodega'),

	# AQUI TERMINAN LAS URLS DE BODEGA-----

#----------------------------------------------------------------------------------------------------------------
	#urls de la tabla cuentadante
	path('vista_cuentadante',lista_cuentadante,name ='lista_cuentadante'),
	path('agr_cuentadante',agregar_cuentadante,name='agregar_cuentadante'),
	path('editar_cuentadante/<int:id_cue>/',editarr_cuentadante,name='editarr_cuentadante'),
	path('eliminar_cuentadante/<int:id_cue>/',eliminarr_cuentadante,name='eliminarr_cuentadante'),

#-----------------------------------------------------------------------------------------------------------------
	#urls de la tabla programa
	path('lista_programas/',vista_lista_programas, name = 'vista_lista_programas'),
	path('agregar_programas/',vista_agregar_programas, name = 'vista_agregar_programas'),
	path('editar_programas/<int:id_pro>/',vista_editar_programas, name = 'vista_editar_programas'),
	path('eliminar_programas<int:id_pro>/', vista_eliminar_programas, name='vista_eliminar_programas'),

#-----------------------------------------------------------------------------------------------------------------
	#urls de la tabla FICHA
	path('ver_ficha',detalle_ficha,name='detalle_ficha'),
	path('agregar_ficha',agr_ficha,name='agr_ficha'),
	path('editar_ficha/<int:id_fic>/',edit_ficha,name='edit_ficha'),
	path('eliminar_ficha/<int:id_fic>/',elim_ficha,name='elim_ficha'),

#-----------------------------------------------------------------------------------------------------------------
	#APRENDIZ
	path('lista_aprendiz/',vista_lista_aprendiz,name='vista_lista_aprendiz'),
	path('agregar_aprendiz/',vista_agregar_aprendiz,name='vista_agregar_aprendiz'),
	path('eliminar_aprendiz/<int:id_apr>/', vista_eliminar_aprendiz, name='vista_eliminar_aprendiz'),
	path('editar_aprendiz/<int:id_apr>/',vista_editar_aprendiz,name='vista_editar_aprendiz'),

#----------------------------------------------------------------------------------------------------------------
#urls de reportes
	path('reporte/',vista_reporte,name="vista_reporte"),
]