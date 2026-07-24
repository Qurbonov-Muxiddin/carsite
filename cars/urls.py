from django.urls import path

from . import views

app_name = "cars"

urlpatterns = [
    path("", views.CarListView.as_view(), name="car_list"),
    path("car/<int:pk>/", views.CarDetailView.as_view(), name="car_detail"),
    path("car/create/", views.CarCreateView.as_view(), name="car_create"),
    path("car/<int:pk>/update/", views.CarUpdateView.as_view(), name="car_update"),
    path("car/<int:pk>/delete/", views.CarDeleteView.as_view(), name="car_delete"),

    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.UserLogoutView.as_view(), name="logout"),
]
