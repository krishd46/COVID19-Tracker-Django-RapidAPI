from django.shortcuts import render

# Create your views here.

def indexpage(request):
    mylistitems = ['item1','item2','item3']
    context = {'string' : string}
    return render(request, 'index.html',context)
