from django.shortcuts import render
from django.template import Template, Context
from django.utils.html import mark_safe
from django.template.loader import get_template, render_to_string
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import ProductCategory, Product

def main(request):
    title = 'главная'
    
    products = Product.objects.all()[:4]
        
    content = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    print(pk)

    title = 'Продукты'
    links_menu = ProductCategory.objects.all()
    basket = get_basket(request.user)

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
        }

        return render(request, 'mainapp/products_list.html', content)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)
    
    content = {
        'title': title,
        'links_menu': links_menu, 
        'hot_product': hot_product,
        'same_products': same_products,
        'basket': basket,
    }

    return render(request, 'mainapp/products.html', content)


# Create your views here.
def index(request):
    # CONST = False

    # template = Template('<h1>{{ variable }}</h1>')

    # if CONST:
    #     context_value = {'variable':'Hello'} 
    # else:
    #     context_value = {'variable':'World'}

    # context = Context(context_value)

    # return HttpResponse(
    #     template.render(context)
    # )
    template = get_template('mainapp/index.html')
    context = {'description': 'Главная страница Интернет-витрины'}
    return HttpResponse(
        template.render(context)
    )


def about(request):
    return HttpResponse(
        render_to_string(
            'mainapp/about.html',
            {'description': 'Информационная страница Интернет-витрины'}
        )
    )


def contacts(request):
    return render(
        request, 
        'mainapp/contacts.html',
        {
            'contacts': [
                'Контакт 1','Контакт 2','Контакт 3',
            ]
        }
    )

def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []

        
def get_hot_product():
    products = Product.objects.all()

    return random.sample(list(products), 1)[0]
    
    
def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).\
                                    exclude(pk=hot_product.pk)[:3]

    return same_products

def product(request, pk):
    title = 'продукты'
    
    content = {
        'title': title, 
        'links_menu': ProductCategory.objects.all(), 
        'product': get_object_or_404(Product, pk=pk), 
        'basket': get_basket(request.user),
    }
	
    return render(request, 'mainapp/product.html', content)
