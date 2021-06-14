from .models import Order

def get_or_create_order(cart, request):
    order = cart.order
    if order is None and request.user.is_authenticated:
        order = Order.objects.create(cart=cart, user=request.user)
    if order:
        request.session['order_id'] = order.id
    return order