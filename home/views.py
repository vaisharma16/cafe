from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def reg(request):

    return render(request,'regform.html')

def preview(request):
    e_name=request.POST.get('fname')
    o_name = request.POST.get('oname')
    print(e_name)
    return render(
        request,
        'preview.html',
        {'e_name': e_name, 'o_name': o_name}
    )
