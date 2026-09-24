from django.db import models

# Create your models here.

from django.db import models

# Create your models here.


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

class Estudiante(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=20, unique=True)
    carrera = models.CharField(max_length=100)

class Instructor(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=100)

class Administrador(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)

class Rol(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField()

class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)

class Modulo(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class Leccion(models.Model):
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class Material(models.Model):
    leccion = models.ForeignKey(Leccion, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50)  # e.g., 'video', 'documento', 'enlace'
    url = models.URLField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default='activo')

class ProgresoLeccion(models.Model):
    inscripcion = models.ForeignKey(Inscripcion, on_delete=models.CASCADE)
    leccion = models.ForeignKey(Leccion, on_delete=models.CASCADE)
    completado = models.BooleanField(default=False)
    fecha_completado = models.DateTimeField(null=True, blank=True)

class HistorialEstadoInscripcion(models.Model):
    inscripcion = models.ForeignKey(Inscripcion, on_delete=models.CASCADE)
    estado_anterior = models.CharField(max_length=20, choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')])
    estado_nuevo = models.CharField(max_length=20, choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')])
    fecha_cambio = models.DateTimeField(auto_now_add=True)

class Evaluacion(models.Model):
    leccion = models.ForeignKey(Leccion, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class EntregaEvaluacion(models.Model):
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='entregas/')
    fecha_entrega = models.DateTimeField(auto_now_add=True)
    calificacion = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    retroalimentacion = models.TextField(null=True, blank=True)

