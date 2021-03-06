# -*- coding: utf-8 -*-
from django import forms
from app.analisis_radiograficos.models import *
from django.contrib.admin import widgets
#from app.informacion.choices import *

class AspectosArticularesForm(forms.ModelForm):
	class Meta:
		model = aspectos_articulares

		fields = [
			'fichas',
			'condilo_mand_izq_alto',
			'condilo_mand_izq_ancho',
			'condilo_mand_der_alto',
			'condilo_mand_der_ancho',
			'condilo_mand_simetrico',
			'condilo_mand_aspectos_observados',
			'eminencia_izq',
			'eminencia_der',
			'eminencia_simetrico',
			'eminencia_aspectos_observados',
			'espacio_articular_simetrico',
			'espacio_articular_aspectos_observados',
		]

		labels={
			'fichas': 'Codigo Expediente y Numero de Ficha'	,
			'condilo_mand_izq_alto':'Altura',
			'condilo_mand_izq_ancho':'Ancho',
			'condilo_mand_der_alto':'Altura',
			'condilo_mand_der_ancho':'Ancho',
			'condilo_mand_simetrico':'',
			'condilo_mand_aspectos_observados':'Aspectos Observados',
			'eminencia_izq':'Izquierdo:',
			'eminencia_der':'Derecho:',
			'eminencia_simetrico':'',
			'eminencia_aspectos_observados':'Aspectos Observados',
			'espacio_articular_simetrico':'',
			'espacio_articular_aspectos_observados':'Aspectos Observados',
		}

		widgets={
			'fichas':forms.HiddenInput(attrs={'class':'form-control'}),
			'condilo_mand_izq_alto':forms.NumberInput(attrs={'class':'form-control','min':1}),
			'condilo_mand_izq_ancho':forms.NumberInput(attrs={'class':'form-control','min':1}),
			'condilo_mand_der_alto':forms.NumberInput(attrs={'class':'form-control','min':1}),
			'condilo_mand_der_ancho':forms.NumberInput(attrs={'class':'form-control','min':1}),
			'condilo_mand_simetrico':forms.Select(attrs={'class':'form-control'}),
			'condilo_mand_aspectos_observados':forms.Textarea(attrs={'class':'form-control','rows':4, 'cols':1}),
			'eminencia_izq':forms.NumberInput(attrs={'class':'form-control','min':1}),
			'eminencia_der':forms.NumberInput(attrs={'class':'form-control','min':1}),
			'eminencia_simetrico':forms.Select(attrs={'class':'form-control'}),
			'eminencia_aspectos_observados':forms.Textarea(attrs={'class':'form-control','rows':5, 'cols':3,'pattern':'[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð ,.-]{2,250}'}),
			'espacio_articular_simetrico':forms.Select(attrs={'class':'form-control simetrico'}),
			'espacio_articular_aspectos_observados':forms.Textarea(attrs={'class':'form-control','rows':5, 'cols':3}),
		}

