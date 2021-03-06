from django.urls import path
from .views.homepage import homepage
from .views.detail import detail
from .views.cart import cart, addToCart, remove_from_cart
from .views.register import register
from .views.signin import signin
from .views.signout import signout
from .views.category import category
from .views.search import search
from .views.order import order
urlpatterns = [
  path('', homepage, name='homepage'),
  path('detail/<int:pk>', detail, name='detail'),
  path('cart', cart, name='cart'),
  path('register',register,name='register'),
  path('signin', signin, name='signin'),
  path('signout', signout, name='signout'),
  path('addToCart/<int:pk>', addToCart, name='addToCart'),
  path('remove_from_cart/<int:pk>', remove_from_cart, name='remove_from_cart'),
  path('category/<int:pk>', category, name='category'),
  path('search',search, name='search'),
  path('order',order, name='order')


  
] 