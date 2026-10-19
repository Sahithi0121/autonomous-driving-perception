from ultralytics import YOLO
print("Loading YOLO model...")
model = YOLO("yolo26n.pt")
print("Processing video...")
results = model.predict(
    source="data/videos/road_traffic.mp4",
    save=True,
    project="outputs",
    name="video_detection",
    show=False
)
print("Video detection completed!")
print("Open outputs/video_detection to see the result.")
