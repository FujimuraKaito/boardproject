from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

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
            return redirect('list')
        else:
            return redirect('login')
    
    return render(request, 'login.html')


# デコレータ→この処理を実行する前に実行するもの
# ログインしていなければLOGIN_URLに遷移する（settings.pyで指定）
@login_required  # ログインしているかどうかの確認
def listfunc(request):
    # BoardModelにあるデータを全て取ってくる
    object_list = BoardModel.objects.all()
    return render(request, 'list.html', {'object_list': object_list})


def logoutfunc(request):
    logout(request)
    return redirect('login')


# どの投稿かを判別するためにpkも引数に加える
def detailfunc(request, pk):
    # 引数で受け取ったpkと等しいものをデータベースから取ってくる
    object = BoardModel.objects.get(pk=pk)
    return render(request, 'detail.html', {'object': object})


def goodfunc(request, pk):
    post = BoardModel.objects.get(pk=pk)
    # いいねをインクリメントする
    post.good += 1
    # 更新したオブジェクトを保存する
    post.save()
    return redirect('list')


def readfunc(request, pk):
    post = BoardModel.objects.get(pk=pk)
    # requestオブジェクトの中にログインしているユーザーの情報が入っている
    post2 = request.user.get_username()
    if post2 in post.readtext:
        return redirect('list')
    else:
        post.read += 1
        post.readtext = post.readtext + ' ' + post2
        post.save()
        return redirect('list')