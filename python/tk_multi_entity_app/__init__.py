# Copyright (c) 2015 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.


def show_dialog(app):
    """Show the main dialog."""

    from .dialog import PublishedFilesAppDialog

    app_title = app.get_setting("title_name")


    from sgtk.platform.qt import QtGui, QtCore
    QtGui.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
    try:
        return app.engine.show_dialog(app_title, app, PublishedFilesAppDialog)
    finally:
        QtGui.QApplication.restoreOverrideCursor()

