from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import fPayment, fProfileInfo, fItems

def Mainpage(request):
	return render(request,'mainpage.html')
def transactiondetails(request):
	if request.method == "POST":
		ddate = request.POST['ddate']
		pay = request.POST['pay']
		tdate = request.POST['tdate']
		item = Payment.objects.create(TDate = tdate,
		Pay = pay,
		DDate= ddate,)
		item.save()
	aProfileInfo = ProfileInfo.objects.all()
	aItems = Items.objects.all()
	aPayment = Payment.objects.all()
	return render (request, 'Model4.html', {'ProfileInfo':aProfileInfo, 'Items':aItems, 'Payment':aPayment})
def product(request):
	if request.method == "POST":
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		address = request.POST['address']
		contact_number = request.POST['contact_number']
		notes = request.POST['notes']
		item = ProfileInfo.objects.create(First_name = first_name,
		Last_name = last_name,
		Email= email,
		Address = address,
		Contact_number = contact_number,
		Notes = notes,)
		item.save()
	return render (request, 'Model2.html')

def modeofpayment(request):
	if request.method == "POST":
		product = request.POST['product']
		qua = request.POST['qua']
		size = request.POST['size']
	
		item = Items.objects.create(Product = product,
		QuaPrice = qua,
		Sizes= size,)
		item.save()
	return render (request, 'Model3.html')

def edit(request, id):
	info = ProfileInfo.objects.get(id=id)
	form = fProfileInfo(instance=info)
	if request.method == 'POST':
		form = fProfileInfo(request.POST, instance = info)
		if form.is_valid():
			form.save()
			return redirect('/transactiondetails')

	return render(request, 'edit.html', {'form':form})
		
def cancel(request, id):
    q = ProfileInfo.objects.get(id=id)
    for x in ProfileInfo.objects.only('id'):
        if q == x:
            x = ProfileInfo.objects.get(id=id).delete()
            break
    return redirect('/transactiondetails')
def edita(request, id):
	info = Items.objects.get(id=id)
	form = fItems(instance=info)
	if request.method == 'POST':
		form = fItems(request.POST, instance = info)
		if form.is_valid():
			form.save()
			return redirect('/transactiondetails')

	return render(request, 'edita.html', {'form':form})
		
def cancela(request, id):
    q = Items.objects.get(id=id)
    for x in Items.objects.only('id'):
        if q == x:
            x = Items.objects.get(id=id).delete()
            break
    return redirect('/transactiondetails')

def editb(request, id):
	info = Payment.objects.get(id=id)
	form = fPayment(instance=info)
	if request.method == 'POST':
		form = fPayment(request.POST, instance = info)
		if form.is_valid():
			form.save()
			return redirect('/transactiondetails')

	return render(request, 'editb.html', {'form':form})
		
def cancelb(request, id):
    q = Payment.objects.get(id=id)
    for x in Payment.objects.only('id'):
        if q == x:
            x = Payment.objects.get(id=id).delete()
            break
    return redirect('/transactiondetails')




