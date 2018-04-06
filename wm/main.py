from Xlib import X
from Xlib.display import Display

if __name__ == '__main__':
    dp = Display()
    name = dp.get_display_name()
    print(name)
