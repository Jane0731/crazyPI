from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from .models import temperature_humidity

class htResource(ModelResource):

    class Meta:
        queryset = temperature_humidity.objects.all()
        resource_name = 'ht'
        fields = ['temperature', 'humidity']
        authorization = Authorization()
        
   
    def get_object_list(self, request):
        return super(htResource,self).get_object_list(request).filter()


ht_resource = htResource()  #建立API資源