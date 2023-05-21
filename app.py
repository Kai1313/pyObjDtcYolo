from flask import Flask, render_template, request, jsonify
from objectdetect import perform_object_detection
from objectdetectv2 import perform_object_detection

app = Flask(__name__, static_folder='templates/')

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Check if a file was uploaded
    if 'image' not in request.files:
        return 'No image uploaded'
    
    # Get the uploaded image file
    image_file = request.files['image']

    # Save the image to a temporary location
    image_path = 'templates/uploaded_image.jpg'
    image_file.save(image_path)

    # Call the object detection function
    # detection_results = perform_object_detection(image_path)
    # object_count, labels = perform_object_detection(image_path)
    label_counts = perform_object_detection(image_path)

    # Process the detection results or return them as a response
    # return detection_results
    # return render_template('result.html', detection_results=detection_results, image_path=image_path)
    # return render_template('result.html', object_count=object_count, labels=labels, image_path=image_path)
    return render_template('result.html', label_counts=label_counts, image_path=image_path)

@app.route('/uploadv2', methods=['POST'])
def uploadv2():
    # Check if an image was uploaded
    if 'image' not in request.files:
        response_data = {
            "result": False,
            "message": "No image uploaded",
            "label_counts": None,
            "labeled_image_path": None
        }
        return jsonify(response_data)
        # return 'No image uploaded'

    # Get the uploaded image file
    image_file = request.files['image']

    # Save the image to a temporary location
    image_path = 'templates/uploaded_image.jpg'
    image_file.save(image_path)

    # Call the object detection function
    label_counts, labeled_image_path = perform_object_detection(image_path)

    # Render the result template with the label counts and path to the labeled image
    response_data = {
        "result": True,
        "message": "Successfully detect",
        "label_counts": label_counts,
        "labeled_image_path": labeled_image_path
    }
    return jsonify(response_data)
    # return render_template('resultv2.html', label_counts=label_counts, labeled_image_path=labeled_image_path)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)