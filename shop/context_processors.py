def cart_context(request):
    from shop.models import Cart

    if not request.user.is_authenticated:
        cart = None
    else:
        cart, created = Cart.objects.get_or_create(user=request.user, checked_at__isnull=True)

    return {
        'cart': cart,
    }
