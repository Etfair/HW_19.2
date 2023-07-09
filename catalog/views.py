from django.shortcuts import render


def contacts(request):
    if request.method == 'POST':
        # в переменной request хранится информация о методе, который отправлял пользователь
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        # а также передается информация, которую заполнил пользователь
        print(f'{name}, {phone} - {message}')
    return render(request, 'main/contacts.html', )


def home(request):
    return render(request, 'main/home.html')
