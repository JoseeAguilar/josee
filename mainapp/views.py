from ast import Return
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from audioop import add
from multiprocessing import context
from django.http.response import HttpResponse
from django.shortcuts import redirect, render,HttpResponse
from .models import *
from django.views import generic
from django.contrib import messages

# Create your views here.

def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list' : item_list
    }
    return render(request,'index.html',context)

def add_item(request):
    if request.method=="POST":
        name = request.POST['name']
        description = request.POST['description']
        item = Item(name = name,description = description)
        item.save()
        messages.info(request,"LIBRO AGREGADO CORRECTAMENTE Al CATALAGO")
    else:
        pass
    item_list = Item.objects.all()
    context = {
        'item_list' : item_list
    }
    return render(request,'index.html',context)


def delete_item(request,myid):
    item = Item.objects.get(id = myid)
    item.delete()
    messages.info(request,"LIBRO ELIMINADO CORRECTAMENTE DEL CATALOGO")
    return redirect(index)


def edit_item(request,myid):
    sel_item = Item.objects.get(id = myid)
    item_list = Item.objects.all()
    context = {
        'sel_item':sel_item,
        'item_list': item_list
    }
    return render(request,'index.html',context)
    

def update_item(request,myid):
    item = Item.objects.get(id = myid)
    item.name = request.POST['name']
    item.description = request.POST['description']
    item.save()
    messages.info(request, "LA ACTUALIZACIÓN CORRECTA DEL CATAlAGO DE LRIBOS")
    return redirect('index')

