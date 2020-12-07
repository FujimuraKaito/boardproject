from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

from .models import BoardModel

# Create your views here.


def signupfunc(request):
    user2 = User.objects.all()  # .allをつけることでQueryになる
    print(user2)
    # requestは指定しなければGETとなる
    # print(request.method) // GET
    if request.method == 'POST':
        # 画面遷移などはここで指定する
        # htmlファイルでusernameというnameタグを指定した
        username2 = request.POST['username']
        password2 = request.POST['password']

        # 重複したユーザーがいないかチェックする
        try:
            # データベースから今入力された名前のデータを取ってくる（あれば重複となる）
            User.objects.get(username=username2)
            return render(request, 'signup.html', {'error': 'このユーザーは登録されています'})
        except:
            # UserというのはDjangoで初めから用意されているデータベースのテーブル→function based viewのデータベースの活用の仕方
            user = User.objects.create_user(username2, '', password2)
            return render(request, 'signup.html', {'some': 'somedata'})

    # class based viewでのtemplate_nameがrenderでの第2引数のような感じ
    # 第3引数はclass based viewでいうmodelに相当するもの→コンテキストという
    return render(request, 'signup.html', {
        'some': 'some'
    })


def loginfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']

        # authenticateはPOSTで受け取ったユーザーの権限などの情報を取ってくる
        user = authenticate(request, username=username2, password=password2)
        if user is not None:
            login(request, user)
            # renderはただ単にレンダリングするだけなのでURLは前のページと変わらない　
            # redirectはurls.pyで指定したnameからパスを推測しページを遷移する
            return redirect('signup')
        else:
            return redirect('login')
    
    return render(request, 'login.html')


def listfunc(request):
    # BoardModelにあるデータを全て取ってくる
    object_list = BoardModel.objects.all()
    return render(request, 'list.html', {'object_list': object_list})