"""
To arrange and overwrite the *.txt file for YOLO LabelImg
The overwritten *.txt file will follow order from 0 to 1000
"""
import glob
from collections import OrderedDict

folder = 'train' # 'test'
txt_path_list = glob.glob(folder + '/*.txt')


for txt_path in txt_path_list:
    txt_lines = []
    with open(txt_path, "r") as f:
        txt_lines = f.readlines()

    #txt_lines_sorted = sorted(txt_lines)
    
    #dict_nbr_ind = OrderedDict()
    dict_nbr_txt = dict()
    for ind, txt_line in enumerate(txt_lines):
        nbr = int(txt_line.split(' ')[0])
        #print(nbr)
        #dict_nbr_ind[nbr] = ind
        if nbr not in  dict_nbr_txt.keys():
            dict_nbr_txt[nbr] = [txt_line]
        else:
            dict_nbr_txt[nbr].append(txt_line)
    
    od = OrderedDict(sorted(dict_nbr_txt.items()))
    
    with open(txt_path, "w") as f:
        for item_list in od.values():
            #print(item_list)
            for item in item_list:
                f.write(item)
                
