from django.shortcuts import render

# Create your views here.

def bienvenido(request):
    return render(request, 'byteclass/bienvenido.html')

def error_404(request, exception):
    return render(request, 'byteclass/404.html', status=404)


