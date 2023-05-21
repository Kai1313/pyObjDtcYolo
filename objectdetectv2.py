import torch
import cv2
import numpy as np

def perform_object_detection(image_path):
    # Load the YOLOv5 model
    model = torch.hub.load("ultralytics/yolov5", "yolov5s")

    # Perform object detection on the image
    results = model(image_path)

    # Get the detected objects
    objects = results.pandas().xyxy[0]

    # Count the occurrences for each label
    label_counts = objects['name'].value_counts().reset_index()

    # Rename the columns
    label_counts.columns = ['label', 'count']

    # Convert the label counts to a list of dictionaries
    label_counts_list = label_counts.to_dict('records')

    # Draw labels on the image
    img = cv2.imread(image_path)
    for _, obj in objects.iterrows():
        label = obj['name']
        confidence = obj['confidence']
        x1, y1, x2, y2 = int(obj['xmin']), int(obj['ymin']), int(obj['xmax']), int(obj['ymax'])
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(img, f'{label} {confidence:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Save the image with labels
    labeled_image_path = 'templates/labeled_image.jpg'
    cv2.imwrite(labeled_image_path, img)

    # Return the label counts and the path to the labeled image
    return label_counts_list, labeled_image_path
