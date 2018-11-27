from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import login,logout,authenticate
from django.forms import inlineformset_factory,formset_factory
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.

def vista_login(request):
	usu=""
	cla=""
	if request.user.is_authenticated:
		return redirect('/inicio/')

	else:	
		if request.method=='POST':
			formulario =login_form(request.POST)
			if formulario.is_valid():
				usu=formulario.cleaned_data['user']
				cla=formulario.cleaned_data['password']
				usuario=authenticate(username=usu,password=cla)
				if usuario is not None and usuario.is_active:
					login(request,usuario)
					return redirect('/inicio/')
				else:
					msj = "Usuario o Clave Incorrectos"
		else:
			formulario=login_form()
		return render(request,'login.html',locals())


def vista_logout(request):
	logout(request)
	return redirect('vista_login')

@login_required(login_url='vista_login')
def vista_inicio (request):
	return render (request,'inicio.html',locals())
#-------------------------------------------------------------------------------------------------------------------
#views de la tabla marca
@login_required(login_url='vista_login')
def vista_lista_marca(request):
	lista = Marca.objects.all()
	return render(request,'vista_lista_marca.html',locals())

@staff_member_required(login_url='vista_login')
def vista_agregar_marca(request):
	if request.method == 'POST':
		formulario = agregar_marca_form(request.POST,request.FILES)
		if formulario.is_valid():
			marca = formulario.save(commit=False)
			marca.status=True
			marca.save()
			return redirect('/lista_marca/')

	else:
		formulario = agregar_marca_form()
	return render(request,'vista_agregar_marca.html',locals())

@staff_member_required(login_url='vista_login')
def vista_editar_marca(request,id_marca):
	marca = Marca.objects.get(id=id_marca)
	if request.method == 'POST':
		formulario = agregar_marca_form(request.POST,request.FILES,instance=marca)
		if formulario.is_valid():
			marca = formulario.save()
			return redirect('/lista_marca/')
	else:
		formulario = agregar_marca_form(instance=marca)
	return render(request,'vista_agregar_marca.html',locals())

@staff_member_required(login_url='vista_login')
def vista_eliminar_marca(request,id_marca):
	marca = Marca.objects.get(id=id_marca)
	marca.delete()
	return redirect('/lista_marca/')
#-----------------------------------------------------------------------------------------------------------------
#views de la tabla nombre_material
@staff_member_required(login_url='vista_login')
def vista_agregar_nombre_material (request):
	if request.method == 'POST':
		formulario = agregar_nombre_material_form(request.POST)
		if formulario.is_valid():
			nombre_material = formulario.save(commit=False)
			nombre_material.save()
			return redirect('/lista_nombre_material/')
	else:
		formulario = agregar_nombre_material_form()

	return render(request,'vista_agregar_nombre_material.html',locals())

@staff_member_required(login_url='vista_login')
def vista_editar_nombre_material(request,id_nm):
	nombre_material = Nombre_Material.objects.get(id=id_nm)
	if request.method == 'POST':
		formulario = agregar_nombre_material_form(request.POST,request.FILES,instance=nombre_material)
		if formulario.is_valid():
			formulario.save()
			return redirect('/lista_nombre_material/')
	else:
		formulario = agregar_nombre_material_form(instance=nombre_material)

	return render(request,'vista_agregar_nombre_material.html',locals())

@staff_member_required(login_url='vista_login')
def vista_eliminar_nombre_material(request,id_nm):
	nombre_material = Nombre_Material.objects.get(id=id_nm)
	nombre_material.delete()
	return redirect('/lista_nombre_material/')

@staff_member_required(login_url='vista_login')
def vista_lista_nombre_material(request):
	lista = Nombre_Material.objects.all()
	return render(request,'lista_nombre_material.html',locals())

#------------------------------------------------------------------------------------------------------------------
#views de la tabla materiales

@staff_member_required(login_url='vista_login')
def vista_agregar_material(request):
	Bodega_MaterialFormset = formset_factory(Bodega_Material_form)
	if request.method == 'POST':
		formulario = agregar_material_form(request.POST, request.FILES)
		bod = Bodega_MaterialFormset(request.POST)
		if formulario.is_valid() and bod.is_valid():
			try:
				material = formulario.save(commit=False)
				material.save()
				
				for i in bod:
					f = i.save(commit=False)
					f.material=material
					f.save()
				return redirect('/lista_material/')
				
			except:
				msj_bod = "los datos de la bodega no deben estar vacios" 

	else:
		formulario = agregar_material_form()
		bod = Bodega_MaterialFormset()

	return render(request,'vista_agregar_material.html',locals())

