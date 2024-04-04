from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [

    path('', views.BootstrapFilterView,name='bootstrapfilter'),

    path('pyfoo',views.pyfoo,name='pyfoo'),

    path('base',views.base,name='base'),
    path('home',views.home,name='home'),

    path('xproject',views.xproject,name='xproject'),
    path('ec/',views.ec,name='ec'),
    path('cs',views.cs,name='cs'),
    path('me',views.me,name='me'),
    path('ee',views.ee,name='ee'),
    path('tc',views.tc,name='tc'),
    path('mel',views.mel,name='mel'),
    path('other',views.other,name='other'),

    path('about',views.about,name='about'),
    path('services',views.developer,name='developer'),

    path('add_to_card/<user>/<product>/<int:id>',views.add_to_card,name='add_to_card'),
    path('cart_delete/<user>/<product>/<int:id>',views.cart_delete,name='cart_delete'),
    path('cart/<user>',views.cart,name='cart'),
    path('address/<user>/<product>/<int:id>',views.address,name='address'),
    path('buy/<user>/<int:id>',views.buy,name='buy'),
    path('order/<user>',views.order,name='order'),
    path('order_delete/<user>/<product>/<int:id>',views.order_delete,name='order_delete'),

    path('ec_details_show/<int:id>', views.ec_details_show, name='ec_details_show'),
    path('cs_details_show/<int:id>', views.cs_details_show, name='cs_details_show'),
    path('ee_details_show/<int:id>', views.ee_details_show, name='ee_details_show'),
    path('tc_details_show/<int:id>', views.tc_details_show, name='tc_details_show'),
    path('me_details_show/<int:id>', views.me_details_show, name='me_details_show'),
    path('mel_details_show/<int:id>', views.mel_details_show, name='mel_details_show'),
    path('x_details_show/<int:id>', views.x_details_show, name='x_details_show'),
    path('o_details_show/<int:id>', views.o_details_show, name='o_details_show'),

    path('new_reviews/<product>/<int:pid>/<user>/<int:id>', views.new_reviews, name='new_reviews'),
    
    path('profile/<user>', views.profile, name='profile'),
    path('update_profile/<user>', views.update_profile, name='update_profile'),

    path('account_delete/<user>', views.account_delete, name='account_delete'),
    
    path('chatbox',views.chatbox,name='chatbox'),
    path('help',views.help,name='help'),
    path('maps',views.maps,name='maps'),
    
    path('logout',views.logout,name='logout')
]