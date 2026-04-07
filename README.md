# Barcode Scanner

A simple barcode scanner application that captures barcode data and processes it in real time.

## Overview

This project is designed to scan barcodes efficiently and return the decoded result for further use in applications such as inventory management, product lookup, or smart cart systems. 

The deployed version supports camera-based input in modern browsers, including mobile devices such as iOS (via HTTPS for access to Apple camera interface). 

This project was developed locally, and packaged into a Github repository for sharing. 

## License 

This project is licensed under the MIT license. 

## Features

- Real-time barcode scanning
- Fast decoding of barcode content
- Simple and lightweight project structure
- Easy to integrate into larger systems
- Suitable for learning, prototyping, and coursework demonstrations

## Tech Stack

List your actual stack here, for example:

- Python 
- Flask 
- pyzbar
- barcode-scanner library
- HTML
- JavaScript
- AWS EC2

## Deployment & Live Demo

The application is deployed on AWS EC2. You can access the deployed version of the application here: 

https://allergysmartcart.duckdns.org

It runs a Flask server to handle requests and serve the web interface. 

## Local Installation

To run locally: 

### Clone the repository:

```bash
git clone https://github.com/caocaoyixin-maker/barcode-scanner.git
cd barcode-scanner
```

### Create a virtual environment:

1. Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

2. macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install dependencies: 

```bash
pip install -r requirement.txt
```

### System dependencies: 

This project requires the 'zbar' library. 

1. macOS (tested)

```bash
brew install zbar
export DYLD_LIBRARY_PATH=$(brew --prefix zbar)/lib
```

2. Linux (untested, may require)

```bash
sudo apt update
sudo apt install libzbar0
```

3. Windows (untested)

Windows may require installing the ZBar library separately and ensuring it is available in you system PATH. 

### Run the application: 

```bash
python app.py
```

### Open in your browser: 

```plain text
http://127.0.0.1:5000
```

## Future Improvements

- Integrate a database for more robust data management
- Improve frontend UI/UX for better usability
- Enhance backend structure and error handling
- Optimise deployment for scalability and reliability 
