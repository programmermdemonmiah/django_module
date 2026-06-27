from django.shortcuts import render


def djangoModule(request):
    return render( request, 'index.html')


def moduleWithExample(request):
    return render( request, 'module-with-example.html')