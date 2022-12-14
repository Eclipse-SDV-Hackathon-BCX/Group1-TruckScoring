import QtQuick 2.15
import QtQuick.Controls 2.15

Item {
    Connections {
        target: main_controller

        function onShow_positive_change(change) {
            positive_change.anchors.bottomMargin = -150;
            positive_change.text = '+' + change.toString();
            positive_change.visible = true;
            positive_change_animation.restart();
        }

        function onShow_negative_change(change) {
            negative_change.anchors.topMargin = -200;
            negative_change.text = '-' + change.toString();
            negative_change.visible = true;
            negative_change_animation.restart();
        }
    }
    anchors.fill: parent

    Image {
        anchors.verticalCenter: parent.verticalCenter
        anchors.horizontalCenter: parent.horizontalCenter

        source: "../res/background.jpg"
    }

    Text {
        id: score_value
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
        text: main_controller.score

        color: "white"
        font.family: "Jaapokki"
        font.pointSize: 250
    }

    Text {
        id: task
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: score_value.bottom
        anchors.topMargin: 0

        color: "white"

        text: main_controller.task

        font.family: "Jaapokki"
        font.pointSize: 80
    }

    Text {
        id: positive_change
        visible: false
        anchors.left: score_value.right
        anchors.bottom: score_value.top
        anchors.leftMargin: -50
        anchors.bottomMargin: -150

        text: "+10"

        color: "green"
        font.pointSize: 100
    }
    ParallelAnimation {
        id: positive_change_animation
        PropertyAnimation {
            target: positive_change
            property: 'visible'
            to: false
            duration: 1500
        }
        PropertyAnimation {
            target: positive_change
            property: 'anchors.bottomMargin'
            to: 1050
            duration: 1500
        }
    }


    Text {
        id: negative_change
        visible: false
        anchors.left: score_value.right
        anchors.top: score_value.bottom
        anchors.topMargin: -200
        anchors.leftMargin: -50
        text: "-10"

        color: "red"
        font.pointSize: 100
    }

    ParallelAnimation {
        id: negative_change_animation
        PropertyAnimation {
            target: negative_change
            property: 'visible'
            to: false
            duration: 1500
        }
        PropertyAnimation {
            target: negative_change
            property: 'anchors.topMargin'
            to: 1000
            duration: 1500
        }
    }

    Button {
        opacity: 0
        x: 14
        y: 894
        width: 583
        height: 160

        onClicked: {
            pageLoader.source = "Leaderboard.qml"
        }
    }

    //Rectangle {
    //    width: avatar_image.width + driver_name.width + 40
    //    height: avatar_image.height + 20
    //    radius: 50
    //    color: Qt.rgba(1,1,1,0.8)

    //    anchors.left: parent.left
    //    anchors.top: parent.top
    //    anchors.leftMargin: 20
    //    anchors.topMargin: 20

    //    Image {
    //        id: avatar_image
    //        width: 128
    //        height: 128

    //        anchors.left: parent.left
    //        anchors.top: parent.top
    //        anchors.topMargin: 10
    //        anchors.leftMargin: 10

    //        source: "../res/avatar.png"
    //    }

    //    Text {
    //        id: driver_name
    //        anchors.left: avatar_image.right
    //        anchors.verticalCenter: avatar_image.verticalCenter
    //        anchors.leftMargin: 20

    //        text: main_controller.driver_name

    //        font.pointSize: 45
    //    }
    //}
}