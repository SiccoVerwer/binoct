import os
import glob
import learn_class_bin as lcb
import sys

#path1 = 'D:\Sicco\Dropbox\Dropbox\INFORMS-J-Optimization\dataset-cg-paper'
#path1 = 'D:\Sicco\Dropbox\Dropbox\INFORMS-J-Optimization\data-exp'

#for filename in os.listdir(path2):

path1 = sys.argv[1]

for filename in glob.glob(os.path.join(path1, '*.train*.csv')):
    print(filename)
     #lcb.main(["-f",filename, "-d", 1, "-t", 900, "-p", 300])

    #for depth in range(1,5):
    #lcb.main(["-f",filename, "-d", depth, "-t", 600, "-p", 150])
    lcb.main(["-f",filename, "-d", 4, "-t", 3600, "-p", 600])

    #for depth in range(1,5):
    #lcb.main(["-f",filename, "-d", 4, "-t", 600, "-p", 150, "-x", 20, "-s", 1])
    #lcb.main(["-f",filename, "-d", depth, "-t", 600, "-p", 150, "-x", 10, "-s", 1])
