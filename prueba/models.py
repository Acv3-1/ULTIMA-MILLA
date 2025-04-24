from django.db import models

class Usuario(models.Model):
    cc = models.CharField(primary_key=True, max_length=15)
    nombre = models.CharField(max_length=30)
    dir = models.CharField(max_length=20)
    telefono = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre


class Proveedor(models.Model):
    nit = models.CharField(primary_key=True, max_length=20)
    propietario = models.CharField(max_length=50)
    cc = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nit


class Producto(models.Model):
    id_producto = models.CharField(primary_key=True, max_length=20)
    nit = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    valor = models.CharField(max_length=9)
    stock = models.IntegerField()
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    cc = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    desc_red = models.CharField(max_length=255)
    id_pedido = models.IntegerField()

    def __str__(self):
        return f'Cliente {self.cc}'


class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    hora_ped = models.DateTimeField()
    hora_ent = models.DateTimeField()
    observaciones = models.CharField(max_length=100)
    productos = models.ManyToManyField(Producto, through='PedidoProducto')

    def __str__(self):
        return f'Pedido {self.id_pedido}'


class PedidoProducto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)


class Transportista(models.Model):
    cc = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    placa = models.CharField(max_length=6)
    modelo = models.IntegerField()
    marca = models.CharField(max_length=10)
    estado = models.CharField(max_length=255)
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)

    def __str__(self):
        return self.placa


class CEDI(models.Model):
    id_bod = models.IntegerField(primary_key=True)
    coord = models.CharField(max_length=50)
    horario = models.CharField(max_length=50)
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)

    def __str__(self):
        return f'CEDI {self.id_bod}'
