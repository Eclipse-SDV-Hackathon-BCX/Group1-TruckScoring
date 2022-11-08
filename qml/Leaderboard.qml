import QtQuick 2.15
import QtQuick.Controls 2.15

Item {
    anchors.fill: parent

    Image {
        anchors.verticalCenter: parent.verticalCenter
        anchors.horizontalCenter: parent.horizontalCenter

        source: "../res/background2.jpg"
    }

    Button {
        opacity: 0
        x: 14
        y: 894
        width: 583
        height: 160

        onClicked: {
            pageLoader.source = "MainPage.qml"
        }
    }
}