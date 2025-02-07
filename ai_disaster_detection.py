import torch
from yolov5.detect import run
run(weights="disaster_model.pt", source="rtsp://drone_camera_feed", conf=0.5)
