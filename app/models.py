from django.core.validators import MaxLengthValidator, MinLengthValidator, RegexValidator
from django.db import models

from adminsortable.models import SortableMixin
from ax3_model_extras.fields import OptimizedImageField
from ax3_model_extras.storages import get_upload_path


class HomeBanner(models.Model):
    title = models.CharField(max_length=60, verbose_name='título')

    summary = models.TextField(blank=True, verbose_name='descripción')

    url = models.URLField(verbose_name='url')

    is_external = models.BooleanField(verbose_name='link externo')

    image = OptimizedImageField(
        optimized_image_output_size=(1920, 1080),
        optimized_image_resize_method='thumbnail',
        optimized_file_formats=['JPEG'],
        optimized_image_quality=90,
        upload_to=get_upload_path,
        verbose_name='imagen',
        help_text='JPG 1920x1080px. Max 300Kb.',
    )

    is_active = models.BooleanField(verbose_name='activo')

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='fecha de creación',
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
        verbose_name = 'banner home'
        verbose_name_plural = 'banners home'


class Contact(models.Model):
    name = models.CharField(max_length=240, verbose_name='nombre completo')

    email = models.EmailField(
        verbose_name='correo electrónico',
        help_text='Máximo 100 caracteres',
        max_length=100,
    )

    mobile_number = models.CharField(
        max_length=10,
        unique=True,
        verbose_name='Teléfono celular',
        validators=[
            RegexValidator(r'^[0-9]*$', message='Ingresa solo números'),
            MinLengthValidator(9, message='Asegurate que tenga al menos 9 caracteres'),
        ],
    )

    message = models.TextField(
        verbose_name='mensaje',
        validators=[MinLengthValidator(20), MaxLengthValidator(500)],
    )

    created_at = models.DateTimeField(auto_now=True, verbose_name='fecha de creación')

    def __str__(self):
        return '{} - {}'.format(self.email, self.mobile_number)

    class Meta:
        ordering = ['-id']
        verbose_name = 'contacto / cotización'


class Newsletter(models.Model):
    name = models.CharField(max_length=240, verbose_name='nombre completo')

    email = models.EmailField(unique=True, verbose_name='correo electrónico')

    created_at = models.DateTimeField(auto_now=True, verbose_name='fecha de creación')

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'news letter'


class InstagramPublication(models.Model):
    title = models.CharField(max_length=60, verbose_name='título')

    image = OptimizedImageField(
        optimized_image_output_size=(737, 516),
        optimized_image_resize_method='thumbnail',
        optimized_file_formats=['JPEG'],
        optimized_image_quality=90,
        upload_to=get_upload_path,
        verbose_name='imagen',
        help_text='JPG 737x516px. Max 150Kb.',
    )

    url = models.URLField(verbose_name='link')

    created_at = models.DateTimeField(auto_now=True, verbose_name='fecha de creación')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'publicación en instagram'
        verbose_name_plural = 'publicaciones en instagram'
