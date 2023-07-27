from django.shortcuts import render

# Create your views here.
def datarender(request):
     d={'name':'linga' ,'age': 23}
     return render(request,'datarender.html', context=d)