import os
import test

def image_predeict(file_url):
    origin_loc = os.getcwd()
    image_dir = origin_loc + file_url

    with open('image_paths', 'w') as f:
        f.write(image_dir)
    input_path = origin_loc + '/image_paths'
    print(input_path)
    os.chdir("C:/Users/ipsl/Desktop/darknet-master/darknet-master/build/darknet/x64")
    os.system("darknet detector test data/food100.data cfg/yolov3-food.cfg backup/yolov3-food_last.weights -dont_show < "+input_path+" > result.txt")
    os.chdir(origin_loc)







