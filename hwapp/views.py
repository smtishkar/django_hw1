from django.shortcuts import render
from django.http import HttpResponse
import logging
from .models import Customer, Thing, Order

logger = logging.getLogger(__name__)     

def index(request):
    maingpage = """
        <header>
            <a href="">Главная страница</a>
            <a href="">О Компании</a>
        </header>
        <div>
            <h1>Главная страница</h1>
            <h2>Тут вы можете ознакомиться с продукцией нашего магазина который продает котиков:</h2>
            <p>Вот первый котик</p>
            <img src="https://gas-kvas.com/grafic/uploads/posts/2023-09/1695792586_gas-kvas-com-p-kartinki-kotiki-26.jpg" width="400" alt="">
            <p>А вот второй котик</p>
            <img src="https://shutniks.com/wp-content/uploads/2020/03/nyashnye_zhivotnye_20_02075858.jpg" width="400" alt="">
        </div>
        <footer>
            <div>
                <p> Контакты: <a href="cats@mai.ru">cats@mail.ru</a> Но эта ссылка не работает :)</p>
            </div>
        </footer>
        """
    logger.info(f'Страница "Главная" успешно открыта')
    return HttpResponse(maingpage)


def about_company(request):
    about_company_page="""
        <header>
            <a href="">Главная страница</a>
            <a href="">О Компании</a>
        </header>
        <div>
        <h1>Добро пожаловать на страницу о наше компании</h1>
        <p>мы давно занимаемся кошками и любим их</p>
        </div>
        """
    logger.info(f'Страница "О Компании" успешно открыта')
    return HttpResponse(about_company_page)

def customers_view(request):
    customers = Customer.objects.all()
    res_str = '<br>'.join([str(customer) for customer in customers])
    return HttpResponse(res_str)


def things_view(request):
    things = Thing.objects.all()
    res_str = '<br>'.join([str(thing) for thing in things])
    return HttpResponse(res_str)

def orders_view(request):
    orders = Order.objects.all()
    res_str = '<br>'.join([str(order) for order in orders])
    return HttpResponse(res_str)