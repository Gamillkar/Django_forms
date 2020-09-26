from django.shortcuts import redirect, render, get_object_or_404


from .models import Product, Review
from .forms import ReviewForm


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()
    context = {
        'product_list': products,
    }
    return render(request, template, context)


def product_view(request, pk, *args, **kwargs):
    list_pk = []
    template = 'app/product_detail.html'
    products = get_object_or_404(Product, id=pk)
    reviews = Review.objects.filter(product_id=pk)
    is_review_exist = False

    if request.method == 'POST':
        form = ReviewForm(request.POST)

        session = request.session.items()
        if str(session) == 'dict_items([])':
            request.session['reviewed_products'] = list_pk
        for el in session:
            post = el[1]
            if pk not in post and form.is_valid():
                list_pk.append(pk)
                request.session['reviewed_products'] = list_pk
                Review.objects.create(text=form, product_id=pk)
                redirect('app/product_detail')
            else:
                is_review_exist = True

    form = ReviewForm
    context = {
        'form': form,
        'product': products,
        'reviews': reviews,
        'is_review_exist': is_review_exist,
    }

    return render(request, template, context)






