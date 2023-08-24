from django.db import models
from django.utils.timezone import now


class Employee(models.Model):
    first_name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100, db_index=True)
    surname = models.CharField('Отчество', max_length=100)
    photo = models.ImageField('Фото', upload_to='media/users', blank=True)
    job_title = models.CharField('Должность', max_length=100, blank=True)
    salary = models.DecimalField('Оклад', default=0, max_digits=10, decimal_places=2)
    birthday = models.DateField('День рождения', blank=True, null=True)
    department = models.ForeignKey('department.Department', on_delete=models.CASCADE, related_name='employees',
                                   verbose_name='Департамент')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = 'last_name',
        unique_together = ['id', 'department']

    @property
    def full_name(self) -> str:
        return f'{self.last_name} {self.first_name} {self.surname}'

    @property
    def age(self) -> int:
        if self.birthday:
            age = now().date().year - self.birthday.year
            return age
        return 0

    def __str__(self) -> str:
        return f'{self.full_name}, {self.job_title}'
