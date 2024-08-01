from ultralytics import YOLO

model = YOLO("yolov10n.pt")

results = model.track(0, save=True, show=True, conf=0.2)