from django.shortcuts import render, redirect
from django.contrib.auth import login, logout

from .authentication import EmailAuthBackend  # подключаем авторизацию по email


# Create your views here.


# авторизация пользователя по email
def login_in(request):
    if request.method == 'POST':
        # получаем пользователя по его email
        """
        можно ещше сделать поиск по email узера через исключение 
        потом получить имя и авторизовать его будет проще наверное
        """
        email_auth = EmailAuthBackend()
        user = email_auth.authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('index')
            else:
                return render(request, 'account/login.html',
                              {'err': 'Аккаунт отключен!',
                               'username': request.POST['username']
                               })
        else:
            return render(request, 'account/login.html',
                          {'err': 'Не верный логин или пароль!',
                           'username': request.POST['username']
                           })
    return render(request, 'account/login.html')


# выход пользователя и перевод на главную
def logged_out(request):
    logout(request)
    return redirect('index')
