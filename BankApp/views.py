from django.shortcuts import render,redirect
from BankApp.models import Bank
from BankApp.forms import BankForm
 
def display(request):
    b=Bank.objects.all()
    print(b)
    d={'bank':b}
    return render(request,'BankApp/bank_list.html',d)
def detail_view(request,id):
    b=Bank.objects.get(id=id)
    print(b)
    d={'b':b}
    print(d)
    return render(request,'BankApp/bank_details.html',d)
def create_view(request):
    f=BankForm()
    if request.method=='POST':
        f=BankForm(request.POST)
        if f.is_valid():
            f.save(commit=True)
        return redirect('/list')
    return render(request,'BankApp/bank_form.html',{'form':f})
def update_view(request,id):
    b=Bank.objects.get(id=id)
    if request.method=="POST":
        f=BankForm(request.POST,instance=b)
        if f.is_valid():
            f.save(commit=True)
        return redirect('/list')
    return render(request,'BankApp/bank_update.html',{'bank':b})
def delete_view(request,id):
    b=Bank.objects.get(id=id)
    b.delete()
    return redirect('/list')