class AspectosArticularesForm_consultar(forms.ModelForm):
	class Meta:
		model = aspectos_articulares

		fields = [
			'fichas',
			'condilo_mand_izq_alto',
			'condilo_mand_izq_ancho',
			'condilo_mand_der_alto',
			'condilo_mand_der_ancho',
			'condilo_mand_simetrico',
			'condilo_mand_aspectos_observados',
			'eminencia_izq',
			'eminencia_der',
			'eminencia_simetrico',
			'eminencia_aspectos_observados',
			'espacio_articular_simetrico',
			'espacio_articular_aspectos_observados',
		]

		labels={
			'fichas': 'Codigo Expediente y Numero de Ficha'	,
			'condilo_mand_izq_alto':'Altura',
			'condilo_mand_izq_ancho':'Ancho',
			'condilo_mand_der_alto':'Altura',
			'condilo_mand_der_ancho':'Ancho',
			'condilo_mand_simetrico':'',
			'condilo_mand_aspectos_observados':'Aspectos Observados',
			'eminencia_izq':'Izquierdo:',
			'eminencia_der':'Derecho:',
			'eminencia_simetrico':'',
			'eminencia_aspectos_observados':'Aspectos Observados',
			'espacio_articular_simetrico':'',
			'espacio_articular_aspectos_observados':'Aspectos Observados',
		}

		widgets={
			'fichas':forms.HiddenInput(attrs={'class':'form-control','readonly':True}),
			'condilo_mand_izq_alto':forms.NumberInput(attrs={'class':'form-control','readonly':True,'min':1}),
			'condilo_mand_izq_ancho':forms.NumberInput(attrs={'class':'form-control','readonly':True,'min':1}),
			'condilo_mand_der_alto':forms.NumberInput(attrs={'class':'form-control','readonly':True,'min':1}),
			'condilo_mand_der_ancho':forms.NumberInput(attrs={'class':'form-control','readonly':True,'min':1}),
			'condilo_mand_simetrico':forms.Select(attrs={'class':'form-control','readonly':True,'disabled':True}),
			'condilo_mand_aspectos_observados':forms.Textarea(attrs={'class':'form-control','rows':4, 'cols':1,'readonly':True}),
			'eminencia_izq':forms.NumberInput(attrs={'class':'form-control','readonly':True,'min':1}),
			'eminencia_der':forms.NumberInput(attrs={'class':'form-control','readonly':True,'min':1}),
			'eminencia_simetrico':forms.Select(attrs={'class':'form-control','readonly':True,'disabled':True}),
			'eminencia_aspectos_observados':forms.Textarea(attrs={'class':'form-control','rows':5, 'cols':3,'readonly':True,}),
			'espacio_articular_simetrico':forms.Select(attrs={'class':'form-control simetrico','readonly':True,'disabled':True}),
			'espacio_articular_aspectos_observados':forms.Textarea(attrs={'class':'form-control','rows':5, 'cols':3,'readonly':True}),
		}

class nance_generalForm(forms.ModelForm):
	class Meta:
		model = nance_general

		fields = [
			'fichas',
			'ed_maxi',
			'ed_mand',
		]

		labels={
			'fichas': 'Codigo Expediente y Numero de Ficha'	,
			'ed_maxi':'Espacio Disponible Maxilar M1-6 a M2-6',
			'ed_mand': 'Espacio Disponible Mandibular M4-6 a M3-6',
		}

		widgets={
			'fichas':forms.HiddenInput(attrs={'class':'form-control'}),
			'ed_maxi': forms.NumberInput(attrs={'class':'form-control','min':1}),
			'ed_mand': forms.NumberInput(attrs={'class':'form-control','min':1}),
		}

class nance_generalForm_Consultar(forms.ModelForm):
	class Meta:
		model = nance_general

		fields = [
			'fichas',
			'ed_maxi',
			'ed_mand',
		]

		labels={
			'fichas': 'Codigo Expediente y Numero de Ficha'	,
			'ed_maxi':'Espacio Disponible Maxilar M1-6 a M2-6',
			'ed_mand': 'Espacio Disponible Mandibular M4-6 a M3-6',
		}

		widgets={
			'fichas':forms.HiddenInput(attrs={'class':'form-control','readonly':True}),
			'ed_maxi': forms.NumberInput(attrs={'class':'form-control','readonly':True,'min':1}),
			'ed_mand': forms.NumberInput(attrs={'class':'form-control','readonly':True,'min':1}),
		}

class nance_tabla(forms.ModelForm):
	class Meta:
		model = nance_tablas

		fields = [
			'seleccion',
			'fichas',
			'tabla',
			'posicion',
			'mdm',
			'mprx',
			'mdrx',
			'multiplicacion',
			'valor_x',
		]

		labels={
			'seleccion': ''	,
			'fichas':'',
			'tabla':'',
			'posicion':'',
			'mdm':'',
			'mprx':'',
			'mdrx':'',
			'multiplicacion':'',
			'valor_x':'',
		}

		widgets={
			'seleccion':forms.CheckboxInput(attrs={'class':'checkbox','readonly':True}),
			'fichas':forms.HiddenInput(attrs={'class':'form-control'}),
			'tabla':forms.HiddenInput(attrs={'class':'form-control'}),
			'posicion':forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'mdm':forms.NumberInput(attrs={'class':'form-control','readonly':True,'min':1}),
			'mprx':forms.NumberInput(attrs={'class':'form-control','readonly':True,'min':1}),
			'mdrx':forms.NumberInput(attrs={'class':'form-control','readonly':True,'min':1}),
			'multiplicacion':forms.NumberInput(attrs={'class':'form-control','readonly':True,'min':1}),
			'valor_x':forms.NumberInput(attrs={'class':'form-control x','required':True,'min':1}),
		}

