from django.urls import path

from measurement.views import SensGetPost, SensModify, MeasurementPost

urlpatterns = [
    path('sensors/', SensGetPost.as_view()),
    path('sensors/', SensModify.as_view()),
    path('measurements/', MeasurementPost.as_view())
]


