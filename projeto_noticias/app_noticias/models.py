from django.db import models
from django.contrib.auth.models import User, Permission

class Categoria(models.Model):
    nome = models.CharField(max_length=200, verbose_name='Nome')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nome


class Status(models.Model):
    nome = models.CharField(max_length=200, verbose_name='Nome')

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Status'

    def __str__(self):
        return self.nome

class Artigo(models.Model):
    titulo = models.CharField(max_length=200, verbose_name='Título')
    resumo = models.CharField(max_length=200, verbose_name='Resumo', null=True, blank=True)
    status = models.ForeignKey(Status, verbose_name='Status', null=True, blank=True, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, verbose_name='Categoria', null=True, blank=True, on_delete=models.CASCADE)
    conteudo = models.CharField(max_length=1000, verbose_name='Conteúdo')
    autor = models.ForeignKey(User, verbose_name='Autor', related_name="autor", on_delete=models.CASCADE)
    revisor = models.ForeignKey(User, verbose_name='Revisor', related_name="revisor", null=True, blank=True, on_delete=models.CASCADE)
    data_publicacao = models.DateField(verbose_name='Data da publicação', null=True, blank=True)
    imagem = models.ImageField(verbose_name='Imagem', upload_to='artigos/', null=True, blank=True)

    class Meta:
        verbose_name = 'Artigo'
        verbose_name_plural = 'Artigos'

    def __str__(self):
        return self.titulo