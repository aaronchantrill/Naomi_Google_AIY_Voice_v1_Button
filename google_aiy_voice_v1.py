from naomi import plugin
from RPi import GPIO


class GoogleAIYVoiceV1Plugin(plugin.VisualizationsPlugin):
    def __init__(self, *args, **kwargs):
        super(GoogleAIYVoiceV1Plugin, self).__init__(*args, **kwargs)
        LED = 25
        # Don't issue warnings about the GPIO pin being in use
        # (it is probably left over from the last run).
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(LED, GPIO.OUT)
        self._pwm = GPIO.PWM(LED, 100)
        self._pwm.start(0)

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
            self._pwm.ChangeDutyCycle((snr - minsnr) / snrrange)

