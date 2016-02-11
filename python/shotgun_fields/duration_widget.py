# Copyright (c) 2015 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

"""
Widget that represents the value of a duration field in Shotgun
"""
from .shotgun_field_manager import ShotgunFieldManager
from .label_base_widget import LabelBaseWidget


class DurationWidget(LabelBaseWidget):
    """
    Inherited from a :class:`~LabelBaseWidget`, this class is able to
    display a duration field value as returned by the Shotgun API.
    """

    pass

# wait to register duration field until display options for hours versus days
# and # of hours in a day are available to the API
# ShotgunFieldManager.register("duration", DurationWidget)
