from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306165774',
        'name': 'Jasmine Rakhaila',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)