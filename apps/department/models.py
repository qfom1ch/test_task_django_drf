from django.db import models


class Department(models.Model):
    name = models.CharField('Название', max_length=150, unique=True)
    director = models.ForeignKey('employee.Employee',
                                 on_delete=models.DO_NOTHING,
                                 related_name='departament',
                                 null=True, blank=True,
                                 verbose_name='Директор')

    class Meta:
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департаменты'
        ordering = 'name',

    def __str__(self):
        return self.name
