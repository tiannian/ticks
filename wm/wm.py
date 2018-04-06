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

    def run(self):
        while not self.has_other_wm:
            event = self.display.next_event()
            print(event)


if __name__ == '__main__':
    try:
        wm = WM()
        wm.run()
    except Exception as e:
        #  print(e)
        pass
