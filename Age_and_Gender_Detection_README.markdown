# Age and Gender Detection System

This project detects age and gender from live video feeds using DeepFace and OpenCV. It stores detections in MySQL and is optimized for CUDA-enabled devices like Jetson Nano.

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Set up MySQL: Run the SQL in `database.sql`.
3. Update MySQL credentials in `config.py`.
4. Run `python main.py` for live detection.

## Dependencies
- deepface, opencv-python, tensorflow, mysql-connector-python

## Usage
- Runs on webcam by default; detections saved to DB.

Note: For best performance, use CUDA. Download datasets like UTKFace for custom training if needed.