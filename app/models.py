from django.db import models


class ClassMates(models.Model):
    name = models.CharField('имя', max_length=50)
    surname = models.CharField('фамилия', max_length=50)
    birthday = models.CharField('день рождения', max_length=70)

    def __str__(self):
        return '{0} {1} {2}'.format(self.name, self.surname, self.birthday)


class Teachers(models.Model):
    name = models.CharField('имя учителя', max_length=50)
    middle_name = models.CharField('отчество', max_length=100)
    description = models.CharField('описание', max_length=200)

    def __str__(self):
        return '{0} {1}'.format(self.name, self.middle_name, self.description)