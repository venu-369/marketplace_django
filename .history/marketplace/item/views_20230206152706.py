from django.shortcuts import render

# Create your views here.

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)