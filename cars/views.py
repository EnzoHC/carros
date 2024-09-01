from cars.models import Car
from cars.forms import CarModelForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)


class CarListView(ListView):
    model = Car
    template_name = "cars.html"
    context_object_name = "cars"

    def get_queryset(self):
        queryset = super().get_queryset().order_by("model")

        search_model = self.request.GET.get("search_model", "")
        search_brand = self.request.GET.get("search_brand", "")

        print(f"Search Model: {search_model}")
        print(f"Search Brand: {search_brand}")

        if search_model:
            queryset = queryset.filter(model__icontains=search_model)

        if search_brand:
            queryset = queryset.filter(brand__name__icontains=search_brand)

        print(f"Queryset: {queryset}")

        return queryset


class CarDetailView(DetailView):
    model = Car
    template_name = "car_detail.html"


@method_decorator(login_required(login_url="login"), name="dispatch")
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = "new_car.html"
    success_url = reverse_lazy("cars_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        # Adicione um print para verificar se a formatação está correta
        print(f"Form is valid: {form.cleaned_data}")
        return response

    def form_invalid(self, form):
        # Adicione um print para verificar erros de formulário
        print(f"Form is invalid: {form.errors}")
        return super().form_invalid(form)


@method_decorator(login_required(login_url="login"), name="dispatch")
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = "car_update.html"

    ##Função para após editar manter na tela de edição do carro
    def get_success_url(self):
        return reverse_lazy("car_detail", kwargs={"pk": self.object.pk})


@method_decorator(login_required(login_url="login"), name="dispatch")
class CarDeleteView(DeleteView):
    model = Car
    form_clas = CarModelForm
    template_name = "car_delete.html"
    success_url = "/cars/"
