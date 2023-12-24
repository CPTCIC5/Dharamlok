from django.db import models

class Broker(models.Model):
    name= models.CharField(max_length=100)
    contact_number=  models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Sauda(models.Model):
    party_name = models.CharField(max_length=50)
    broker_name = models.ForeignKey(Broker, on_delete=models.RESTRICT, help_text='select broker u want to sell')
    image= models.ImageField(upload_to='Data', blank=True, null=True)
    loading = models.CharField(max_length=20)
    brand = models.CharField(max_length=50)
    quantity= models.IntegerField()
    rate = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.party_name

