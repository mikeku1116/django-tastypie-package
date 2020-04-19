from tastypie.resources import ModelResource
from .models import Music


class MusicResource(ModelResource):
    class Meta:
        queryset = Music.objects.all()
        resource_name = 'music'
        fields = ['name', 'artist']
        allowed_methods = ['get']


music_resource = MusicResource()
