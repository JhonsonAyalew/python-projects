from ultralytics import YOLO
import cv2

# Load YOLOv8 model (pretrained on COCO dataset)
model = YOLO("yolov8n.pt")  # nano = fastest
image = cv2.imread("image.jpg")
results = model(image, conf=0.5)

for r in results:
    for box in r.boxes:
        if int(box.cls[0]) == 0:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(image, (x1, y1), (x2, y2), (0,255,0), 2)

cv2.imshow("Person Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