@login_required(login_url='vista_login')
def vista_lista_material(request):
	lista = Material.objects.all()
	return render(request,'vista_lista_material.html',locals())

@staff_member_required(login_url='vista_login')
def vista_editar_material(request,id_material):
	material = Material.objects.get(id=id_material)
	lista_bodegas = Bodega_Material.objects.filter(material=material)
	
	Bodega_MaterialFormset = inlineformset_factory(Material,Bodega_Material,form=Bodega_Material_form,can_delete=False,extra=0)
	if material.tipo_elemento == 'Devolutivo':
		if request.method == 'POST':
			formulario = agregar_material_form(request.POST,request.FILES,instance=material)
			bod = Bodega_MaterialFormset(request.POST,instance=material)
			if formulario.is_valid() and bod.is_valid():
				formulario.save()
				bod.save()
				return redirect('/lista_material/')
		else:
			formulario = agregar_material_form(instance=material)
			bod = Bodega_MaterialFormset(instance=material)

		return render(request,'vista_agregar_material.html',locals())
	else:
		if request.method == 'POST':
			formulario = agregar_material_form(request.POST,request.FILES,instance=material)
			bod = Bodega_MaterialFormset(request.POST,instance=material)
			if formulario.is_valid() and bod.is_valid():
				formulario.save()
				bod.save()
				return redirect('/lista_material/')
		else:
			formulario = agregar_material_form(instance=material)
			bod = Bodega_MaterialFormset(instance=material)
		return render(request,'vista_editar_material_consumible.html',locals())

@staff_member_required(login_url='vista_login')
def vista_eliminar_material(request,id_material):
	material = Material.objects.get(id=id_material)
	material.delete()
	return redirect('/lista_material/')

@login_required(login_url='vista_login')
def vista_ver_material(request,id_material):
	material = Material.objects.get(id=id_material)
	return render(request,'vista_ver_material.html',locals())
#------------------------------------------------------------------------------------------------------------------
#views de la tabla prestamo

@login_required(login_url='vista_login')
def lista_prestamo(request):
	lista=Prestamo.objects.filter()
	return render(request,'lista_prestamo.html',locals())

@login_required(login_url='vista_login')
def agregar_prestamo(request):
	

	Detalle_PrestamoFormSet = formset_factory(agregar_DPrestamoF,max_num=50,can_delete=True)
	if request.method=='POST':
		formulario=agregar_prestamoF(request.POST)
		formset=Detalle_PrestamoFormSet(request.POST)
		if formulario.is_valid() and formset.is_valid():			
			prest=formulario.save(commit=False)			

	
			codigos = []
			for instance in formset:
				i=instance.save(commit=False)
				if prest.estado =='Activo':
					i.material.estado='No Disponible'
					i.material.save()
				print("xxxxxxxxxxxxxxx")
				print(i.material.codigo_sena)
				codigos.append(i)
				print("xxxxxxxxxxxxxxx")

			x=1
			aux = 0	
			if len(codigos) == 0:
				print ("error lista en 0 detalles")
				p = False
			elif len(codigos) == 1:
				p = True
			else:
				p=True
				'''		for i in range(len(codigos)-1):
											for j in range(1,len(codigos) , 1):
												if codigos[i] != codigos[j]:
													print ("NO Haay Repetidos")
													p = True
													print (p)
												else:
													print(codigos[i])
													print(codigos[j])
													print ("Haay Repetidos")
													p = False
													break
													print (p)
						'''
			'''	print (p)				
									print (codigos)	'''
			#guarda el prestamo con los detalles despues de validar 	
			if p:
				prest.save()
				for j in codigos:
					j.prestamo = prest
					j.save()	


			return redirect('/Lista/')
	else:
		formulario=agregar_prestamoF()
		formset=Detalle_PrestamoFormSet()
	return render(request,'agregar_prestamo.html',locals(),{'formset': formset})

@login_required(login_url='vista_login')
def editar_prestamo(request,id_prest):
	p=Prestamo.objects.get(id=id_prest)
	Detalle_PrestamoFormSet = inlineformset_factory(Prestamo,Detalle_Prestamo, form=agregar_DPrestamoF,can_delete=True)
	if request.method=='POST':
		formulario=agregar_prestamoF(request.POST,instance=p)
		formset=Detalle_PrestamoFormSet(request.POST,instance=p)
		if formulario.is_valid() and formset.is_valid():					
			formulario.save()			
			formset.save()			
			return redirect('/Lista/')
	else:
		formulario=agregar_prestamoF(instance=p)
		formset=Detalle_PrestamoFormSet(instance=p)
	return render(request,'agregar_prestamo.html',locals())

