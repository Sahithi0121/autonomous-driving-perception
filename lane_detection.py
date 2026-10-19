
import cv2
import numpy as np

print("Starting lane detection...")

video_path = "data/videos/road_traffic.mp4"
cap = cv2.VideoCapture(video_path)

import os

os.makedirs("outputs", exist_ok=True)

fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(
    "outputs/lane_detection.mp4",
    fourcc,
    fps if fps > 0 else 30,
    (width, height)
)


if not cap.isOpened():
    print("Error: Could not open the road video.")
    raise SystemExit

while True:
    ret, frame = cap.read()

    if not ret:
        break

    height, width = frame.shape[:2]

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 50, 150)

    mask = np.zeros_like(edges)
    polygon = np.array([[
        (0, height),
        (int(width * 0.45), int(height * 0.55)),
        (int(width * 0.55), int(height * 0.55)),
        (width, height)
    ]], dtype=np.int32)

    cv2.fillPoly(mask, polygon, 255)
    road_edges = cv2.bitwise_and(edges, mask)

    lines = cv2.HoughLinesP(
        road_edges,
        1,
        np.pi / 180,
        threshold=35,
        minLineLength=30,
        maxLineGap=100
    )

    if lines is not None:
        for line in lines:
            coords = np.asarray(line).reshape(-1)

            if len(coords) >= 4:
                x1, y1, x2, y2 = map(int, coords[:4])
                cv2.line(
                    frame, (x1, y1), (x2, y2),
                    (0, 255, 0), 3
                )

    cv2.imshow("Lane Detection - Press Q to Quit", frame)
    out.write(frame)

    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

print("Lane detection finished!")