class nance_tabla_consultar(forms.ModelForm):
	class Meta:
		model = nance_tablas

		fields = [
			'seleccion',
			'fichas',
			'tabla',
			'posicion',
			'mdm',
			'mprx',
			'mdrx',
			'multiplicacion',
			'valor_x',
		]

		labels={
			'seleccion': ''	,
			'fichas':'',
			'tabla':'',
			'posicion':'',
			'mdm':'',
			'mprx':'',
			'mdrx':'',
			'multiplicacion':'',
			'valor_x':'',
		}

		widgets={
			'seleccion':forms.CheckboxInput(attrs={'class':'checkbox','disabled':True}),
			'fichas':forms.HiddenInput(attrs={'class':'form-control'}),
			'tabla':forms.HiddenInput(attrs={'class':'form-control'}),
			'posicion':forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'mdm':forms.NumberInput(attrs={'class':'form-control','readonly':True,'min':1}),
			'mprx':forms.NumberInput(attrs={'class':'form-control','readonly':True,'min':1}),
			'mdrx':forms.NumberInput(attrs={'class':'form-control','readonly':True,'min':1}),
			'multiplicacion':forms.NumberInput(attrs={'class':'form-control','readonly':True,'min':1}),
			'valor_x':forms.NumberInput(attrs={'class':'form-control x','readonly':True,'min':1}),
		}

class aspectos_mandibulares2Form(forms.ModelForm):
	class Meta:
		model = aspectos_mandibulares2

		fields = [
			'fichas',
			'aspectos_sinusales_simetrico',
			'aspectos_sinusales_izq_aspect_observ',
			'aspectos_sinusales_der_aspect_observ',
			'ord_ori_simetrico',
			'ord_ori_izq_aspect_observ',
			'ord_ori_der_aspect_observ',
			'fpgd_fpgi_simetrico',
			'fpgd_fpgi_izq_aspect_observ',
			'fpgd_fpgi_der_aspect_observ',
			'veloc_erup_simetrico',
			'veloc_erup_izq_aspect_observ',
			'veloc_erup_der_aspect_observ',
			'diagnostico',
		]

		labels = {
			'fichas': 'Numero de expediente y ficha',
			'aspectos_sinusales_simetrico': 'Aspectos Sinusales',
			'aspectos_sinusales_izq_aspect_observ': 'Izquierdo',
			'aspectos_sinusales_der_aspect_observ': 'Derecho',
			'ord_ori_simetrico': 'Ord-Ori',
			'ord_ori_izq_aspect_observ': 'Izquierdo',
			'ord_ori_der_aspect_observ': 'Derecho',
			'fpgd_fpgi_simetrico': 'Fptgd-Fptgi',
			'fpgd_fpgi_izq_aspect_observ': 'Izquierdo',
			'fpgd_fpgi_der_aspect_observ': 'Derecho',
			'veloc_erup_simetrico': 'Velocidad de Erupcion',
			'veloc_erup_izq_aspect_observ': 'Izquierdo',
			'veloc_erup_der_aspect_observ': 'Derecho',
			'diagnostico': 'Diagnostico',
		}
		widgets = {
			'fichas': forms.HiddenInput(attrs={'class': 'form-control'}),
			'aspectos_sinusales_simetrico': forms.RadioSelect,
			'aspectos_sinusales_izq_aspect_observ': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
			'aspectos_sinusales_der_aspect_observ': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
			'ord_ori_simetrico': forms.RadioSelect,
			'ord_ori_izq_aspect_observ': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
			'ord_ori_der_aspect_observ': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
			'fpgd_fpgi_simetrico': forms.RadioSelect,
			'fpgd_fpgi_izq_aspect_observ': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
			'fpgd_fpgi_der_aspect_observ': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
			'veloc_erup_simetrico': forms.RadioSelect,
			'veloc_erup_izq_aspect_observ': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
			'veloc_erup_der_aspect_observ': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
			'diagnostico': forms.Textarea(attrs={'class': 'form-control', 'max_length': 500}),
		}


