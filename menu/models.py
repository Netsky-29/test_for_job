from django.db import models
from django.urls import reverse


class BaseAbstractModel(models.Model):
    """
   Базовая абстрактная модель.
   Предоставляет настройки видимости, порядок и созданное/обновленное поле.
    """
    is_visible = models.BooleanField(default=True, verbose_name='Visibility')
    order = models.IntegerField(default=10, verbose_name='Order')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Menu(BaseAbstractModel):
    """
    Модель для пункта меню. Имеет поля title и slug.
    Slug предназначен для отображения меню в шаблоне.
    """
    title = models.CharField(max_length=20, verbose_name='Menu title')
    slug = models.SlugField(max_length=255, verbose_name='Slug', null=True)
    named_url = models.CharField(
        max_length=255,
        verbose_name='Named URL',
        blank=True
    )

    class Meta:
        verbose_name = 'menu'
        verbose_name_plural = 'menu'

    def __str__(self):
        return self.title

    def get_full_path(self):
        if self.named_url:
            url = reverse(self.named_url)
        else:
            url = '/{}/'.format(self.slug)
        return url


class MenuItem(BaseAbstractModel):
    """
   Модель для пункта меню.
    """
    menu = models.ForeignKey(Menu, related_name='items',
                             verbose_name='меню', blank=True, null=True,
                             on_delete=models.CASCADE)
    parent = models.ForeignKey('self', blank=True, null=True,
                               related_name='items',
                               verbose_name='родительский пункт меню',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='название пункта')
    url = models.CharField(max_length=255, verbose_name='ссылка', blank=True)
    named_url = models.CharField(
        max_length=255,
        verbose_name='именованный URL',
        blank=True
    )

    class Meta:
        verbose_name = 'пункт меню'
        verbose_name_plural = 'пункты меню'
        ordering = ('order', )

    def get_url(self):
        if self.named_url:
            url = reverse(self.named_url)
        elif self.url:
            url = self.url
        else:
            url = '/'

        return url

    def __str__(self):
        return self.title
