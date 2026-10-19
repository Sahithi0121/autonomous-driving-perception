# Autonomous Driving Perception Stack

## Project Overview

This project implements a basic autonomous-driving perception pipeline using computer vision and deep learning. It processes road traffic video to detect objects, identify possible lane markings, and track detected objects across video frames.

## Features

- **Object Detection:** Uses YOLO to detect objects in road traffic video.
- **Lane Detection:** Uses OpenCV, Canny edge detection, a region-of-interest mask, and Hough line detection to highlight possible lane markings.
- **Vehicle Tracking:** Uses YOLO tracking with the ByteTrack tracker to follow detected objects across video frames.
- **Video Processing:** Saves processed videos for inspection and demonstration.

## Technologies Used

- Python
- YOLO and Ultralytics
- OpenCV
- NumPy
- ByteTrack
- Visual Studio Code

## Project Structure

```text
autonomous-driving-perception/
├── data/
│   └── videos/
│       └── road_traffic.mp4
├── outputs/
│   └── lane_detection.mp4
├── first_detection.py
├── video_detection.py
├── lane_detection.py
├── vehicle_tracking.py
├── README.md
└── .venv/
```

*Note: YOLO-generated detection and tracking results may be stored under `runs/detect/outputs/`, depending on the Ultralytics configuration.*

## Setup

1. Install Python.
2. Open the project folder in VS Code.
3. Install the required libraries using the project's virtual environment:

```powershell
.\.venv\Scripts\python.exe -m pip install ultralytics opencv-python numpy
```

## How to Run

Run these commands in the VS Code PowerShell terminal from the main project folder.

### 1. Object Detection on an Image

```powershell
.\.venv\Scripts\python.exe first_detection.py
```

### 2. Object Detection on a Video

```powershell
.\.venv\Scripts\python.exe video_detection.py
```

### 3. Lane Detection

```powershell
.\.venv\Scripts\python.exe lane_detection.py
```

The processed lane-detection video is saved as `outputs/lane_detection.mp4`.

### 4. Vehicle Tracking

```powershell
.\.venv\Scripts\python.exe vehicle_tracking.py
```

## Current Limitations

- Lane detection is a basic demonstration and may produce noisy or inaccurate lines.
- Detection and tracking accuracy depend on video quality, lighting, camera angle, and model performance.
- The current implementation is a prototype and is not intended for real-world vehicle control or safety-critical use.

## Future Improvements

- Evaluate object detection performance using precision, recall, and mean Average Precision (mAP).
- Improve lane detection under curves, shadows, and changing light conditions.
- Compare tracking performance using different tracking methods.
- Test the pipeline on additional road-scene datasets such as KITTI or BDD100K.
- Explore integration with a simulator such as CARLA.

## Conclusion

This project demonstrates foundational autonomous-driving perception concepts by combining deep-learning-based object detection, classical computer-vision lane detection, and multi-object tracking on road traffic video.
