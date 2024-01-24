from django.db import models

# Create your models here.
# Поля модели «Клиент»:
# — имя клиента
# — электронная почта клиента
# — номер телефона клиента
# — адрес клиента
# — дата регистрации клиента

# Поля модели «Товар»:
# — название товара
# — описание товара
# — цена товара
# — количество товара
# — дата добавления товара

# Поля модели «Заказ»:
# — связь с моделью «Клиент», указывает на клиента, сделавшего заказ
# — связь с моделью «Товар», указывает на товары, входящие в заказ
# — общая сумма заказа
# — дата оформления заказа

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    tel = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Customer: {self.name}, email: {self.email}, tel: {self.tel}, address: {self.address}, created_at: {self.created_at}'


class Thing(models.Model):
    thing_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(default=0)
    quantity = models.IntegerField()
    thing_added_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'Thing: {self.thing_name}, description: {self.description}, price: {self.price}, quantity: {self.quantity}, thing_added_date: {self.thing_added_date}'


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    thing = models.ForeignKey(Thing, on_delete=models.CASCADE)
    sum = models.IntegerField(default=0)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'customer: {self.customer}, thing: {self.thing}, sum: {self.sum}, order_date: {self.order_date}'

