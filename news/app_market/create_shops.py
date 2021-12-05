from app_market.models import Shop, Product, ReportSales


def create_shops():
    a = []
    for i in range(10):
        a.append('Магазин ' + str(i))
    for i in a:
        b = Shop(name=i)
        b.save()
        p = Product(name='Продукт', price=100, number=50)
        s = Shop.objects.get(name=i)
        p.shop = s
        p.save()
        r = ReportSales(created=2021-11-25, number=7)
        f = Product.objects.get(id=p.id)
        r.product = f
        r.save()

