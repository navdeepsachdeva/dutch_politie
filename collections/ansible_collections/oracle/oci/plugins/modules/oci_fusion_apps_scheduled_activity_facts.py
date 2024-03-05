#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.
# GENERATED FILE - DO NOT EDIT - MANUAL CHANGES WILL BE OVERWRITTEN


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_fusion_apps_scheduled_activity_facts
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_fusion_apps_scheduled_activity_facts_module.html)
    for the module documentation.
author: Oracle (@oracle)
"""


from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.fusion_apps import FusionApplicationsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ScheduledActivityFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "fusion_environment_id",
            "scheduled_activity_id",
        ]

    def get_required_params_for_list(self):
        return [
            "fusion_environment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_scheduled_activity,
            fusion_environment_id=self.module.params.get("fusion_environment_id"),
            scheduled_activity_id=self.module.params.get("scheduled_activity_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "time_scheduled_start_greater_than_or_equal_to",
            "time_expected_finish_less_than_or_equal_to",
            "run_cycle",
            "lifecycle_state",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_scheduled_activities,
            fusion_environment_id=self.module.params.get("fusion_environment_id"),
            **optional_kwargs
        )


ScheduledActivityFactsHelperCustom = get_custom_class(
    "ScheduledActivityFactsHelperCustom"
)


class ResourceFactsHelper(
    ScheduledActivityFactsHelperCustom, ScheduledActivityFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            scheduled_activity_id=dict(aliases=["id"], type="str"),
            fusion_environment_id=dict(type="str", required=True),
            display_name=dict(aliases=["name"], type="str"),
            time_scheduled_start_greater_than_or_equal_to=dict(type="str"),
            time_expected_finish_less_than_or_equal_to=dict(type="str"),
            run_cycle=dict(
                type="str", choices=["QUARTERLY", "MONTHLY", "ONEOFF", "VERTEX"]
            ),
            lifecycle_state=dict(
                type="str",
                choices=["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["TIME_CREATED", "DISPLAY_NAME"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="scheduled_activity",
        service_client_class=FusionApplicationsClient,
        namespace="fusion_apps",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(scheduled_activities=result)


if __name__ == "__main__":
    main()
