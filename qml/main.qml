import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    id: window

    visible: true
    visibility: "FullScreen"
    width: 600
    height: 500
    title: "Truckmania"

    Text {
        id: score_value
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
        text: main_controller.score

        font.bold: true
        font.pointSize: 130
    }

    Text {
        id: driver_name
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.bottom: score_value.top
        anchors.bottomMargin: 50
        text: main_controller.driver_name

        font.pointSize: 60
    }

    Text {
        id: task
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: score_value.bottom
        anchors.topMargin: 100

        text: main_controller.task

        font.pointSize: 80
    }

    Image {
        id: avatar_image
        width: 250
        height: 250

        anchors.horizontalCenter: parent.horizontalCenter
        anchors.bottom: driver_name.top

        source: "../res/avatar.jpg"
    }
}