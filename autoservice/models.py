from django.db import models
import uuid

class Types(models.Model):
    types = models.CharField('Kėbulo tipas', max_length=200, help_text='Įveskite automobilio kėbulo tipą (pvz. Hečbekas)')

    def __str__(self):
        return self.types


class Car(models.Model):
    """Modelis reprezentuoja auotomobilį (bet ne kopiją)"""
    modelis = models.CharField('Modelis', max_length=200)
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True)
    summary = models.TextField('Aprašymas', max_length=1000, help_text='Trumpas automobilio aprašymas')
    vin = models.CharField('VIN', max_length=13, help_text='13 Simbolių <a href="https://lt.wikipedia.org/wiki/Automobilio_identifikacinis_kodas">VIN kodas</a>')
    types = models.ManyToManyField(Types, help_text='Išrinkite kėbulo tipą')

    def __str__(self):
        return self.modelis


class CarInstance(models.Model):
    """Modelis, aprašantis konkretaus automobilio kopijos būseną"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unikalus ID automobilio kopijai')
    car = models.ForeignKey('Car', on_delete=models.SET_NULL, null=True)
    due_back = models.DateField('Bus prieinama', null=True, blank=True)

    LOAN_STATUS = (
        ('a', 'Administruojama'),
        ('p', 'Paimta'),
        ('g', 'Galima paimti'),
        ('r', 'Rezervuota'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='a',
        help_text='Statusas',
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} ({self.car.title})'

class Brand(models.Model):
    """Model: gamintojas, šalis."""
    model_name = models.CharField('Gamintojas', max_length=100)
    country = models.CharField('Gamitojo šalis', max_length=100)

    class Meta:
        ordering = ['country', 'model_name']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.country} {self.model_name}'