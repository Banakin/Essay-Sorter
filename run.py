# -*- coding: utf-8 -*-
import os
import time
from wrdbank import wwrds

good_path = "sorted/good/"
bad_path = "sorted/bad/"
sort_path = "to_sort/"
to_sort = os.listdir(sort_path)

filecount = len(to_sort)
if filecount == 0:
    print("No files to be sorted!")
    print("Waiting 5 seconds...")
    time.sleep(5)
    print("Exiting")
    exit()
else:
    print("Files have been found!")
    while filecount > 0:
        filecount = filecount - 1

        goodfile = 1
        
        essaytxt = open(sort_path + to_sort[filecount], 'r').read().replace('\n', '')
        wrdcount = len(wwrds)
        while wrdcount > 0:
            wrdcount = wrdcount - 1
            
            if wwrds[wrdcount] in essaytxt.lower():
                print("The word '" + wwrds[wrdcount] + "' has been found in file '" + to_sort[filecount] + "'")
                goodfile = 0
            else:
                print("The word '" + wwrds[wrdcount] + "' has NOT been found in file '" + to_sort[filecount] + "'")
        if goodfile != 0:
            print(to_sort[filecount] + " is good")
            os.rename(sort_path + to_sort[filecount], good_path + to_sort[filecount])
            print("Sorted File")
        else:
            print(to_sort[filecount] + " is bad")
            os.rename(sort_path + to_sort[filecount], bad_path + to_sort[filecount])
            print("Sorted File")