@login_required(login_url='vista_login')
def eliminar_prestamo(request,id_prest):
	p=Prestamo.objects.get(id=id_prest)
	p.delete()
	return redirect('/Lista/')
#---------------------------------------------------------------------------------------------------------------
#views de devoluciones
@login_required(login_url='vista_login')
def devolucion_prestamo(request,id_prest):
	p =Prestamo.objects.get(id=id_prest)
	Detalle_PrestamoFormSet = inlineformset_factory(Prestamo,Detalle_Prestamo,extra=0, form=dev_DPrestamoF,can_delete=True)
	if request.method=='POST':
		formulario=dev_prestamoF(request.POST,instance=p)
		formset=Detalle_PrestamoFormSet(request.POST,instance=p)
		if formulario.is_valid() and formset.is_valid():					
			formulario.save()
			for instance in formset:	
				i=instance.save(commit=False)
				if i.estado_elemento_prestamo =='Entregado':
					i.material.estado = 'Disponible'					
					i.prestamo.estado='Terminado'   
					i.material.save()
					i.prestamo.save()			
				
				if i.estado_devolucion=="malo":
					i.material.estado='No Disponible'   
					i.material.save()
				i.save()			
						
			return redirect('/Lista/')
	else:
		formulario=dev_prestamoF(instance=p)
		formset=Detalle_PrestamoFormSet(instance=p)
	return render(request,'ver_prestamo.html',locals())
	
#------------------------------------------------------------------------------------------------------------------
#views de la tabla destalle_prestamoo

@login_required(login_url='vista_login')
def lista_DetallePrestamo(request):
	lista=Detalle_Prestamo.objects.filter()
	return render(request,'lista_DetallePrestamo.html',locals())


@login_required(login_url='vista_login')
def ver_DetallePrestamo(request,id_Dprest):
	p =Prestamo.objects.get(id=id_Dprest)
	Detalle_PrestamoFormSet = inlineformset_factory(Prestamo,Detalle_Prestamo,extra=0, form=det_DPrestamoF,can_delete=True)
	if request.method=='POST':
		formulario=det_prestamoF(request.POST,instance=p)
		formset=Detalle_PrestamoFormSet(request.POST,instance=p)
		return render(request,'ver_DetallePrestamo.html',locals())			
	else:
		formulario=dev_prestamoF(instance=p)
		formset=Detalle_PrestamoFormSet(instance=p)
	return render(request,'ver_DetallePrestamo.html',locals())


@login_required(login_url='vista_login')
def elimnar_DetallePrestamo(request,id_Dprest):
	Dp=Detalle_Prestamo.objects.get(id=id_Dprest)
	Dp.delete()
	return redirect('/ListaD/')


#-------------------------------------------------------------------------------------------------------------------
#views de la tabla categoria
@login_required(login_url='vista_login')
def nombre_categoria(request):
	lista = Categoria.objects.filter()
	return render (request,'categoria.html',locals())


@staff_member_required(login_url='vista_login')
def agr_categoria(request):
	if request.method == "POST":
		formulario = categoria_form(request.POST,request.FILES)
		if formulario.is_valid():
			prod = formulario.save(commit =False)
			prod.status= True
			prod.save()
			formulario.save_m2m()
			return redirect ('/categoria')
	else:
		formulario = categoria_form()
	return render (request,'agregar_categoria.html',locals())

@staff_member_required(login_url='vista_login')
def editarr_categoria(request,id_cat):
	cat = Categoria.objects.get(id=id_cat)
	if request.method == "POST":
		formulario = categoria_form(request.POST, request.FILES,instance = cat)
		if formulario.is_valid():
			cat = formulario.save()
		return redirect ('/categoria')
	else:
		formulario = categoria_form(instance=cat)
	return render (request,'agregar_categoria.html',locals())

@staff_member_required(login_url='vista_login')
def eliminarr_categoria(request,id_cat):
	cat=Categoria.objects.get(id=id_cat)
	cat.delete()
	return redirect('/categoria')
#------------------------------------------------------------------------------------------------------------------
	# AQUI INICIAN LAS VISTAS DE DODEGAS.......
	#BODEGAS
