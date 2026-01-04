# Accident Detection System using YOLO and Flask

This project is a real-time accident detection system. It uses a YOLO model to analyze video frames and trigger an automated email alert when an accident is detected.

## Features
* **Real-time Detection:** Uses YOLO to identify accidents in images/video.
* **Email Alerts:** Automatically sends an email notification via Flask-Mail.
* **Web Dashboard:** Simple Flask interface to upload images and view results.

## Setup Instructions
1. Install dependencies: `pip install -r requirements.txt`
2. Configure your Gmail App Password in `app.py`.
3. Run the app: `python app.py`

## Technologies Used
* Python
* Flask
* YOLO (You Only Look Once)
* OpenCV
