from django.shortcuts import render
from django.template import Template, Context
from django.utils.html import mark_safe
from django.template.loader import get_template, render_to_string
from django.http import HttpResponse

from .models import ProductCategory, Product

def main(request):
    title = 'главная'
    
    products = Product.objects.all()[:4]
        
    content = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', content)


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

