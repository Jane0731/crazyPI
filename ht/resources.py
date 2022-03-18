from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from .models import temperature_humidity

class htResource(ModelResource):

    class Meta:
        queryset = temperature_humidity.objects.filter().order_by('-id')
        resource_name = 'ht'
        limit = 5
        fields = ['temperature', 'humidity', 'create_date']
        authorization = Authorization()

ht_resource = htResource()  #建立API資源