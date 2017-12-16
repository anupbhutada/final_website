# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from forms import RegisterForm

# Create your views here.

def index(request):
	request.session['reg_status'] = 'False'
	return render(request, 'extropy/index.html')

def register(request):
	return redirect('https://docs.google.com/forms/d/e/1FAIpQLSdHy-EsjrSkv56QlXOGOX0dR0JgD7diVc8JmAtqdYgeKRHTLw/viewform?usp=sf_link')
	'''
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid: 
			form_object=form.save()
			request.session['reg_status'] = 'True'
			return render(request,'extropy/index.html')
	else:
		form = RegisterForm()

	return render(request,'extropy/form.html',{'form': form })
	'''
	