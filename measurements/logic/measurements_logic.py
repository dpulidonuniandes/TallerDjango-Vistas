from ..models import Measurement

def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(meas_pk):
    measurement = Measurement.objects.get(pk=meas_pk)
    return measurement

def update_measurement(meas_pk, new_meas):
    measurement = get_measurement(meas_pk)
    measurement.name = new_meas["variable"]
    measurement.save()
    return measurement

def create_measurement(meas):
    measurement = Measurement(name=meas["variable"])
    measurement.save()
    return measurement