from ultralytics import YOLO

print("Loading YOLO model...")

model = YOLO("yolo26n.pt")

print("Running object detection...")

results = model.predict(
    source="bus.jpg",
    save=True,
    project="outputs",
    name="first_detection"
)

print("Object detection completed!")
