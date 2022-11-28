from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, JsonResponse

# Create your views here.


def index(request):
    return HttpResponse(f'''
    <p>Task_1</p>
    <a href="http://127.0.0.1:8000/post/new_post" >New_post</a><br>
    <a href="http://127.0.0.1:8000/post/popular" >Poost_popular</a><br>
    <a href="http://127.0.0.1:8000/post/all" >All_post</a><br>
    <br<br>
    <p>Task_2</p>
    <a href="http://127.0.0.1:8000/post/comments/12" >get commnets for post this post has 12 id</a><br>
    <a href="http://127.0.0.1:8000/post/like/11" >get likes for post this post has 11 id</a><br>
    
    <br<br>
    <p>Task_3</p>
    <p>Login_user = {request.GET.get('login', 'you dont have login')}, Password_user = {request.GET.get('password', 'you dont have password')}</p>
    <a href='http://127.0.0.1:8000/?login=login&password=1234'>login=login&password=1234</a>
    <br><br>
    <p>Task_4</p>
    <a href='http://127.0.0.1:8000/contacts'>http://127.0.0.1:8000/contacts</a><br>
    <a href='http://127.0.0.1:8000/about'>http://127.0.0.1:8000/about</a>

''')


def popular(requset):
    return HttpResponse('<p>popular posts</p>')


def new_post(requset):
    return HttpResponse('<p>new posts</p>')


def post(requset):
    return HttpResponse('<p>all posts</p>')


def number_post_like(requset, id=10):
    return HttpResponse(f'''
    <p>Post with id {id} has {__import__('random').randint(1, 30)} like</p>
''')


def number_post_comments(requset, id=10):
    return HttpResponse(f'''
        <p>Post with id {id} has {__import__('random').randint(10, 60)} comments</p>
    ''')


def about_first(requset):
    return HttpResponseRedirect('about_second')


def about_second(requset):
    return HttpResponse(f'''
    <p>Временая переадресация на about_second</p>
''')


def contacts_first(request):
    return HttpResponsePermanentRedirect('contacts_second')


def contacts_second(requset):
    return HttpResponse(f'''
    <p>Постояная переадресация на contacts</p>
''')


def pageNotFound(requset, status=404, message='Page loading failed'):
    return HttpResponse(f'''
    <p>Status = {status} Загрузка страницы была завершена ошибкой</p>
''', status=status, reason=message)


def access(requset):
    login = requset.GET.get('login')
    pasword = requset.GET.get('password')
    if login == pasword == 'admin':
        return HttpResponse(f'''
            <p>Успешный вход</p>
''')
    return HttpResponse(f'''
            <p>Не верные данные</p>
''')


def json(requset):
    return JsonResponse(requset.GET)


def set(requset):
    cookie = requset.GET.get('login', 'login')
    re = HttpResponse(f'GET = {cookie}')
    re.set_cookie('cookie', cookie)
    return re


def get(requset):
    return HttpResponse(f"<p>dict = {requset.COOKIES['cookie']}</p>")