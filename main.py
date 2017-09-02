import os
import shutil
from main_scrable import *

if __name__=='__main__':
    test=Scrable_all()
    test.scrbl_all()
    #test.scrable_info()
    path_from='/'.join((os.path.join(__file__).split('/')[:-1]))+'/rscrable.res.db'
    path_to='/'.join((os.path.join(__file__).split('/')[:-2]))+'/my_site/rscrable.res.db'
    print(path_from,path_to,sep = '\n')
    shutil.copyfile(path_from,path_to)
