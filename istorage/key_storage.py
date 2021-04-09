import os
import re
import copy
import datetime
import time
import random
import pickle
from sqlitedict import SqliteDict #pip install -U sqlitedict

LOCAL_DIR = os.path.abspath(os.path.dirname(__file__))+"/"


#0v6# JC  Dec  3, 2020  Return removed/popped item
#0v5# JC  Oct 13, 2020  Allow storage_dir     
#0v4# JC  Aug 20, 2019  pre-crawler migration
#0v3# JC  Apr 17, 2019  Reuseable
#0v2# JC  Apr  6, 2019  Generic peristent key storage
#0v1# JC  Mar 27, 2019

#TODO:
# watch as get_ and set_ are not semiphore protected


class NestedDict(dict):
    def __getitem__(self, key):
        if key in self: return self.get(key)
        return self.setdefault(key, NestedDict())
    
class SqliteDict_Wrap(SqliteDict):
    def __init__(self,storage_dir='storage',name='default',absolute_dir=True):
        if not storage_dir: storage_dir='storage'

        if not re.search(r'^\/',storage_dir) and not re.search(r'\:',storage_dir):
            storage_dir=LOCAL_DIR+storage_dir
        elif storage_dir=='storage':
            storage_dir=LOCAL_DIR+storage_dir
        elif not absolute_dir:
            storage_dir=LOCAL_DIR+storage_dir
        else:
            storage_dir=storage_dir

        if not os.path.exists(storage_dir):
            os.mkdir(storage_dir)

        self.name=name
        self.storage_filename=storage_dir+"/"+name+"_db.sqlite"
        storage_filename=storage_dir+"/"+name+"_db.sqlite"
        #super(SqliteDict_Wrap,self).__init__(storage_filename,autocommit=False)
        #Old style:
        SqliteDict.__init__(self,storage_filename,autocommit=False)
        return
    
    def get_dd(self,key):
        if key in self:   #Fails here if key is invalid type 
            return self[key]
        else:
            return NestedDict()
    
    def set_dd(self,key,dd,do_commit=True):
        self[key]=dd
        if do_commit:
            self._commit()
        return
    
    def remove_dd(self,key,do_commit=True):
        dd={}
        if key in self:
            dd=self.pop(key) #dict pop or remove?
            if do_commit:
                self._commit()
        return dd

    def _commit(self):
        try:
            self.commit()
        except Exception as e:
            #Aug 8, 2019 saw attempt to write readonly db
            print ("[warning sqlite b] commit error (retry): "+str(e))
            time.sleep(10)
            self.commit()
        return

def dev_storage2():
    DB=SqliteDict_Wrap()
    print ("ok2")
    dd=DB.get_dd('jon1')
    dd['this']['world']=True
    DB.set_dd('jon1',dd)
    dd=DB.get_dd('jon1')
    print ("GOT: "+str(dd))
    return

if __name__=='__main__':
    branches=['dev_storage2']
    for b in branches:
        globals()[b]()
        
        
        
        
        
        
        
        
        
