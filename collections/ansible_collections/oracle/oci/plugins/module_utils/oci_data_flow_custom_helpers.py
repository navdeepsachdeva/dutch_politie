# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

try:
    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataFlowRunHelperCustom:
    def get_optional_kwargs_for_list(self):
        optional_kwargs_for_list = super(
            DataFlowRunHelperCustom, self
        ).get_optional_kwargs_for_list()

        # it is not allowed to specify display_name and application ID in the same list call, so if this
        # happens, prefer application_id
        if (
            "display_name" in optional_kwargs_for_list
            and "application_id" in optional_kwargs_for_list
        ):
            del optional_kwargs_for_list["display_name"]

        return optional_kwargs_for_list


class DataFlowApplicationHelperCustom:
    def get_optional_kwargs_for_list(self):
        optional_kwargs_for_list = super(
            DataFlowApplicationHelperCustom, self
        ).get_optional_kwargs_for_list()

        # it is not allowed to specify both display_name and spark_version together in the same list call.
        # So, if this happens, we prefer display_name
        if (
            "display_name" in optional_kwargs_for_list
            and "spark_version" in optional_kwargs_for_list
        ):
            del optional_kwargs_for_list["spark_version"]
        return optional_kwargs_for_list
