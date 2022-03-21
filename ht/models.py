'''
Author: your name
Date: 2022-03-17 17:47:58
LastEditTime: 2022-03-21 10:22:57
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \crazyPI\ht\models.py
'''
from django.db import models

class temperature_humidity(models.Model):

    id = models.AutoField(primary_key=True)
    temperature = models.CharField(max_length=50, verbose_name='溫度', blank=True)
    humidity = models.CharField(max_length=50, verbose_name='濕度', blank=True)
    create_date = models.CharField(max_length=50,verbose_name='創建日期', blank=True, null=True) 

    class Meta:
        ordering = ('id',)
        verbose_name = '溫度濕度'
        verbose_name_plural = '溫度濕度'

    def __str__(self):
        return self.temperature

