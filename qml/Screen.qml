import QtQuick
import QtWayland.Compositor
import QtQuick.Window

WaylandOutput {
    id: screen
    property alias screen: win.screen
    sizeFllowWindow: true

    window: Window {
        id: window
        x: Screen.virtualX
        y: Screen.virtualY

        Shortcut {
            sequence: "Ctrl+Alt+Backspace"
            onActivated: Qt.quit()
        }
    }
}

