from .forms import CitasForm
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Citas


# Create your views here.
def lista_citas(request):
    qs = Citas.objects.select_related("usuario", "servicio")
    paginator = Paginator(qs, 10)
    citas = paginator.get_page(request.GET.get("page"))
    return render(request, "citas/lista.html", {"citas": citas})


def crear_cita(request):
    if request.method == "POST":
        form = CitasForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("citas:lista")

    else:
        form = CitasForm()

    return render(
        request,
        "citas/formulario.html",
        {"form": form, "titulo": "Nueva cita"},
    )


def editar_cita(request, pk):
    cita = get_object_or_404(Citas, pk=pk)

    if request.method == "POST":
        form = CitasForm(request.POST, instance=cita)

        if form.is_valid():
            form.save()
            return redirect("citas:lista")

    else:
        form = CitasForm(instance=cita)

    return render(
        request, "citas/formulario.html", {"form": form, "titulo": "Editar cita"}
    )


def eliminar_cita(request, pk):
    cita = get_object_or_404(Citas, pk=pk)

    if request.method == "POST":
        cita.delete()
        return redirect("citas:lista")

    return render(request, "citas/confirmar_eliminar.html", {"cita": cita})
