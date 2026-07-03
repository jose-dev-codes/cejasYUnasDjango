from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.
class Usuarios(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    correo = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=255, validators=[MinLengthValidator(6)])
    numero_telefono = models.CharField(
        max_length=15, validators=[MinLengthValidator(10)]
    )
    fecha_nacimiento = models.DateField()

    def clean(self):
        self.correo = self.correo.lower()

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"


class Servicios(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, default="activo")

    def __str__(self):
        return self.nombre


class Citas(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicios, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    especialista = models.CharField(max_length=100)

    ESTADO_CHOICES = [
        ("pendiente", "Pendiente"),
        ("confirmada", "Confirmada"),
        ("cancelada", "Cancelada"),
        ("completado", "Completado"),
    ]

    estado = models.CharField(
        max_length=20, choices=ESTADO_CHOICES, default="pendiente"
    )

    def __str__(self):
        return f"{self.usuario} - {self.servicio} - {self.fecha} {self.hora}"
