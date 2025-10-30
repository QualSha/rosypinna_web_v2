from django.shortcuts import render

def home(request):
    # Fungsi ini hanya akan merender file 'home.html'
    return render(request, 'beranda.html')