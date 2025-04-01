# 3D Reconstruction API

This project provides an API that accepts a ZIP file containing images, processes them using Meshroom to generate 3D reconstructions, and returns the output as a ZIP file.

## Features

- **Upload Images**: Submit a ZIP file of images to the API.
- **3D Reconstruction**: Automatically process the images using Meshroom.
- **Download Results**: Retrieve the reconstructed 3D model as a ZIP file.

## Installation

1. **Clone the Repository**:
```bash
    git clone https://github.com/Aura-Decor/3D.git
   cd 3D
```

## Prerequisites

- **Python 3.9 or higher**: Ensure you have Python installed on your system.
- **Cloning Meshroom**
```bash
wget https://github.com/alicevision/Meshroom/releases/download/v2019.1.0/Meshroom-2019.1.0-linux.tar.gz.
tar -xzf Meshroom-2019.1.0-linux.tar.gz -C ./
```
- **Install Dependencies**
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```

## Usage
- **Start the API Server**
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 5000
```
- **Access the API**: Open postman and navigate to http://0.0.0.0:5000/generate-3d-model endpoint to upload your ZIP file of images and download the resulting 3D model.

