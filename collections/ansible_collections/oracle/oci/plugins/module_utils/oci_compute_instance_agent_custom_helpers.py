# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class InstanceAgentCommandHelperCustom:
    # The create operation is not idempotent since it is valid to have multiple commands with the given
    # values and there is no way for us to distinguish if the user wants to create another or not.
    def get_matching_resource(self):
        return None
