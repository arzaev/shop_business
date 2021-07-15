
from .models import Product

class Cart(object):
    def __init__(self, request):
        # request.session['cart'] = []
        self.req = request
        """if we don't have cart session we are creating it"""
        try:
            self.req.session['cart']
        except KeyError:
            self.req.session['cart'] = []

    def add_product(self, product):
        """if we don't have product in our cart we are adding
           if we have we are updating
        """
        list_id = []
        list_products = self.req.session['cart']
        if len(list_products) != 0:
            for pr in list_products:
                list_id.append(int(pr['id_product']))
                if pr['id_product'] == product['id_product']:
                    pr['count_product'] = str(int(pr['count_product']) + int(product['count_product']))
            if int(product['id_product']) not in list_id:
                list_products.append(product)
        else:
            list_products.append(product)
        self.req.session['cart'] = list_products

    def remove_product(self, product):
        list_products = self.req.session['cart']
        tmp_list = []
        for pr in list_products:
            if pr['id_product'] == product['id_product']:
                continue
            else:
                tmp_list.append(pr)
        self.req.session['cart'] = tmp_list

    def update_product(self, product):
        """only update product in cart"""
        print(product)
        tmp_list = []
        list_products = self.req.session['cart']

        for pr in list_products:
            if pr['id_product'] == product['id_product']:
                pr['count_product'] = product['new_count']
            tmp_list.append(pr)
        self.req.session['cart'] = tmp_list


def cart_html(request):
    session_cart = request.session['cart']
    products = []
    gen_price = 0
    for pr in session_cart:
        p = Product.objects.get(id=int(pr['id_product']))
        products.append({'id': p.id, 'name': p.name, 'price': p.price, 'image': p.main_image.url, 'count': pr['count_product'], 'total_price': p.price * int(pr['count_product'])})
        gen_price += p.price * int(pr['count_product'])
    return [products, gen_price]