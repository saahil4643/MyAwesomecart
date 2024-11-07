from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name = "ShopHome"),
    path("about/",views.about,name="About us"),
    path("contact/",views.contact,name="ContactUs"),
    path("tracker/",views.tracker,name="TrackingStatus"),
    path("search/",views.search,name="Search"),
    path("products/<int:myid>",views.products,name="productView"),
    path("checkout/",views.checkout,name="About us"),
    # path('get_data/',views.get_data, name='get_data')
]