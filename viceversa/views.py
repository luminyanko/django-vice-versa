from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def reverse(request):
    message = request.GET['message']
    return render(request, 'reverse.html', {'original_message': message, 'reversed_message': message[::-1]})
