from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def signupfunc(request):
    # requestは指定しなければGETとなる
    # print(request.method) // GET
    if request.method == 'POST':
        # 画面遷移などはここで指定する
        # htmlファイルでusernameというnameタグを指定した
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username, '', password)
        return render(request, 'signup.html', {'some': 'somedata'})

    # class based viewでのtemplate_nameがrenderでの第2引数のような感じ
    # 第3引数はclass based viewでいうmodelに相当するもの→コンテキストという
    return render(request, 'signup.html', {
        'some': ''
    })
