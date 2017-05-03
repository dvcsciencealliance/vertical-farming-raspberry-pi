import web
#import RPI.GPIO as GPIO

on = False

urls = (
    '/', 'index'
    )

class index:

    def GET(self):
        global on
        on = not on
        #GPIO.output(16, GPIO.LOW if on else GPIO.HIGH)
        return ("On" if on else "Off")

if __name__ == "__main__":
    #GPIO.setmode(GPIO.BCM)
    #GPIO.setup(16, GPIO.OUT)
    app = web.application(urls, globals())
    app.run()
