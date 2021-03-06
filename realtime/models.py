from django.db import models

# Create your models here.


class motorstate(models.Model):
    msg_id = models.AutoField(primary_key=True)
    time = models.DateTimeField()
    busCurrent = models.FloatField()
    busVoltage = models.FloatField()
    vehicleVelocity = models.FloatField()
    motorVelocity = models.FloatField()
    phaseACurrent = models.FloatField()
    phaseBCurrent = models.FloatField()
    vectVoltReal = models.FloatField()
    vectVoltImag = models.FloatField()
    vectCurrReal = models.FloatField()
    vectCurrImag = models.FloatField()
    backEMFReal = models.FloatField()
    backEMFImag = models.FloatField()
    fifteenVsupply = models.FloatField()
    onesixfiveVsupply = models.FloatField()
    twofiveVsupply = models.FloatField()
    onetwoVsupply = models.FloatField()
    fanSpeed = models.FloatField()
    fanDrive = models.FloatField()
    heatSinkTemp = models.FloatField()
    motorTemp = models.FloatField()
    airInletTemp = models.FloatField()
    processorTemp = models.FloatField()
    airOutletTemp = models.FloatField()
    capacitorTemp = models.FloatField()
    DCBusAmpHours = models.FloatField()
    Odometer = models.FloatField()

    class Meta:
        db_table = "motorstate"
        managed = False
        get_latest_by = 'msg_id'


class controlstate(models.Model):

    id = models.AutoField(primary_key=True)
    time = models.DateTimeField()
    setBusCurrent = models.FloatField()
    setMotorCurrent = models.FloatField()
    setMotorVelocity = models.FloatField()

    class Meta:
        db_table = "controls"
        managed = False
        get_latest_by = 'id'
