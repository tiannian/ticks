import QtQuick
import QtWayland.Compositor
import QtQuick.Window

WaylandOutput {
    id: screen
    property alias screen: win.screen
    property alias compositor: compositor
    property bool windowed: false
    sizeFllowWindow: true

    window: Window {
        id: window
        x: Screen.virtualX
        y: Screen.virtualY
        visible: true
        width: 800
        height: 600
        visibility: windowed ? Window.Windowed : Window.FullScreen

        Shortcut {
            sequence: "Ctrl+Alt+Backspace"
            onActivated: Qt.quit()
        }
    }
}

