QT += gui qml

SOURCES += \
    main.cpp

OTHER_FILES = \
    qml/main.qml
    qml/Screen.qml

RESOURCES += ticks.qrc

; target.path = $$[QT_INSTALL_EXAMPLES]/wayland/server-side-decoration
; sources.files = $$SOURCES $$HEADERS $$RESOURCES $$FORMS server-side-decoration.pro
; sources.path = $$[QT_INSTALL_EXAMPLES]/wayland/server-side-decoration
; INSTALLS += target sources
