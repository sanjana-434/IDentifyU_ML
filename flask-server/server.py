# from flask import Flask, jsonify
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)  # Enable CORS for the entire app

# @app.route("/api/members")
# def get_members():
#     members = ["Member1", "Member2", "Member3"]
#     return jsonify(members)

# if __name__ == "__main__":
#     app.run()


'''
import cv2

# Set the desired frame width and height
frame_width = 1280  # Adjust this value as needed
frame_height = 720  # Adjust this value as needed

# Open the default camera (usually camera index 0)
cap = cv2.VideoCapture(0)

# Set the frame width and height for the camera
cap.set(3, frame_width)  # 3 is the identifier for width
cap.set(4, frame_height)  # 4 is the identifier for height

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Create a window to display the camera frame
cv2.namedWindow("Camera Frame", cv2.WINDOW_NORMAL)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    # Display the frame
    cv2.imshow("Camera Frame", frame)

    # Check for key press (press 's' to save, 'q' to quit)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        # Save the frame as an image
        cv2.imwrite("captured_image.jpg", frame)
        print("Image saved as 'captured_image.jpg'")
    elif key == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
'''

import os
import numpy as np
import matplotlib.pyplot as plt
import cv2
import pickle
import random
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from PIL import Image

dir = 'IDentifyU/dataset'

categories = ['AngelinaJulie','WillSmith']
data = []

for category in categories:
    path = os.path.join(dir,category)
    label = categories.index(category)

    for img in os.listdir(path):
        img_path = os.path.join(path,img)
        
        person_img = cv2.imread(img_path,0)  # 0->grayscale
    #     cv2.imshow('image',person_img)
    #     break
    # break
        try:
            person_img = cv2.resize(person_img,(50,50))
            image = np.array(person_img).flatten()
            data.append([image,label])
        except Exception as e:
            pass

print("Len of dataset : ",len(data))

random.shuffle(data)
features = []
labels = []
for feature,label in data:
    features.append(feature)
    labels.append(label)

fig, axes = plt.subplots(2, 3, figsize=(10, 6))

for i in range(5):
    d = data[i][0].reshape(50, 50)
    label = data[i][1]
    
    # Determine the position of the subplot in the 2x3 grid
    row = i // 3  # Integer division to get the row
    col = i % 3   # Modulo operation to get the column
    
    # Select the appropriate subplot in the grid
    ax = axes[row, col]
    
    ax.imshow(d, cmap='gray')  # Assuming grayscale images
    ax.set_title(f"Label: {label}")
    ax.axis('off')  # Turn off axis labels

# Adjust the spacing between subplots
plt.tight_layout()

# Display the subplots
plt.show()

x_train,x_test,y_train,y_test = train_test_split(features,labels,test_size=0.2)

model = SVC(C=1,kernel='poly',gamma='auto')
model.fit(x_train,y_train)
prediction = model.predict(x_test)

accuracy = model.score(x_test,y_test)

print(accuracy)
print('Prediction : ',categories[prediction[0]])

person = x_test[0].reshape(50,50)
plt.imshow(person,cmap = 'gray')
plt.show()



image_path = 'C:/Users/User/Downloads/captured-image.jpg'  # Replace with the actual path to your image
image = Image.open(image_path)  # Open the image
image = image.resize((50, 50))  # Resize to the expected size (50x50)
image = image.convert('L')  # Convert to grayscale
image = np.array(image)  # Convert to a NumPy array

# Reshape the image to match the model's input shape
image = image.reshape(1, -1)

# Make a prediction
prediction = model.predict(image)

print('Prediction: ', categories[prediction[0]])

person = image.reshape(50,50)
plt.imshow(person,cmap = 'gray')
plt.show()