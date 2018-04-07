from Xlib.display import Display
from Xlib import X
import logging

class WM:
    def __init__(self):
        self.display = Display()
        self.root = self.display.screen()['root']
        self.has_other_wm = False
        def onerror(error,obj):
            logging.error('Has other Windows Manager is running.')
            self.has_other_wm = True
        self.root.change_attributes(onerror,
                event_mask = X.SubstructureNotifyMask |
                X.SubstructureRedirectMask)
        self.display.sync()

    def load_already_exists_window(self):
        print(self.root.query_tree())
        children = self.root.query_tree().children
        for x in children:
            print(x)

    def run(self):
        #  self.load_already_exists_window()
        selector = {
                X.CreateNotify: lambda e: self.on_create_notify(e),
                X.MapRequest: lambda e:self.on_map_request(e),
                X.MapNotify: lambda e:self.on_map_notify(e),
                X.UnmapNotify: lambda e:self.on_unmap_notify(e),
                X.DestroyNotify: lambda e:self.on_destroy_notify(e),
                }
        while not self.has_other_wm:
            event = self.display.next_event()
            #  print(event)
            selector[event.type](event)
            

    def on_create_notify(self,event):
        print(event)

    def on_map_request(self,event):
        if event.window.get_attributes().override_redirect == 0:
            event.window.map()

    def on_map_notify(self,event):
        print(event)

    def on_unmap_notify(self,event):
        print(event)

    def on_destroy_notify(self,event):
        print(event)


if __name__ == '__main__':
    wm = WM()
    wm.run()
