"""
Count the number of every class in img_folder with yolo bounding box labels.
The folder must include classes.txt file for class names.
"""
import glob
from collections import Counter, OrderedDict
import matplotlib.pyplot as plt

img_folder = 'train' # 'test'

cls_file_path = img_folder + '/classes.txt'
cls_list = []
with open(cls_file_path, "r") as f:
    cls_list = f.read().splitlines() 
cls_list = [cls_elem for cls_elem in cls_list if cls_elem != '']

img_path_list = glob.glob(img_folder + '/*.jpg')
txt_path_list = glob.glob(img_folder + '/*.txt')# [14:] # [6:14] # [:6]

cls_cntr_dict = Counter()
for txt_path in txt_path_list:
    img_path = txt_path.split('.')[0] + '.jpg'
    if img_path in img_path_list:
        print(txt_path)
        
        txt_lines = []
        with open(txt_path, "r") as f:
            txt_lines = f.readlines()
        
        for txt_line in txt_lines:
            cls_ind = int(txt_line.split(' ')[0])
            cls_cntr_dict[cls_ind] += 1
        
#print(f'cls_cntr_dict = {cls_cntr_dict}')


od = OrderedDict(sorted(cls_cntr_dict.items()))
print(f'od = {od}')
for key, val in od.items():
    print(f'{cls_list[key]} : {val}')

xticks_list = [cls_list[ind] for ind in od.keys()]
plt.figure(figsize=(15,12))
plt.barh(list(od.keys()), list(od.values()))
plt.yticks(list(od.keys()), xticks_list)#, rotation=-90)
plt.xlabel('number')
plt.gca().invert_yaxis()
plt.grid()
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/barh.html

