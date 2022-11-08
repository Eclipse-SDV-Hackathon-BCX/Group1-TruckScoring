import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    id: window

    visible: true
    visibility: "FullScreen"
    width: 600
    height: 500
    title: "FUNDRIVE"

    Text {
        id: score_value
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
        text: "000"

        font.bold: true
        font.pointSize: 130
    }

    Text {
        id: driver_name
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.bottom: score_value.top
        text: "Driver XY"

        font.pointSize: 80
    }

    Text {
        id: task
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: score_value.bottom
        text: "Do ABC"

        font.pointSize: 80
    }
}