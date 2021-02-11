from django.urls import path

from . import views


urlpatterns = [
    # path('<int:id>', views.detail, name="detail"),
    # path('rooms', views.rooms_list, name="rooms"),
    path('list', views.list, name="list"),
    # path('edit/<int:id>', views.edit, name="edit"),
    # path('delete/<int:id>', views.delete, name="delete")
]
