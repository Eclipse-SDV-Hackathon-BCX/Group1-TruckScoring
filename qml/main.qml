import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    function show_positive_change(change){
        positive_change.text = '+' + change.toString();
        positive_change.visible = true;
        positive_change_animation.restart();
    }

    function show_negative_change(change){
        negative_change.text = '-' + change.toString();
        negative_change.visible = true;
        negative_change_animation.restart();
    }

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

    Text {
        id: positive_change
        visible: false
        anchors.left: score_value.right
        anchors.verticalCenter: score_value.verticalCenter
        anchors.leftMargin: 50

        text: "+10"

        color: "green"
        font.pointSize: 40
    }

    PropertyAnimation {
        id: positive_change_animation
        running: true
        target: positive_change
        property: 'visible'
        to: false
        duration: 1500
    }

    Text {
        id: negative_change
        visible: false
        anchors.left: score_value.right
        anchors.verticalCenter: score_value.verticalCenter
        anchors.leftMargin: 50

        text: "-10"

        color: "red"
        font.pointSize: 40
    }

    PropertyAnimation {
        id: negative_change_animation
        running: true
        target: negative_change
        property: 'visible'
        to: false
        duration: 1500
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