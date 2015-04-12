from django.core.serializers.python import Serializer

class ProductSerializer(Serializer):
    '''
    Convert django model instance to a simple dict
    '''

    def get_dump_object(self, obj):
        self._current['pk'] = obj.pk
        self._current['price'] = float(obj.price)
        self._current['price_old'] = float(obj.price_old)
        self._current['permanent_id'] = obj.permanent_id
        del self._current['_permanent_id']
        return self._current