@login_required(login_url='vista_login')
def vista_lista_bodega(request):
	lista=Bodega.objects.filter()
	return render (request, 'lista_bodega.html',locals())

	
@staff_member_required(login_url='vista_login')
def vista_agregar_bodega(request):
	if request.method== 'POST':
		formulario= agregar_bodega_form(request.POST,request.FILES)
		if formulario.is_valid():
			bod=formulario.save(commit=False)
			bod.status= True
			bod.save()
			formulario.save_m2m()
			return redirect('/lista_bodega')
	else:
		formulario=agregar_bodega_form()
	return render(request,'vista_agregar_bodega.html',locals())

@login_required(login_url='vista_login')
def vista_ver_bodega(request, id_bod):
	bod = Bodega.objects.get(id=id_bod)
	return render (request, 'ver_bodega.html', locals())

@staff_member_required(login_url='vista_login')	
def vista_editar_bodega(request, id_bod):
	bod	 = Bodega.objects.get(id=id_bod)
	if request.method== 'POST':
		formulario = agregar_bodega_form(request.POST, request.FILES, instance=bod)

		if formulario.is_valid():
			bod = formulario.save()
			return redirect ('/lista_bodega/')

	else :
		formulario = agregar_bodega_form(instance = bod)

	return render (request,'vista_agregar_bodega.html',locals())	 

@staff_member_required(login_url='vista_login')
def vista_eliminar_bodega(request, id_bod):
	bod= Bodega.objects.get(id=id_bod)
	bod.delete()
	return redirect ('/lista_bodega/')
#------------------------------------------------------------------------------------------------------------------
#views de la tabla cuentadante
		
@login_required(login_url='vista_login')
def lista_cuentadante(request):
	lista = Cuentadante.objects.filter()
	return render(request,'lista_cuentadante.html', locals())

@staff_member_required(login_url='vista_login')
def agregar_cuentadante(request):
	if request.method == "POST":
		formulario = cuentadante_form(request.POST, request.FILES)
		if formulario.is_valid():
			prod = formulario.save(commit = False)
			prod.status = True
			prod.save()
			formulario.save_m2m()
			return redirect ('/vista_cuentadante')
	else:
		formulario = cuentadante_form()
	return render (request,'ingresar_cuentadante.html',locals())

@staff_member_required(login_url='vista_login')
def editarr_cuentadante(request,id_cue):
	cue = Cuentadante.objects.get(id=id_cue)
	if request.method == "POST":
		formulario = cuentadante_form (request.POST,request.FILES, instance=cue)
		if formulario.is_valid():
			cue = formulario.save()
			return redirect ('/vista_cuentadante')
	else:
		formulario = cuentadante_form(instance=cue)
	return render(request,'ingresar_cuentadante.html',locals())

@staff_member_required(login_url='vista_login')
def eliminarr_cuentadante(request,id_cue):
	cue =Cuentadante.objects.get(id=id_cue)
	cue.delete()
	return redirect('/vista_cuentadante')
#------------------------------------------------------------------------------------------------------------------
#views de la tabla programa

@login_required(login_url='vista_login')	
def vista_lista_programas(request):
	lista = Programa.objects.all()
	return render(request,'lista_programas.html',locals())

@staff_member_required(login_url='vista_login')
def  vista_agregar_programas(request):
	if (request.method == 'POST') :
		formulario = agregar_programas_form(request.POST,request.FILES)
		if formulario.is_valid():
			pro =formulario.save(commit =False)
			pro.status =True
			pro.save()
			formulario.save_m2m()
			return redirect ('/lista_programas/')
	else:
		formulario = agregar_programas_form()
	return render(request, 'agregar_programa.html',locals())

@staff_member_required(login_url='vista_login')
def vista_editar_programas(request,id_pro):
	pro =Programa.objects.get(id=id_pro)
	if (request.method == 'POST'):
		formulario =agregar_programas_form(request.POST,instance=pro)
		if formulario.is_valid():
			pro.save()
			return redirect ('/lista_programas/')
	else:
		formulario =agregar_programas_form(instance =pro)
	return render (request, 'agregar_programa.html', locals())

@staff_member_required(login_url='vista_login')
def vista_eliminar_programas(request,id_pro):
	pro =Programa.objects.get(id =id_pro)
	pro.delete()
	return redirect('/lista_programas')
#------------------------------------------------------------------------------------------------------------------
#views de la tabla ficha
@login_required(login_url='vista_login')
def detalle_ficha(request):
	lista = Ficha.objects.filter()
	return render (request,'ver_ficha.html',locals())

