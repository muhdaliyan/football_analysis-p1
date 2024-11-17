from ultralytics import YOLO

model = YOLO("models/v8-50ep/best.pt")

results = model.predict("input_videos/3.mp4", save=True)
print(results[0])
print("=====================================")
for box in results[0].boxes:
    print(box)
