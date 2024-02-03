from datetime import timedelta
from django.shortcuts import render
from django.http import HttpResponse
import logging
from .models import Customer, Thing, Order
from datetime import datetime as dt, timedelta
from .forms import AddThingPhoto
from django.shortcuts import render, get_object_or_404, redirect
from django.core.files.storage import FileSystemStorage
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
    about_company_page = """
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
    context = {
        'customers': customers
    }
    return render(request, 'hwapp/customers.html', context=context)


def things_view(request):
    things = Thing.objects.all()
    res_str = '<br>'.join([str(thing) for thing in things])
    return HttpResponse(res_str)


def orders_view(request):
    orders = Order.objects.all()
    res_str = '<br>'.join([str(order) for order in orders])
    return HttpResponse(res_str)


def customer_orders_view(request, customer_id: int, filter_days: int):
    things = []
    user = Customer.objects.filter(pk=customer_id).first()
    date_low_lim = (dt.now() - timedelta(filter_days))
    orders = Order.objects.filter(customer=user).filter(
        order_date__gt=date_low_lim).order_by('order_date')
    context = {
        'user': user,
        'orders': orders,
        'things': things
    }
    for order in orders:
        things.append(order.thing.thing_name)
        print(order.order_date)
        print(things)
        print(order.thing.thing_name)

    return render(request, 'hwapp/customer_orders.html', context=context)


def add_thing_image(request, id_product: int):
    thing = get_object_or_404(Thing, pk=id_product)
    if request.method == "POST":
        form = AddThingPhoto(request.POST, request.FILES)
        if form.is_valid():
            thing.thing_name = request.POST["thing_name"]
            thing.description = request.POST["description"]
            thing.price = request.POST["price"]
            thing.quantity = request.POST["quantity"]
            thing_image = request.FILES["thing_image"]
            fs = FileSystemStorage()
            fs.save(thing_image.name, thing_image)
            thing.thing_image = thing_image.name
            thing.save()
            logger.info(f"Product {thing.thing_name} is changed successfully")
    else:
        form = AddThingPhoto()

    context = {
        "form": form,
    }
    return render(request, "hwapp/add_image.html", context=context)
