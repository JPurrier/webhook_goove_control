from flask import Flask, request, Response
from key import name, lg
from govee import Control
import json
from datetime import datetime
import time

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        data = json.loads(request.form.to_dict()['payload'])
        now = datetime.now()

        on_time = now.replace(hour=19, minute=0, second=0, microsecond=0)
        end_time = now.replace(hour=2, minute=0, second=0, microsecond=0)

        if now > on_time or now < end_time:
            if data['Player']['title'] == name:
                if data['event'] == "media.play":
                    Control().turn_light_on(lg)
                    time.sleep(3)
                    if now > on_time:
                        Control().set_light_brightness(lg)
                        print('setting default light 80 percent')
                    else:
                        Control().set_light_brightness(lg, 40)
                        print('Reducing light level to 40')
                    time.sleep(3)
                    Control().set_light_colour(lg)
                    print('Turning lights on', '\r\n', data['event'])

                if data['event'] == "media.resume":
                    Control().turn_light_on(lg)
                    time.sleep(3)
                    if now > on_time:
                        Control().set_light_brightness(lg)
                        print('setting default light 80 percent')
                    else:
                        Control().set_light_brightness(lg, 40)
                        print('Reducing light level to 40')
                    time.sleep(3)
                    Control().set_light_colour(lg)
                    print('Turning lights on', '\r\n', data['event'])

        if data['event'] == "media.stop":
            Control().turn_light_off(lg)
            print('Turning lights off', '\r\n', data['event'])

        return Response(status=200)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5978)
