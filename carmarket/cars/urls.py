from django.urls import path

from . import views


urlpatterns = [
    # path('<int:id>', views.detail, name="detail"),
    # path('rooms', views.rooms_list, name="rooms"),
    path('list', views.list, name="list"),
    path('buy/<int:id>', views.buy, name="buy"),
    # path('delete/<int:id>', views.delete, name="delete")
    path('filter/', views.car_search, name='search'),
]
