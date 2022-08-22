# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from measurement.models import Sensor, Measurement
from measurement.serializers import MeasurementSerializer, SensorSerializer, ShowSensorSerializer


class SensGetPost(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensModify(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = ShowSensorSerializer


class MeasurementPost(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer