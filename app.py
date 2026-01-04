from flask import Flask, render_template, request
from ultralytics import YOLO
import os
import cv2
from utils.email_alert import send_email


app = Flask(__name__)
model = YOLO('model/accident_yolov8.pt')
UPLOAD_FOLDER = 'static/uploads'


@app.route('/', methods=['GET', 'POST'])
def index():
 result = None
 if request.method == 'POST':
   file = request.files['file']
   path = os.path.join(UPLOAD_FOLDER, file.filename)
   file.save(path)
   results = model(path)
   accident_detected = False


   for r in results:
    for c in r.boxes.cls:
     if int(c) == 0:
      accident_detected = True

   if accident_detected:
    send_email()
    result = 'Accident Detected 🚨 Email Sent'
   else:
    result = 'No Accident Detected'

 return render_template('index.html', result=result)


if __name__ == '__main__':
 app.run(debug=True)