class aspectos_mandibulares2Form_consultar(forms.ModelForm):
	class Meta:
		model = aspectos_mandibulares2

		fields = [
			'fichas',
			'aspectos_sinusales_simetrico',
			'aspectos_sinusales_izq_aspect_observ',
			'aspectos_sinusales_der_aspect_observ',
			'ord_ori_simetrico',
			'ord_ori_izq_aspect_observ',
			'ord_ori_der_aspect_observ',
			'fpgd_fpgi_simetrico',
			'fpgd_fpgi_izq_aspect_observ',
			'fpgd_fpgi_der_aspect_observ',
			'veloc_erup_simetrico',
			'veloc_erup_izq_aspect_observ',
			'veloc_erup_der_aspect_observ',
			'diagnostico',
		]

		labels = {
			'fichas': 'Numero de expediente y ficha',
			'aspectos_sinusales_simetrico': 'Aspectos Sinusales',
			'aspectos_sinusales_izq_aspect_observ': 'Izquierdo',
			'aspectos_sinusales_der_aspect_observ': 'Derecho',
			'ord_ori_simetrico': 'Ord-Ori',
			'ord_ori_izq_aspect_observ': 'Izquierdo',
			'ord_ori_der_aspect_observ': 'Derecho',
			'fpgd_fpgi_simetrico': 'Fptgd-Fptgi',
			'fpgd_fpgi_izq_aspect_observ': 'Izquierdo',
			'fpgd_fpgi_der_aspect_observ': 'Derecho',
			'veloc_erup_simetrico': 'Velocidad de Erupcion',
			'veloc_erup_izq_aspect_observ': 'Izquierdo',
			'veloc_erup_der_aspect_observ': 'Derecho',
			'diagnostico': 'Diagnostico',
		}

		widgets = {
			'fichas': forms.HiddenInput(attrs={'class': 'form-control'}),
			'aspectos_sinusales_simetrico': forms.RadioSelect(attrs={'readonly': True, 'disabled': True}),
			'aspectos_sinusales_izq_aspect_observ': forms.Textarea(
				attrs={'class': 'form-control', 'rows': 3, 'readonly': True, 'disabled': True}),
			'aspectos_sinusales_der_aspect_observ': forms.Textarea(
				attrs={'class': 'form-control', 'rows': 3, 'readonly': True, 'disabled': True}),
			'ord_ori_simetrico': forms.RadioSelect(attrs={'readonly': True, 'disabled': True}),
			'ord_ori_izq_aspect_observ': forms.Textarea(
				attrs={'class': 'form-control', 'rows': 3, 'readonly': True, 'disabled': True}),
			'ord_ori_der_aspect_observ': forms.Textarea(
				attrs={'class': 'form-control', 'rows': 3, 'readonly': True, 'disabled': True}),
			'fpgd_fpgi_simetrico': forms.RadioSelect(attrs={'readonly': True, 'disabled': True}),
			'fpgd_fpgi_izq_aspect_observ': forms.Textarea(
				attrs={'class': 'form-control', 'rows': 3, 'readonly': True, 'disabled': True}),
			'fpgd_fpgi_der_aspect_observ': forms.Textarea(
				attrs={'class': 'form-control', 'rows': 3, 'readonly': True, 'disabled': True}),
			'veloc_erup_simetrico': forms.RadioSelect(attrs={'readonly': True, 'disabled': True}),
			'veloc_erup_izq_aspect_observ': forms.Textarea(
				attrs={'class': 'form-control', 'rows': 3, 'readonly': True, 'disabled': True}),
			'veloc_erup_der_aspect_observ': forms.Textarea(
				attrs={'class': 'form-control', 'rows': 3, 'readonly': True, 'disabled': True}),
			'diagnostico': forms.Textarea(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
		}


class estadios_de_nollaForm(forms.ModelForm):
	class Meta:
		model = estadios_de_nolla

		fields = [
			'fichas',
			'e_1_1',
			'e_1_2',
			'e_1_3',
			'e_1_4',
			'e_1_5',
			'e_1_6',
			'e_1_7',
			'e_1_8',
			'e_2_1',
			'e_2_2',
			'e_2_3',
			'e_2_4',
			'e_2_5',
			'e_2_6',
			'e_2_7',
			'e_2_8',
			'e_3_1',
			'e_3_2',
			'e_3_3',
			'e_3_4',
			'e_3_5',
			'e_3_6',
			'e_3_7',
			'e_3_8',
			'e_4_1',
			'e_4_2',
			'e_4_3',
			'e_4_4',
			'e_4_5',
			'e_4_6',
			'e_4_7',
			'e_4_8',
			'otros_hallazgos',
		]

		labels = {

			'fichas': 'Numero de expediente y ficha',
			'e_1_1': '1-1',
			'e_1_2': '1-2',
			'e_1_3': '1-3',
			'e_1_4': '1-4',
			'e_1_5': '1-5',
			'e_1_6': '1-6',
			'e_1_7': '1-7',
			'e_1_8': '1-8',
			'e_2_1': '2-1',
			'e_2_2': '2-2',
			'e_2_3': '2-3',
			'e_2_4': '2-4',
			'e_2_5': '2-5',
			'e_2_6': '2-6',
			'e_2_7': '2-7',
			'e_2_8': '2-8',
			'e_3_1': '3-1',
			'e_3_2': '3-2',
			'e_3_3': '3-3',
			'e_3_4': '3-4',
			'e_3_5': '3-5',
			'e_3_6': '3-6',
			'e_3_7': '3-7',
			'e_3_8': '3-8',
			'e_4_1': '4-1',
			'e_4_2': '4-2',
			'e_4_3': '4-3',
			'e_4_4': '4-4',
			'e_4_5': '4-5',
			'e_4_6': '4-6',
			'e_4_7': '4-7',
			'e_4_8': '4-8',
			'otros_hallazgos': 'Otros Hallazgos En Radiografia Panoramica',

		}

		widgets = {

			'fichas': forms.HiddenInput(attrs={'class': 'form-control'}),
			'e_1_1': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'e_1_2': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'e_1_3': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'e_1_4': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'e_1_5': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'e_1_6': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'e_1_7': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'e_1_8': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'e_2_1': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'e_2_2': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'e_2_3': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'e_2_4': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'e_2_5': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'e_2_6': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'e_2_7': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'e_2_8': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'e_3_1': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'e_3_2': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'e_3_3': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'e_3_4': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'e_3_5': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'e_3_6': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'e_3_7': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'e_3_8': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'e_4_1': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'e_4_2': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'e_4_3': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'e_4_4': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'e_4_5': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'e_4_6': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'e_4_7': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'e_4_8': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'otros_hallazgos': forms.Textarea(attrs={'class': 'form-control', 'max_length': 200}),
		}


class secuencia_y_cronologiaForm(forms.ModelForm):
	class Meta:
		model = secuencia_y_cronologia

		fields = [

			'fichas',
			'o_1_1',
			'o_1_2',
			'o_1_3',
			'o_1_4',
			'o_1_5',
			'o_1_6',
			'o_1_7',
			'o_1_8',
			'o_2_1',
			'o_2_2',
			'o_2_3',
			'o_2_4',
			'o_2_5',
			'o_2_6',
			'o_2_7',
			'o_2_8',
			'o_3_1',
			'o_3_2',
			'o_3_3',
			'o_3_4',
			'o_3_5',
			'o_3_6',
			'o_3_7',
			'o_3_8',
			'o_4_1',
			'o_4_2',
			'o_4_3',
			'o_4_4',
			'o_4_5',
			'o_4_6',
			'o_4_7',
			'o_4_8',
		]

		labels = {

			'fichas': 'Numero de expediente y ficha',
			'o_1_1': '1-1',
			'o_1_2': '1-2',
			'o_1_3': '1-3',
			'o_1_4': '1-4',
			'o_1_5': '1-5',
			'o_1_6': '1-6',
			'o_1_7': '1-7',
			'o_1_8': '1-8',
			'o_2_1': '2-1',
			'o_2_2': '2-2',
			'o_2_3': '2-3',
			'o_2_4': '2-4',
			'o_2_5': '2-5',
			'o_2_6': '2-6',
			'o_2_7': '2-7',
			'o_2_8': '2-8',
			'o_3_1': '3-1',
			'o_3_2': '3-2',
			'o_3_3': '3-3',
			'o_3_4': '3-4',
			'o_3_5': '3-5',
			'o_3_6': '3-6',
			'o_3_7': '3-7',
			'o_3_8': '3-8',
			'o_4_1': '4-1',
			'o_4_2': '4-2',
			'o_4_3': '4-3',
			'o_4_4': '4-4',
			'o_4_5': '4-5',
			'o_4_6': '4-6',
			'o_4_7': '4-7',
			'o_4_8': '4-8',
		}

		widgets = {

			'fichas': forms.HiddenInput(attrs={'class': 'form-control'}),
			'o_1_1': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'o_1_2': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'o_1_3': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'o_1_4': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'o_1_5': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'o_1_6': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'o_1_7': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'o_1_8': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'o_2_1': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'o_2_2': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'o_2_3': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'o_2_4': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'o_2_5': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'o_2_6': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'o_2_7': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'o_2_8': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'o_3_1': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'o_3_2': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'o_3_3': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'o_3_4': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'o_3_5': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'o_3_6': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'o_3_7': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'o_3_8': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'o_4_1': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'o_4_2': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'o_4_3': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'o_4_4': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'o_4_5': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'o_4_6': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'o_4_7': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),
			'o_4_8': forms.NumberInput(attrs={'class': 'form-control', 'max': 10}),

		}


