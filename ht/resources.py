from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from .models import temperature_humidity

class htResource(ModelResource):

    class Meta:
        queryset = temperature_humidity.objects.all()
        resource_name = 'ht'
        fields = ['temperature', 'humidity']
        authorization = Authorization()
    
    def aa(self, bundle):
        qs =  temperature_humidity.objects.raw('SELECT * FROM ht_temperature_humidity')
        return [row for row in qs]

ht_resource = htResource()  #建立API資源