import QtQuick 2.12
import QtQuick.Layouts 1.12
import QtQuick.Controls 2.5

Rectangle {

    radius: 4

    property string controlSource
    property string controlTitle

    Rectangle {
        radius: 4
        anchors.top: parent
        anchors.left: parent
        anchors.right: parent
        height: 40

        RowLayout {
            margins: 4
            spacing: 16

            Image {
                source: controlSource
                sourceSize: Qt.size(controlSize, controlSize)
            }

            Label {
                text: controlTitle
                font.pixelSize: 24
                wrapMode: "Wrap"
            }
        }
    }


}
