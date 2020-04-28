from naomi import plugin
from RPi import GPIO

class GoogleAIYVoiceV1Plugin(plugin.VisualizationsPlugin):
    def __init__(self):
        LED = 25
        # GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(25,GPIO.OUT)
        self._pwm=GPIO.PWM(25,100)
        self._pwm.start(0)
        
    @classmethod
    def mic_volume(self, *args, **kwargs):
        try:
            recording = kwargs['recording']
            snr = kwargs['snr']
            minsnr = kwargs['minsnr']
            maxsnr = kwargs['maxsnr']
        except KeyError:
            return
        if(recording):
            self._pwm.ChangeDutyCycle(100)
        else:
            snrrange = maxsnr - minsnr
            if snrrange == 0:
                snrrange = 1  # to avoid divide by zero below
            self._pwm.ChangeDutyCycle((snr-minsnr) / snrrange)

