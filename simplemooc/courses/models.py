from django.db import models

# Create your models here.
#Models tem as funções para facilitar o manuseio do banco de dados.

class Course(models.Model):
    name = models.CharField('Nome', max_length=100) #Um nome é a nivel de programação e o outro é a nível de usuário
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição', blank=True) #Campo não obrigatório
    start_date = models.DateField(
        'Data de Início', null=True, blank=True
    )
    image = models.ImageField(upload_to='courses/images',
                              verbose_name='Imagem') #Caminho onde o arquivo será salvo

    created_at = models.DateTimeField('Criado em', auto_now_add=True) #Toda vez que eu criar um curso, automaticamente será a data atual
    updated_at = models.DateTimeField('Atualizado em', auto_now=True) #Toda vez que eu salvar um curso, automaticamente será a data atual