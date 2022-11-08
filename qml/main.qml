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

    Loader {
        id: pageLoader
        anchors.fill: parent

        source: "MainPage.qml"
    }


}