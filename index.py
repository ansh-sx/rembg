from flask import Flask, request, jsonify, send_file
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)

@app.route('/remove-background', methods=['POST'])
def remove_background():
    if 'image' not in request.files:
        return jsonify({"error": "No image part in the request"}), 400

    file = request.files['image']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    try:
        # Open the image and remove the background
        input_image = Image.open(file)

        # Convert image to byte array for background removal
        img_byte_arr = io.BytesIO()
        input_image.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()

        # Remove the background
        output_image_data = remove(img_byte_arr)

        # Return the processed image as a response
        output_image = Image.open(io.BytesIO(output_image_data))
        output_image_io = io.BytesIO()
        output_image.save(output_image_io, 'PNG')
        output_image_io.seek(0)

        return send_file(output_image_io, mimetype='image/png')

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
