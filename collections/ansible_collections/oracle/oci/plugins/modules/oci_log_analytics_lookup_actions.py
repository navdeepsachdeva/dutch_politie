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
module: oci_log_analytics_lookup_actions
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_log_analytics_lookup_actions_module.html)
    for the module documentation.
author: Oracle (@oracle)
"""


from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.log_analytics import LogAnalyticsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class LogAnalyticsLookupActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        append_lookup_data
        update_lookup_data
    """

    @staticmethod
    def get_module_resource_id_param():
        return "lookup_name"

    def get_module_resource_id(self):
        return self.module.params.get("lookup_name")

    def get_get_fn(self):
        return self.client.get_lookup

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_lookup,
            namespace_name=self.module.params.get("namespace_name"),
            lookup_name=self.module.params.get("lookup_name"),
        )

    def append_lookup_data(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.append_lookup_data,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                lookup_name=self.module.params.get("lookup_name"),
                append_lookup_file_body=self.module.params.get(
                    "append_lookup_file_body"
                ),
                is_force=self.module.params.get("is_force"),
                char_encoding=self.module.params.get("char_encoding"),
                expect=self.module.params.get("expect"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def update_lookup_data(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_lookup_data,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                lookup_name=self.module.params.get("lookup_name"),
                update_lookup_file_body=self.module.params.get(
                    "update_lookup_file_body"
                ),
                is_force=self.module.params.get("is_force"),
                char_encoding=self.module.params.get("char_encoding"),
                expect=self.module.params.get("expect"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


LogAnalyticsLookupActionsHelperCustom = get_custom_class(
    "LogAnalyticsLookupActionsHelperCustom"
)


class ResourceHelper(
    LogAnalyticsLookupActionsHelperCustom, LogAnalyticsLookupActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            append_lookup_file_body=dict(type="str"),
            namespace_name=dict(type="str", required=True),
            lookup_name=dict(type="str", required=True),
            update_lookup_file_body=dict(type="str"),
            is_force=dict(type="bool"),
            char_encoding=dict(type="str"),
            expect=dict(type="str"),
            action=dict(
                type="str",
                required=True,
                choices=["append_lookup_data", "update_lookup_data"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="log_analytics_lookup",
        service_client_class=LogAnalyticsClient,
        namespace="log_analytics",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
