from ultralytics import YOLO
import cv2
model=YOLO("../yolo_weights/yolov8l.pt")
results = model("/Users/alchemy/Ai_Mark1/pythonProject/Yolo/cars.jpeg",show=True)
cv2.waitKey(0)


