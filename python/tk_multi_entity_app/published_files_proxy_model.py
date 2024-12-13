# Copyright (c) 2021 Autodesk, Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Autodesk, Inc.

from .framework_qtwidgets import FilterItemProxyModel


class PublishedFilesProxyModel(FilterItemProxyModel):
    """Proxy model for entities."""

    def __init__(self, *args, **kwargs):
        """Initialize."""

        super(PublishedFilesProxyModel, self).__init__(*args, **kwargs)
