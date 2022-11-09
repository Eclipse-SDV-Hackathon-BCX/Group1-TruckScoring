import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    id: window

    visible: true
    visibility: "FullScreen"
    width: 600
    height: 500
    title: "Truckmania"

    Loader {
        id: pageLoader
        anchors.fill: parent

        source: "MainPage.qml"
    }


}