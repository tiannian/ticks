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
        self.clients = {}

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
                X.ReparentNotify: lambda e:self.on_reparent_notify(e),
                }
        while not self.has_other_wm:
            event = self.display.next_event()
            #  print(event)
            selector[event.type](event)
            

    def frame_header(self,window):
        if window in self.clients:
            return
        x = window.get_geometry().x
        y = window.get_geometry().y
        width = window.get_geometry().width
        height = window.get_geometry().height
        border_width = window.get_geometry().border_width

        window.change_save_set(X.SetModeInsert)
        # Create Contour
        frame = self.root.create_window(x,y,width,height+20,1,0)
        window.reparent(frame,0,20)
        self.clients[window] = frame
        frame.map()
        # Create title window

        print(x, y, width, height, border_width)

    def on_create_notify(self,event):
        pass

    def on_map_request(self,event):
        if event.window.get_attributes().override_redirect == 0:
            self.frame_header(event.window)
            event.window.map()

    def on_map_notify(self,event):
        pass
        #  print(event)

    def on_unmap_notify(self,event):
        pass
        #  print(event)

    def on_destroy_notify(self,event):
        pass
        #  print(event)

    def on_reparent_notify(self,event):
        pass


if __name__ == '__main__':
    wm = WM()
    wm.run()
