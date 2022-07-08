from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Mainpage, name="Mainpage"),
    path('product/',views.product, name="product"),
    path('modeofpayment/',views.modeofpayment, name="modeofpayment"),
    path('transactiondetails/',views.transactiondetails, name="transactiondetails"),
    path('cancel/<int:id>', views.cancel, name='cancel'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('cancela/<int:id>', views.cancela, name='cancela'),
    path('edita/<int:id>', views.edita, name='edita'),
     path('cancelb/<int:id>', views.cancelb, name='cancelb'),
    path('editb/<int:id>', views.editb, name='editb'),
    ]