# Copyright (c) 2015 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

import sgtk
import os


class PublishedFilesApp(sgtk.platform.Application):
    def init_app(self):
        """Called as the application is being initialized."""

        if not self.engine.has_ui:
            return

        tk_multi_entity_app = self.import_module("tk_multi_entity_app")

        # register command
        display_name = self.get_setting("menu_name", "Published Files")
        self.engine.register_command(
            f"{display_name}...",
            lambda: tk_multi_entity_app.show_dialog(self),
            {
                "short_name": display_name.replace(" ", "_"),
            },
        )

    def _log_metric_viewed_app(self):
        """Module local metric logging helper method for the "Logged In" metric."""

        try:
            from sgtk.util.metrics import EventMetric

            EventMetric.log(
                EventMetric.GROUP_TOOLKIT,
                "Opened Multi Published Files App",
                log_once=False,
                bundle=self,
            )
        except:
            # Ignore all errors, e.g. using a core that does not support metrics.
            pass
