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


class Categoria(Base):
    tipo = models.CharField('Tipo', max_length=50)


class Produto(Base):
    nome = models.CharField('Nome', max_length=50)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=5)
    descricao = models.TextField('Descrição', max_length=200)
    img = StdImageField('Imagem', upload_to=get_file_path,
                        variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Combo(Base):
    nome = models.CharField('Nome', max_length=100)
    pizza = models.ManyToManyField(Produto)
    img = StdImageField('Imagem', upload_to=get_file_path,
                        variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    total = models.DecimalField('Preço', decimal_places=2, max_digits=5)

