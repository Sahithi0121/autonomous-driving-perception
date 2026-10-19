from ultralytics import YOLO
import os

print("Loading YOLO model...")

model = YOLO("yolo26n.pt")

video_path = "data/videos/road_traffic.mp4"

os.makedirs("outputs", exist_ok=True)

print("Starting vehicle tracking...")

model.track(
    source=video_path,
    tracker="bytetrack.yaml",
    save=True,
    project="outputs",
    name="vehicle_tracking",
    show=True,
    conf=0.3
)

print("Vehicle tracking completed!")
print("Check outputs/vehicle_tracking for the result.")
