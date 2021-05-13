cmake_minimum_required(VERSION 3.14)
project(ticks LANGUAGES CXX)

set(CMAKE_INCLUDE_CURRENT_DIR ON)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

find_package(Qt6 COMPONENTS Core)
find_package(Qt6 COMPONENTS Gui)
find_package(Qt6 COMPONENTS Qml)

qt_add_executable(ticks
    main.cpp
)

# set_target_properties(ticks PROPERTIES
    # WIN32_EXECUTABLE TRUE
    # MACOSX_BUNDLE TRUE
# )

add_custom_target(ticksrs ALL cargo build --release
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}/ticksrs)

target_link_libraries(ticks PUBLIC
    Qt::Core
    Qt::Gui
    Qt::Qml
)


set(ticks_resource_files
    "qml/main.qml"
    "qml/CompositorScreen.qml"
)

qt6_add_resources(ticks "ticks"
    PREFIX
        "/"
    FILES
        ${ticks_resource_files}
)
