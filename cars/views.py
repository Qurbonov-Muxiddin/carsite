from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from .forms import CarForm, RegisterForm
from .models import Car, Brand


# ---------- Autentifikatsiya (talab 1) ----------

class RegisterView(CreateView):
    """Ro'yxatdan o'tish - muvaffaqiyatli bo'lsa avtomatik login qiladi"""
    form_class = RegisterForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("cars:car_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class UserLoginView(LoginView):
    template_name = "registration/login.html"


class UserLogoutView(LogoutView):
    next_page = reverse_lazy("cars:car_list")


# ---------- CRUD (talab 3, 4, 5, 6) - barchasi Class Based View ----------

from .models import Car, Brand

class CarListView(ListView):
    model = Car
    template_name = "cars/car_list.html"
    context_object_name = "cars"
    paginate_by = 9

    def get_queryset(self):
        queryset = Car.objects.select_related("brand").filter(isActive=True)

        query = self.request.GET.get("q")
        brand = self.request.GET.get("brand")
        min_price = self.request.GET.get("min_price")
        max_price = self.request.GET.get("max_price")

        if query:
            queryset = queryset.filter(name__icontains=query)

        if brand:
            queryset = queryset.filter(brand_id=brand)

        if min_price:
            queryset = queryset.filter(price__gte=min_price)

        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["brands"] = Brand.objects.all()

        context["query"] = self.request.GET.get("q", "")
        context["selected_brand"] = self.request.GET.get("brand", "")
        context["min_price"] = self.request.GET.get("min_price", "")
        context["max_price"] = self.request.GET.get("max_price", "")

        return context

def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    context["query"] = self.request.GET.get("q", "")
    context["brands"] = Brand.objects.all()
    context["selected_brand"] = self.request.GET.get("brand", "")
    context["min_price"] = self.request.GET.get("min_price", "")
    context["max_price"] = self.request.GET.get("max_price", "")
    context["total_cars"] = Car.objects.count()
    return context


class CarDetailView(DetailView):
    """Har bir mashinaning alohida sahifasi (talab 5)"""
    model = Car
    template_name = "cars/car_detail.html"
    context_object_name = "car"


class CarCreateView(LoginRequiredMixin, CreateView):
    model = Car
    form_class = CarForm
    template_name = "cars/car_form.html"
    login_url = reverse_lazy("cars:login")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Yangi mashina qo'shish"
        return context


class CarUpdateView(LoginRequiredMixin, UpdateView):
    model = Car
    form_class = CarForm
    template_name = "cars/car_form.html"
    login_url = reverse_lazy("cars:login")

    def get_queryset(self):
        return Car.objects.filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Mashinani tahrirlash"
        return context
    
class CarDeleteView(LoginRequiredMixin, DeleteView):
    model = Car
    template_name = "cars/car_confirm_delete.html"
    success_url = reverse_lazy("cars:car_list")
    login_url = reverse_lazy("cars:login")

    def get_queryset(self):
        return Car.objects.filter(owner=self.request.user)




