import os
def delete_image_by_PATH(PATH):
    real_path_list = PATH.split(".")
    real_path_crop = "./crop_image/"+real_path_list[-3]+"."+real_path_list[-1]
    real_path_image= "./images/"+real_path_list[-3][:-1] +"."+ real_path_list[-1]
    print(os.path.exists(real_path_crop))
    print(real_path_image)
    if os.path.exists(real_path_crop):
        os.remove(real_path_crop)
    if os.path.exists(real_path_image):
        os.remove(real_path_image)
    return "Deleted both Image and Crop"
