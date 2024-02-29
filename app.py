import cv2
from matplotlib import pyplot as plt
from pathlib import Path
import sys
import torch

from pathlib import Path

# Model
# Load your custom YOLOv5 model
model_path = Path(r'E:\project\brain\bone.pt')
model = torch.hub.load(r'E:\project\brain\yolov5', 'custom', path=model_path, source='local', force_reload=True)

# Model
# model = torch.hub.load('yolov5', r'E:\project\brain\bone.pt')
# model1 = torch.hub.load(r'E:\project\brain\yolov5' , 'custom', source ='local', path=r'E:\project\brain\bone.pt',force_reload=True)
# model = torch.hub.load(r'E:\project\brain\yolov5', 'custom', source ='local', path='bone.pt',force_reload=True)
 
 
# cap = cv2.VideoCapture(0)
 
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
 
#     results = model(frame)
#     # Get the incidents and store to db
#     for result in results.xyxy[0]:
#         x1, y1, x2, y2, conf, cls = result
#         cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
#         cv2.putText(frame, f'{model.names[int(cls)]} {conf:.2f}', (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
       
#     cv2.imshow('Frame', frame)
#     cv2.waitKey(1)