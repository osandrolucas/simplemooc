from django.db import models


class CourseManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) | \
            models.Q(description__icontains=query)  # Feita busca OU na descrição
        )


# Create your models here.
# Models tem as funções para facilitar o manuseio do banco de dados.

class Course(models.Model):
    name = models.CharField('Nome', max_length=100)  # Um nome é a nivel de programação e o outro é a nível de usuário
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição', blank=True)  # Campo não obrigatório - Verbose Name é o nome que aparece nos Forms
    start_date = models.DateField(
        'Data de Início', null=True, blank=True
    )
    image = models.ImageField(upload_to='courses/images', verbose_name='Imagem', null=True,
                              blank=True)  # Caminho onde o arquivo será salvo
    # Blank = True quer dizer que não é um campo obrigatorio.

    created_at = models.DateTimeField('Criado em',
                                      auto_now_add=True)  # Toda vez que eu criar um curso, automaticamente será a data atual
    updated_at = models.DateTimeField('Atualizado em',
                                      auto_now=True)  # Toda vez que eu salvar um curso, automaticamente será a data atual

    objects = CourseManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['name'] #Com o - na frente, vai do menor ao maior.