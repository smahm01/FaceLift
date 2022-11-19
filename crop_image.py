import os
import cv2
import face_recognition
    
def crop_images(): 
    
    list = []

    for file in os.listdir("./images"):
        if file.endswith(".jpg"):
            list.append(os.path.join("./images", file))
            
    print(list)

    for image in list: 

        image_name = image.split("/")[-1].split(".")[0]
        
        print(image_name)
        # Read the input image
        img = cv2.imread(image)

        face_locations = face_recognition.face_locations(img, model="cnn")

        face_int = 0

        for (top, right, bottom, left) in face_locations:
            print(top, right, bottom, left)
            faces = img[top-30:bottom+30, left-30:right+30]

            #cv2.imshow("face",faces)
            cv2.imwrite('./crop_image/' + image_name + str(face_int) + '.jpg', faces)
            face_int += 1
            
    return "done"
