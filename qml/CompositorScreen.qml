import QtQuick
import QtWayland.Compositor
import QtQuick.Window

WaylandOutput {
    id: screen
    property alias screen: win.screen
    property bool windowed: false

    sizeFollowsWindow: true

    window: Window {
        id: win
        x: Screen.virtualX
        y: Screen.virtualY
        visible: true
        width: 800
        height: 800
        visibility: windowed ? Window.Windowed : Window.FullScreen

        Shortcut {
            sequence: "Ctrl+Alt+Backspace"
            onActivated: Qt.quit()
        }
    }
}

