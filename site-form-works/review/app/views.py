from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views import View

from .models import Product, Review
from .forms import ReviewForm


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()

    context = {
        'product_list': products,
    }

    return render(request, template, context)

class product_view_new(View):
    template = 'app/product_detail.html'

    def get(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        form = ReviewForm()
        reviewed = self.is_reviewed(request, pk)
        return self.render(request, form, product, reviewed)

    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        form = ReviewForm(request.POST)
        reviewed = self.is_reviewed(request, pk)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            user_id = request.session.session_key if request.session.session_key is not None else 'guest'
            review.text = f'{user_id}: {review.text}'

            if not reviewed:
                session_reviews = request.session.get('reviews', list())
                session_reviews.append(pk)
                request.session['reviews'] = session_reviews
                review.save()
                return redirect('product_detail', pk=pk)
            else:
                form.errors['text'] = ['Вы уже оставляли отзыв!']

        return self.render(request, form, product, reviewed)


    def is_reviewed(self, request, pk):
        return 'reviews' in request.session and pk in request.session['reviews']


    def render(self, request, form, product, reviewed):
        context = {
            'form': form,
            'product': product,
            'reviews': product.reviews.all(),
            'reviewed': reviewed
        }

        return render(request, self.template, context)

def product_view(request : WSGIRequest, pk):
    template = 'app/product_detail.html'
    product = get_object_or_404(Product, id=pk)
    reviews = product.reviews.all()
    form = None

    session_reviews = request.session.get('reviews', list())
    reviewed = pk in session_reviews

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            user_id = request.session.session_key if request.session.session_key is not None else 'guest'
            review.text = f'{user_id}: {review.text}'

            if not reviewed:
                session_reviews.append(pk)
                request.session['reviews'] = session_reviews
                review.save()
                return redirect('product_detail', pk=pk)
            else:
                form.errors['text'] = ['Вы уже оставляли отзыв!']
    else:
        form = ReviewForm

    context = {
        'form': form,
        'product': product,
        'reviews': reviews,
        'reviewed': reviewed
    }

    return render(request, template, context)