@staff_member_required(login_url='vista_login')
def agr_ficha(request):
	if request.method == "POST":
		formulario = ficha_form(request.POST, request.FILES)
		if formulario.is_valid():
			prod = formulario.save(commit = False)
			prod.status = True
			prod.save()
			formulario.save_m2m()
			return redirect ('/ver_ficha')
	else:
		formulario = ficha_form()
	return render (request,'agregar_ficha.html',locals())

@staff_member_required(login_url='vista_login')
def edit_ficha(request,id_fic):
	fic = Ficha.objects.get(id=id_fic)
	if request.method == "POST":
		formulario = ficha_form (request.POST,request.FILES, instance=fic)
		if formulario.is_valid():
			fic = formulario.save()
			return redirect ('/ver_ficha')
	else:
		formulario = ficha_form(instance=fic)
	return render(request,'agregar_ficha.html',locals())

@staff_member_required(login_url='vista_login')
def elim_ficha(request,id_fic):
	fic =Ficha.objects.get(id =id_fic)
	fic.delete()
	return redirect('/ver_ficha')

#------------------------------------------------------------------------------------------------------------------
#views de la tabla bodega material
		
@login_required(login_url='vista_login')
def detalle_ver(request):
	lista =  Bodega_Material.objects.filter()
	return render (request,'bodega_material.html',locals())

@staff_member_required(login_url='vista_login')
def agr_bodega_materiall(request):
	if request.method == "POST":
		formulario = Bodega_Material_form(request.POST, request.FILES)
		if formulario.is_valid():
			prod = formulario.save(commit = False)
			prod.status = True
			prod.save()
			formulario.save_m2m()
			return redirect ('/inicio')
	else:
		formulario = Bodega_Material_form()
	return render (request,'agregar_bodega_material.html',locals())



@staff_member_required(login_url='vista_login')
def editar_bodega_material(request,id_bdm):
	bdm =  Bodega_Material.objects.get(id=id_bdm)
	if request.method == "POST":
		formulario = Bodega_Material_form(request.POST,request.FILES, instance=bdm)
		if formulario.is_valid():
			fic = formulario.save()
			return redirect ('/inicio')
	else:
		formulario = Bodega_Material_form(instance=bdm)
	return render(request,'agregar_bodega_material.html',locals())

@staff_member_required(login_url='vista_login')
def eliminarr_bodega_material(request,id_bdm):
	bdm = Bodega_Material.objects.get(id =id_bdm)
	bdm.delete()
	return redirect('/inicio')
#------------------------------------------------------------------------------------------------------------------
#views de labla aprendiz

@login_required(login_url='vista_login')
def vista_lista_aprendiz(request):
	lista = Aprendiz.objects.filter()
	return render(request,'lista_aprendiz.html',locals())

@staff_member_required(login_url='vista_login')
def vista_agregar_aprendiz(request):
	if request.method=='POST':
		formulario=agregar_aprendiz_form(request.POST,request.FILES)
		if formulario.is_valid():
			Apren=formulario.save(commit=False)
			Apren.status=True
			Apren.save()
			formulario.save_m2m()
			return redirect('/lista_aprendiz/')
	else:
		formulario= agregar_aprendiz_form()
	return render(request,'agregar_aprendiz.html',locals())

@staff_member_required(login_url='vista_login')
def vista_eliminar_aprendiz(request,id_apr):
	apr = Aprendiz.objects.get(id=id_apr)
	apr.delete()
	return redirect('/lista_aprendiz/')

@staff_member_required(login_url='vista_login')
def vista_editar_aprendiz(request,id_apr):
	apr=Aprendiz.objects.get(id=id_apr)
	if request.method=='POST':
		formulario=agregar_aprendiz_form(request.POST,request.FILES,instance=apr)
		if formulario.is_valid():
			apr=formulario.save()
			return redirect('/lista_aprendiz/')
	else:
		formulario=agregar_aprendiz_form(instance=apr)
	return render(request,'agregar_aprendiz.html',locals())

#views de reportes
@staff_member_required(login_url='vista_login')
def vista_reporte(request):
	info=False
	if request.method=='POST':
		busqueda1 = request.POST.get('textfield',None)
		busqueda2 = request.POST.get('textfield1',None)
		p = Prestamo.objects.filter(fecha_prestamo__range=(busqueda1,busqueda2))
		print (p)
		if len(p)>=1:
			info=True
		else:
			pass
	return render(request,'ver_reporte.html',locals())