from django.db import models

class temperature_humidity(models.Model):

    id = models.AutoField(primary_key=True)
    temperature = models.CharField(max_length=50, verbose_name='溫度', blank=True)
    humidity = models.CharField(max_length=50, verbose_name='濕度', blank=True)
    create_date = models.DateField(verbose_name='創建日期', blank=True, null=True) 

    class Meta:
        ordering = ('id',)
        verbose_name = '溫度濕度'
        verbose_name_plural = '溫度濕度'
    
    def __str__(self):
        return self.temperature

