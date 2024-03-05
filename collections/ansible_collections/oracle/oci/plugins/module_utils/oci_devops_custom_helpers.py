# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class DevopsConnectionHelperCustom:
    # API throws an error when we pass connection_type value.
    def get_optional_kwargs_for_list(self):
        optional_list_method_params = super(
            DevopsConnectionHelperCustom, self
        ).get_optional_kwargs_for_list()
        optional_list_method_params.pop("connection_type", None)
        return optional_list_method_params


class DevopsConnectionActionsHelperCustom:
    def get_action_desired_states(self, action):
        action_desired_states = super(
            DevopsConnectionActionsHelperCustom, self
        ).get_action_desired_states(action)

        if action.lower() == "validate":
            return action_desired_states + [
                "ACTIVE",
            ]
        return action_desired_states


class DevopsBuildRunHelperCustom:
    # Running a build is not an idempotent operation. It is perfectly valid
    # to run the build multiple times.
    def get_matching_resource(self):
        return None
