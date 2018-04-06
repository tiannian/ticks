class Plugins:
    def __init__(conn,db):
        self.conn = conn
        self.db = db

    async def deal(self,pid,request):
        ## map request to call. deal request and resopnse
        pass

    def start_plugins(self):
        pass

    def register(self,name,version,category=[]):
        pass

    def unregister(self,pid):
        pass

    def load(self,pid):
        pass
    
    def unload(self,pid):
        pass

    def status(self,pid):
        pass

    def list(self):
        pass

    def enable(self,pid):
        pass

    def disable(self,pid):
        pass
