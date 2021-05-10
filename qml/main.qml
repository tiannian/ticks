import QtQuick
import QtQml
import QtQml.Models
import QtQuick.Window
import QtQuick.Layouts
import QtWayland.Compositor
import QtWayland.Compositor.XdgShell
import QtWayland.Compositor.WlShell

WaylandCompositor {
    // The output defines the screen.
    id: compositor
    // defaultOutput: output1

    // For emulated screen
    ListModel {
        id: emulatedScreens
        ListElement { name: "left";   virtualX: 0;    virtualY: 0; width: 800; height: 600 }
        ListElement { name: "right";  virtualX: 800;  virtualY: 0; width: 800; height: 600 }
    }

    property bool emulated: Qt.application.arguments[1] != "tty"

    Component.onCompleted: {
        console.log("start with ", emulated ? "emulated": "tty")
    }

    Instantiator {
        id: screens
        model: emulated ? emulatedScreens: Qt.application.screens

        delegate: CompositiorScreen {
            screen: modelData
            compositor: compositor
            windowed: emulated
        }
    }

    // XdgOutputManagerV1 {}
//     XdgShell {
    //     onToplevelCreated: shellSurfaces.append({shellSurface: xdgSurface});
    // }
    // WlShell {
    //     onWlShellSurfaceCreated: shellSurfaces.append({shellSurface: shellSurface});
    // }
    // XdgDecorationManagerV1 {
    //     preferredMode: XdgToplevel.ServerSideDecoration
    // }
    // ListModel { id: shellSurfaces }
}
