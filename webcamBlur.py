import os
import face_recognition
import cv2
import numpy as np

video_capture = cv2.VideoCapture(0)  #could be -1
face_locations = []

list = []

print(len(os.listdir("./crop_image")))

for file in os.listdir("./crop_image"):
    if file.endswith(".jpg"):
        list.append(os.path.join("./crop_image", file))

known_face_encodings = []

for cropped_image in list:
    image = face_recognition.load_image_file(cropped_image)
    face_encoding = face_recognition.face_encodings(image)[0]

    # Create arrays of known face encodings and their names
    known_face_encodings.append(face_encoding)

detected_unknown_face_coordinates = []
detected_known_face_coordinates = []
eye_data = cv2.CascadeClassifier('./haarcascade_eye.xml')

while (True) :
    ret, frame = video_capture.read() 
    small_frame = cv2.resize(frame, (0, 0), fx=0.16, fy=0.16)

    if (len(os.listdir("./crop_image")) != len(list)):
        list =[]
        for file in os.listdir("./crop_image"):
            if file.endswith(".jpg"):
                list.append(os.path.join("./crop_image", file))

        known_face_encodings = []

        for cropped_image in list:
            image = face_recognition.load_image_file(cropped_image)
            face_encoding = face_recognition.face_encodings(image)[0]

            # Create arrays of known face encodings and their names
            known_face_encodings.append(face_encoding)


            dimensions = frame.shape
            frame_width = dimensions[0]
            frame_height = dimensions[1]

    face_locations = face_recognition.face_locations(small_frame, model="cnn")
    face_encodings = face_recognition.face_encodings(small_frame, face_locations)

    
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"

        # Or instead, use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = "Known"

        if name == "Unknown" :
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 6.25
            right *= 6.25
            bottom *= 6.25
            left *= 6.25

            detected_unknown_face_coordinates = [top, right, bottom, left]

            # Extract the region of the image that contains the face
            face_image = frame[round(top):round(bottom), round(left):round(right)]
            # Blur the face image
            face_image = cv2.GaussianBlur(face_image, (99, 99), 30)

            # Put the blurred face region back into the frame image
            frame[round(top):round(bottom), round(left):round(right)] = face_image

        if name != "Unknown":
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            detected_known_face_coordinates = [top, right, bottom, left]


    eye_found = eye_data.detectMultiScale(frame, minSize=(20, 20))

    if len(eye_found) != 0:
        for (x, y, width, height) in eye_found:
            if (len(detected_unknown_face_coordinates) == 0) or ((detected_unknown_face_coordinates[0] < y < detected_unknown_face_coordinates[2]) and (detected_unknown_face_coordinates[1] < x < detected_unknown_face_coordinates[3])):
                if (len(detected_known_face_coordinates) == 0) or ((detected_known_face_coordinates[0] < y < detected_known_face_coordinates[2]) and (detected_known_face_coordinates[1] < x < detected_known_face_coordinates[3])):
                    # cv2.rectangle(frame, (x, y), (x + height, y + width), (0, 255, 0), 5)
                    if (y - 2*height) < 0:
                        frame_top = 0
                    else:
                        frame_top = (y - 2*height)
                    if (y + 4*height) > 720:
                        frame_bottom = 720
                    else:
                        frame_bottom = (y + 4*height)
                    if (x - 2*width) < 0:
                        frame_left = 0
                    else:
                        frame_left = (x - 2*width)
                    if x + 2*width > 1280:
                        frame_right = 1280
                    else:
                        frame_right =  x + 2*width
                    face_image = frame[frame_top:frame_bottom, frame_left:frame_right]
                    # face_image = cv2.GaussianBlur(face_image, (99, 99), 30)
                    frame[frame_top:frame_bottom, frame_left:frame_right] = face_image

    cv2.imshow("video", frame)
    if cv2.waitKey(1) and 0xFF==ord("q"):
        break

    detected_unknown_face_coordinates = []
    detected_known_face_coordinates = []

video_capture.release()
cv2.destroyAllWindows()

