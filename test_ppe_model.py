"""
Test PPE Model
"""

from ultralytics import YOLO

print("=" * 50)
print("Loading PPE model...")
print("=" * 50)

model = YOLO("models/ppe/best.pt")

print("\nModel loaded successfully.\n")

print("Classes found:\n")

for class_id, class_name in model.names.items():
    print(f"{class_id} -> {class_name}")