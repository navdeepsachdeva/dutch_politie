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
module: oci_data_safe_alert_analytics_facts
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_data_safe_alert_analytics_facts_module.html)
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
    from oci.data_safe import DataSafeClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataSafeAlertAnalyticsFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id_in_subtree",
            "time_started",
            "time_ended",
            "query_time_zone",
            "sort_order",
            "sort_by",
            "access_level",
            "scim_query",
            "summary_field",
            "group_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_alert_analytics,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


DataSafeAlertAnalyticsFactsHelperCustom = get_custom_class(
    "DataSafeAlertAnalyticsFactsHelperCustom"
)


class ResourceFactsHelper(
    DataSafeAlertAnalyticsFactsHelperCustom, DataSafeAlertAnalyticsFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            compartment_id_in_subtree=dict(type="bool"),
            time_started=dict(type="str"),
            time_ended=dict(type="str"),
            query_time_zone=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["displayName", "timeCreated"]),
            access_level=dict(type="str", choices=["RESTRICTED", "ACCESSIBLE"]),
            scim_query=dict(type="str"),
            summary_field=dict(
                type="list",
                elements="str",
                choices=[
                    "alertType",
                    "targetIds",
                    "targetNames",
                    "alertSeverity",
                    "alertStatus",
                    "timeCreated",
                    "policyId",
                    "open",
                    "closed",
                    "critical",
                    "high",
                    "medium",
                    "low",
                    "alertcount",
                ],
            ),
            group_by=dict(
                type="list",
                elements="str",
                choices=[
                    "alertType",
                    "targetIds",
                    "targetNames",
                    "alertSeverity",
                    "alertStatus",
                    "timeCreated",
                    "policyId",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="alert_analytics",
        service_client_class=DataSafeClient,
        namespace="data_safe",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(alert_analytics=result)


if __name__ == "__main__":
    main()
