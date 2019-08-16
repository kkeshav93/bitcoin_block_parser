import os
import datetime
import binascii as bhex

dir_dat = os.listdir("../data/")
dat_file_list = [files for files in dir_dat if (files.endswith('.dat') and files.startswith('blk'))]
dat_file_list.sort()


for i in dat_file_list:
    parsed_file = i.replate('.dat','.txt')

    print(parsed_file)


#while f.tell() != fsize:
