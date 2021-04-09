import os,sys
import datetime
import random
import json

LOCAL_PATH = os.path.abspath(os.path.dirname(__file__))+"/"
sys.path.insert(0,LOCAL_PATH)
from key_storage import SqliteDict_Wrap
from key_storage import NestedDict

#**add auto refresh

#0v9# JC Mar 18, 2021  Return record at db_update
#0v8# JC Dec  3, 2020  Add is_exists
#0v7# JC Oct  6, 2020  Flexible storage mount point
#0v6# JC Dec 10, 2019  Randomize pop
#0v5# JC Dec  4, 2019  Return removed record
#0v4# JC Aug 20, 2019  pre-crawler migration
#0v3# JC Jul 31, 2019  Include update dict
#0v2# JC Apr 26, 2019  Extend from xstorage


def decode_dict(d):
    ## Dict can't have byte keys
    ## Remove byte keys from dictionary
    #>> need to work with lists too
    result = {}
    for key, value in d.items():
        if isinstance(key, bytes):
            key = key.decode()
        if isinstance(value, bytes):
            value = value.decode()
        elif isinstance(value, dict):
            value = decode_dict(value)
        result.update({key: value})
    return result

class Storage_Helper(object):
    def __init__(self,storage_dir=''):
        #self.db_html=SqliteDict_Wrap(name='html')
        #self.db_meta=SqliteDict_Wrap(name='meta')
        self.dbs={}
        self.default_name='noname'
        self.storage_dir=storage_dir
        return
    
    def init_db(self,name):
        self.dbs[name]=SqliteDict_Wrap(name=name,storage_dir=self.storage_dir)
        self.default_name=name
        return
    
    def db_update(self,idx,the_key,the_value,name=''):
        ## Possibly issues with this?
        ## ** this works at ie dict level (not field level persay)
        #At given index.  Allows the key to be added to the dictionary without overwriting dict

        ##1/  Get dict
        if not name: require=name_stop

        org_dd=self.dbs[name].get_dd(idx)

        org_dd[the_key]=the_value
        org_dd['the_date']=datetime.datetime.now()
        
        print (" UPDATE> "+str(org_dd))

        self.dbs[name].set_dd(idx,org_dd)
        print (" UPDATE2> "+str(org_dd))
        ## Not returned because is entire dd
        return
    
    def db_put(self,idx,the_key,the_value,name=''):
        try: test_dump=json.dumps(the_value) ## Check prior to sqlite
        except:
            print ("[warning] could not json dump at: "+str(idx))
        if not name: name=self.default_name
        if not name in self.dbs: self.init_db(name)
        dd=NestedDict()
        dd[the_key]=the_value
        dd['the_date']=datetime.datetime.now()
        self.dbs[name].set_dd(idx,dd)
        return

    def db_get(self,idx,the_key,name=''):
        the_value=None
        if not name: name=self.default_name
        if not name in self.dbs:
            the_value=None
        else:
            dd=self.dbs[name].get_dd(idx)
            the_value=dd.get(the_key,None)
        return the_value
    
    def iter_database(self,name):
        for the_key in self.dbs[name]:
            yield the_key
        return

    def random_choice(self,name):
        the_key=''
        if self.dbs[name]:
            the_key=random.choice(self.dbs[name].keys())
        return the_key

    def db_remove(self,idx,name=''):
        dd=None
        the_value=None
        if not name: name=self.default_name
        if not name in self.dbs:
            the_value=None
        else:
            size_before=len(self.dbs[name])
            dd=self.dbs[name].remove_dd(idx)
            size_after=len(self.dbs[name])
            if size_before==size_after:
                print ("[error] did not remove at index: "+str(idx))
                dd=self.dbs[name].get_dd(idx)
                print ("RAW RECORD: "+str(dd))
                print ("New fun exists: "+str(self.is_exists(idx,name=name)))
                stopp=no_removal
        return dd
    
    def is_exists(self,idx,name=''):
        exists=False
        if not name: name=self.default_name
        if idx in self.dbs[name]: exists=True
        return exists
    
    

def test_storage():
    return


if __name__=='__main__':
    branches=['test_storage']
    for b in branches:
        globals()[b]()
    print ("Done.")



