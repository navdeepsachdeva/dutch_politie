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
module: oci_log_analytics_lookup
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_log_analytics_lookup_module.html)
    for the module documentation.
author: Oracle (@oracle)
"""


from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.log_analytics import LogAnalyticsClient
    from oci.log_analytics.models import UpdateLookupMetadataDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class LogAnalyticsLookupHelperGen(OCIResourceHelperBase):
    """Supported operations: update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(LogAnalyticsLookupHelperGen, self).get_possible_entity_types() + [
            "loganalyticslookup",
            "loganalyticslookups",
            "logAnalyticsloganalyticslookup",
            "logAnalyticsloganalyticslookups",
            "loganalyticslookupresource",
            "loganalyticslookupsresource",
            "lookup",
            "lookups",
            "logAnalyticslookup",
            "logAnalyticslookups",
            "lookupresource",
            "lookupsresource",
            "loganalytics",
        ]

    def get_module_resource_id_param(self):
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

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "namespace_name",
            "type",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(self.client.list_lookups, **kwargs)

    def is_update(self):
        if not self.module.params.get("state") == "present":
            return False

        return self.does_resource_exist()

    def is_create(self):
        if not self.module.params.get("state") == "present":
            return False

        return not self.does_resource_exist()

    def get_update_model_class(self):
        return UpdateLookupMetadataDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_lookup,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                lookup_name=self.module.params.get("lookup_name"),
                update_lookup_metadata_details=update_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_lookup,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                lookup_name=self.module.params.get("lookup_name"),
                is_force=self.module.params.get("is_force"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


LogAnalyticsLookupHelperCustom = get_custom_class("LogAnalyticsLookupHelperCustom")


class ResourceHelper(LogAnalyticsLookupHelperCustom, LogAnalyticsLookupHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            default_match_value=dict(type="str"),
            description=dict(type="str"),
            fields=dict(
                type="list",
                elements="dict",
                options=dict(
                    common_field_name=dict(type="str"),
                    default_match_value=dict(type="str"),
                    display_name=dict(aliases=["name"], type="str"),
                    is_common_field=dict(type="bool"),
                    match_operator=dict(type="str"),
                    name=dict(type="str"),
                    position=dict(type="int"),
                ),
            ),
            max_matches=dict(type="int"),
            categories=dict(
                type="list",
                elements="dict",
                options=dict(
                    name=dict(type="str"),
                    description=dict(type="str"),
                    display_name=dict(aliases=["name"], type="str"),
                    type=dict(type="str"),
                    is_system=dict(type="bool"),
                ),
            ),
            namespace_name=dict(type="str", required=True),
            lookup_name=dict(type="str", required=True),
            is_force=dict(type="bool"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
