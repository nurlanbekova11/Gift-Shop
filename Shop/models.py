from django.db import models


class Products(models.Model):
    title = models.CharField(max_length=123)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-created_at']

class Application(models.Model):
    name = models.CharField(max_length=123)
    email = models.EmailField()
    phone = models.CharField(max_length=123)
    message = models.TextField(blank = True, null = True)

    def __str__(self):
        return f'Заявка от : {self.name} - {self.email}'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

