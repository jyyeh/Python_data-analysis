from PIL import Image
import os

images_path = 'C:\\Users\\jerry.yeh\\Desktop\\CW\\SBIR\\image_test\\'
images_format = ['.jpg','.JPG']

image_size_w = 60
image_size_h = 60

image_row = 13
image_column = 2
image_save_path = 'C:\\Users\\jerry.yeh\\Desktop\\CW\\SBIR\\image_test\\test_2.jpg'

image_names = os.listdir(images_path)

len(image_names)
image_row * image_column

# if len(image_names) != image_row * image_column:
#     raise ValueError("合成圖片的引數和要求的數量不能匹配！")

def image_compose():
    to_image = Image.new('RGB',(image_column*image_size_w,image_row*image_size_h))

    for y in range(1,image_row+1):
        for x in range(1,image_column+1):
            from_image = Image.open(images_path + image_names[image_column*(y-1)+x-1]).resize((image_size_w,image_size_h),Image.ANTIALIAS)
            to_image.paste(from_image,((x-1)*image_size_w,(y-1)*image_size_h))
    return to_image.save(image_save_path)

image_compose()

# test  
#Image.open('C:\\Users\\jerry.yeh\\Desktop\\CW\\SBIR\\image_test\\S__36110358.jpg')
