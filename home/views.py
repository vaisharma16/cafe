from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def reg(request):

    return render(request,'regform.html')

def preview(request):

    return render(
        request,
        'preview.html',
        #{'categories': categories, 'products': products}
    )
