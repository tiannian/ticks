import pyejdb

class DB:
    def __init__(self):
        self.ejdb = pyejdb.EJDB("ticks.db", 
                pyejdb.DEFAULT_OPEN_MODE | 
                pyejdb.JBOREADER | 
                pyejdb.JBOWRITER | 
                pyejdb.JBOCREAT )
    
    def get_conn(self):
        return self.ejdb