class estadios_de_nollaConsultarForm(forms.ModelForm):
	class Meta:
		model = estadios_de_nolla

		fields = [
			'fichas',
			'e_1_1',
			'e_1_2',
			'e_1_3',
			'e_1_4',
			'e_1_5',
			'e_1_6',
			'e_1_7',
			'e_1_8',
			'e_2_1',
			'e_2_2',
			'e_2_3',
			'e_2_4',
			'e_2_5',
			'e_2_6',
			'e_2_7',
			'e_2_8',
			'e_3_1',
			'e_3_2',
			'e_3_3',
			'e_3_4',
			'e_3_5',
			'e_3_6',
			'e_3_7',
			'e_3_8',
			'e_4_1',
			'e_4_2',
			'e_4_3',
			'e_4_4',
			'e_4_5',
			'e_4_6',
			'e_4_7',
			'e_4_8',
			'otros_hallazgos',
		]

		labels = {

			'fichas': 'Numero de expediente y ficha',
			'e_1_1': '1-1',
			'e_1_2': '1-2',
			'e_1_3': '1-3',
			'e_1_4': '1-4',
			'e_1_5': '1-5',
			'e_1_6': '1-6',
			'e_1_7': '1-7',
			'e_1_8': '1-8',
			'e_2_1': '2-1',
			'e_2_2': '2-2',
			'e_2_3': '2-3',
			'e_2_4': '2-4',
			'e_2_5': '2-5',
			'e_2_6': '2-6',
			'e_2_7': '2-7',
			'e_2_8': '2-8',
			'e_3_1': '3-1',
			'e_3_2': '3-2',
			'e_3_3': '3-3',
			'e_3_4': '3-4',
			'e_3_5': '3-5',
			'e_3_6': '3-6',
			'e_3_7': '3-7',
			'e_3_8': '3-8',
			'e_4_1': '4-1',
			'e_4_2': '4-2',
			'e_4_3': '4-3',
			'e_4_4': '4-4',
			'e_4_5': '4-5',
			'e_4_6': '4-6',
			'e_4_7': '4-7',
			'e_4_8': '4-8',
			'otros_hallazgos': 'Otros Hallazgos En Radiografia Panoramica',

		}

		widgets = {

			'fichas': forms.HiddenInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'e_1_1': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'e_1_2': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'e_1_3': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'e_1_4': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'e_1_5': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'e_1_6': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'e_1_7': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'e_1_8': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'e_2_1': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'e_2_2': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'e_2_3': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'e_2_4': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'e_2_5': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'e_2_6': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'e_2_7': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'e_2_8': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'e_3_1': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'e_3_2': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'e_3_3': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'e_3_4': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'e_3_5': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'e_3_6': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'e_3_7': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'e_3_8': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'e_4_1': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'e_4_2': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'e_4_3': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'e_4_4': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'e_4_5': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'e_4_6': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'e_4_7': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'e_4_8': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'otros_hallazgos': forms.Textarea(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
		}


class secuencia_y_cronologiaConsultarForm(forms.ModelForm):
	class Meta:
		model = secuencia_y_cronologia

		fields = [

			'fichas',
			'o_1_1',
			'o_1_2',
			'o_1_3',
			'o_1_4',
			'o_1_5',
			'o_1_6',
			'o_1_7',
			'o_1_8',
			'o_2_1',
			'o_2_2',
			'o_2_3',
			'o_2_4',
			'o_2_5',
			'o_2_6',
			'o_2_7',
			'o_2_8',
			'o_3_1',
			'o_3_2',
			'o_3_3',
			'o_3_4',
			'o_3_5',
			'o_3_6',
			'o_3_7',
			'o_3_8',
			'o_4_1',
			'o_4_2',
			'o_4_3',
			'o_4_4',
			'o_4_5',
			'o_4_6',
			'o_4_7',
			'o_4_8',
		]

		labels = {

			'fichas': 'Numero de expediente y ficha',
			'o_1_1': '1-1',
			'o_1_2': '1-2',
			'o_1_3': '1-3',
			'o_1_4': '1-4',
			'o_1_5': '1-5',
			'o_1_6': '1-6',
			'o_1_7': '1-7',
			'o_1_8': '1-8',
			'o_2_1': '2-1',
			'o_2_2': '2-2',
			'o_2_3': '2-3',
			'o_2_4': '2-4',
			'o_2_5': '2-5',
			'o_2_6': '2-6',
			'o_2_7': '2-7',
			'o_2_8': '2-8',
			'o_3_1': '3-1',
			'o_3_2': '3-2',
			'o_3_3': '3-3',
			'o_3_4': '3-4',
			'o_3_5': '3-5',
			'o_3_6': '3-6',
			'o_3_7': '3-7',
			'o_3_8': '3-8',
			'o_4_1': '4-1',
			'o_4_2': '4-2',
			'o_4_3': '4-3',
			'o_4_4': '4-4',
			'o_4_5': '4-5',
			'o_4_6': '4-6',
			'o_4_7': '4-7',
			'o_4_8': '4-8',
		}

		widgets = {

			'fichas': forms.HiddenInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'o_1_1': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'o_1_2': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'o_1_3': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'o_1_4': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'o_1_5': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'o_1_6': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'o_1_7': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'o_1_8': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'o_2_1': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'o_2_2': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'o_2_3': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'o_2_4': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'o_2_5': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'o_2_6': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'o_2_7': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'o_2_8': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'o_3_1': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'o_3_2': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'o_3_3': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'o_3_4': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'o_3_5': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'o_3_6': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'o_3_7': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'o_3_8': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'o_4_1': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'o_4_2': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'o_4_3': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'o_4_4': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'o_4_5': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'o_4_6': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'o_4_7': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),
			'o_4_8': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, 'disabled': True}),

		}
