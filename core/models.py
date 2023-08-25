import uuid
from django.db import models
from stdimage.models import StdImageField


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criado = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Modificação', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True


class Bebida(Base):
    TYPE_CHOICE = {
        ('vinho', 'Vinho'),
        ('drink', 'Drink'),
        ('cerveja', 'Cerveja'),
        ('refrigerante', 'Refrigerante'),
        ('suco', 'Suco'),
    }
    nome = models.CharField('Nome', max_length=50)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=5)
    descricao = models.TextField('Descrição', max_length=200)
    img = StdImageField('Imagem', upload_to=get_file_path,
                        variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    tipo = models.CharField('Tipo', max_length=20, choices=TYPE_CHOICE)


class Pìzza(Base):
    TYPE_CHOICE = {
        (0, 'Doce'),
        (1, 'Salgado'),
    }
    nome = models.CharField('Nome', max_length=40)
    ingredientes = models.TextField('Ingredientes', max_length=300)
    broto = models.DecimalField('Preço Broto', max_digits=3, decimal_places=2)
    media = models.DecimalField('Preço Media', max_digits=3, decimal_places=2)
    grande = models.DecimalField('Preço Grande', max_digits=3, decimal_places=2)
    img = StdImageField('Imagem', upload_to=get_file_path,
                        variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    salgado = models.BooleanField('Tipo', choices=TYPE_CHOICE)
