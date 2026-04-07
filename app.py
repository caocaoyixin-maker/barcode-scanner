from flask import Flask, render_template, request, send_file
import barcode
from barcode.writer import ImageWriter
import os
import cv2
from pyzbar.pyzbar import decode
from PIL import Image
import json


c_data = "/db/customer.json"
p_data = "/db/product.json"

app = Flask(__name__)
BARCODE_FOLDER = "files"

os.makedirs(BARCODE_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template("camera.html")


@app.route('/encode', methods=['POST'])
def encode():
    data = request.form.get('data')

    code128 = barcode.get_barcode_class('code128')
    filename = os.path.join(BARCODE_FOLDER, "barcode")

    barcode_obj = code128(data, writer=ImageWriter())
    full_path = barcode_obj.save(filename)

    return render_template('bar.html', barcode_image=full_path)


@app.route('/decode', methods=['POST'])
def decode_barcode():
    file = request.files['file']

    if file:
        filepath = os.path.join(BARCODE_FOLDER, file.filename)
        file.save(filepath)

        image = cv2.imread(filepath)
        decoded_objects = decode(image)

        results = [obj.data.decode('utf-8') for obj in decoded_objects]

        return render_template('bar.html', decoded_data=results)

    return "No file uploaded"


@app.route('/process', methods=['POST'])
def process():
    data = request.json.get('data')

    # do whatever you want with the scanned code
    print("Scanned:", data)

    # Example logic:
    if data.startswith("http"):
        return {"redirect": data}
    else:
        return {"redirect": f"/result?data={data}"}


@app.route('/result')
def result():
    data = request.args.get('data')
    return f"<h1>Scanned Code: {data}</h1>"




if __name__ == '__main__':
    app.run(debug=True)
