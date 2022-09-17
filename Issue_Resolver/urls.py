from django.contrib import admin
from django.urls import path
from .views import home,login,register,addissues,myissues,resolverlogin,employeeregister
 


urlpatterns = [
    path('', home.Index.as_view(),name='homepage'),
    path('login',login.Login.as_view(),name='login'),
    path('register',register.Register.as_view(),name='register'),
    path('addissues',addissues.Addissues.as_view(),name='addissues'),
    path('logout/',login.logout,name='logout'),
    path('myissues', myissues.Myissues.as_view() ,name='myissues'),
    path('resolverlogin', resolverlogin.Resolverlogin.as_view() ,name='resolverlogin'),
    path('employeeregister', employeeregister.Employeeregister.as_view() ,name='employeeregister'),


    # path('cart',cart.Cart.as_view(),name='cart'),
    # path('check_out',auth_middleware(check_out.CheckOut.as_view()),name='check_out'),
    # path('orders',auth_middleware(orders.OrderView.as_view()),name='orders'),
    # path('seller',seller.Seller.as_view(),name='seller'),

    
]
