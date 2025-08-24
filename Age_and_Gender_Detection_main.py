import cv2
from deepface import DeepFace
import mysql.connector
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB

def store_detection(age, gender):
    conn = mysql.connector.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, database=MYSQL_DB)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO faces (age, gender) VALUES (%s, %s)", (age, gender))
    conn.commit()
    cursor.close()
    conn.close()

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    try:
        result = DeepFace.analyze(frame, actions=['age', 'gender'], enforce_detection=False)
        for face in result:
            age = face['age']
            gender = face['dominant_gender']
            print(f"Age: {age}, Gender: {gender}")
            store_detection(age, gender)
    except:
        pass
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()