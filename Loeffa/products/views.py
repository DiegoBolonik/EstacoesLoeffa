from django.shortcuts import render, redirect
from .models import Locais
from .forms import ProductForm
from tkinter import *


def list_products(request):
    products = Locais.objects.all()
    return render(request, 'products.html', {'products': products})


def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        menu_inicial = Tk()
        menu_inicial.title("Sucesso!")
        menu_inicial.geometry("350x150+400+300")
        label_1 = Label(menu_inicial, text="Seu local de trabalho foi reservado com sucesso!")
        label_1.pack()
        menu_inicial.mainloop()

        return redirect('list_products')

    return render(request, 'products-form.html', {'form': form})


def update_product(request, id):
    product = Locais.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect('list_products')

    return render(request, 'products-form.html', {'form': form, 'product': product})


def delete_product(request, id):
    product = Locais.objects.get(id=id)

    if request.method == 'POST':
        product.delete()
        return redirect('list_products')

    return render(request, 'prod-delete-confirm.html', {'product': product})
