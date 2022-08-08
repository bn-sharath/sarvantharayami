from imutils import paths
import os

print(os.path.join(os.getcwd(), "test_image"))
list_of_images = paths.list_images(os.path.join(os.getcwd(), "test_image", ""))
rename_images_dir = os.path.join(os.getcwd(), "test_image", "")

# print(list_of_images)

i = 1
for imagePath in list_of_images:
    print(imagePath)
    i_path, i_filename = os.path.split(imagePath)
    file_name, file_extension = os.path.splitext(i_filename)
    os.rename(imagePath, rename_images_dir+str(i)+file_extension)
    i = i+1
    print(imagePath)
