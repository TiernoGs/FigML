import QtQuick 2.12
import QtQuick.Controls 2.5

Rectangle {
    id: rectangle

    property string controlText
    property color controlColor
    color: controlColor
    radius: 4

    Label {
        text: "Ct"
        textFormat: Text.AutoText
        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignHCenter
        anchors.fill: parent
        color: "#DFDFDF"
    }


    signal buttonClicked()
    width: 34
    height: 34

    MouseArea {
        hoverEnabled: true
        anchors.fill: parent
    }
}
