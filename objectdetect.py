import torch

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

    # Return the label counts
    return label_counts_list
