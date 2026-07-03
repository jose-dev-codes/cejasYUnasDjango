from django import forms
from .models import Citas


class CitasForm(forms.ModelForm):
    error_css_class = "campo-error"

    class Meta:
        model = Citas

        fields = ["usuario", "servicio", "fecha", "hora", "especialista", "estado"]

        widgets = {
            "usuario": forms.Select(attrs={"class": "form-select"}),
            "servicio": forms.Select(attrs={"class": "form-select"}),
            "fecha": forms.DateInput(
                attrs={"type": "date", "class": "form-control"},
                format="%Y-%m-%d",
            ),
            "hora": forms.TimeInput(attrs={"type": "time", "class": "form-control"}),
            "especialista": forms.TextInput(attrs={"class": "form-control"}),
            "estado": forms.Select(attrs={"class": "form-select"}),
        }

        error_messages = {
            "usuario": {"required": "Debes seleccionar un usuario para la cita."},
            "servicio": {"required": "Debes seleccionar un servicio."},
            "fecha": {"required": "Debes indicar la fecha de la cita."},
            "hora": {"required": "Debes indicar la hora de la cita."},
            "especialista": {"required": "Debes escribir el nombre del especialista."},
            "estado": {"required": "Debes seleccionar el estado de la cita."},
        }

    def clean(self):
        cleaned = super().clean()
        especialista = cleaned.get("especialista")
        fecha = cleaned.get("fecha")
        hora = cleaned.get("hora")
        estado = cleaned.get("estado")

        if not self.instance.pk and estado == "cancelada":
            raise forms.ValidationError(
                "No puedes crear una cita directamente con estado Cancelada."
            )

        if especialista and fecha and hora:
            citas_choque = Citas.objects.filter(
                especialista=especialista, fecha=fecha, hora=hora
            ).exclude(estado="cancelada")
            if self.instance.pk:
                citas_choque = citas_choque.exclude(pk=self.instance.pk)
            if citas_choque.exists():
                raise forms.ValidationError(
                    f"{especialista} ya tiene una cita agendada el {fecha} a las {hora}."
                )

        return cleaned
