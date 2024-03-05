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
module: oci_log_analytics_entity_facts
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_log_analytics_entity_facts_module.html)
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
    from oci.log_analytics import LogAnalyticsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class LogAnalyticsEntityFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "namespace_name",
            "log_analytics_entity_id",
        ]

    def get_required_params_for_list(self):
        return [
            "namespace_name",
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_log_analytics_entity,
            namespace_name=self.module.params.get("namespace_name"),
            log_analytics_entity_id=self.module.params.get("log_analytics_entity_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "name",
            "name_contains",
            "entity_type_name",
            "cloud_resource_id",
            "lifecycle_state",
            "lifecycle_details_contains",
            "is_management_agent_id_null",
            "hostname",
            "hostname_contains",
            "source_id",
            "creation_source_type",
            "creation_source_details",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_log_analytics_entities,
            namespace_name=self.module.params.get("namespace_name"),
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


LogAnalyticsEntityFactsHelperCustom = get_custom_class(
    "LogAnalyticsEntityFactsHelperCustom"
)


class ResourceFactsHelper(
    LogAnalyticsEntityFactsHelperCustom, LogAnalyticsEntityFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            log_analytics_entity_id=dict(aliases=["id"], type="str"),
            namespace_name=dict(type="str", required=True),
            compartment_id=dict(type="str"),
            name=dict(type="str"),
            name_contains=dict(type="str"),
            entity_type_name=dict(type="list", elements="str"),
            cloud_resource_id=dict(type="str"),
            lifecycle_state=dict(type="str", choices=["ACTIVE", "DELETED"]),
            lifecycle_details_contains=dict(type="str"),
            is_management_agent_id_null=dict(type="str", choices=["true", "false"]),
            hostname=dict(type="str"),
            hostname_contains=dict(type="str"),
            source_id=dict(type="str"),
            creation_source_type=dict(
                type="list",
                elements="str",
                choices=[
                    "EM_BRIDGE",
                    "BULK_DISCOVERY",
                    "SERVICE_CONNECTOR_HUB",
                    "DISCOVERY",
                    "NONE",
                ],
            ),
            creation_source_details=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "timeUpdated", "name"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="log_analytics_entity",
        service_client_class=LogAnalyticsClient,
        namespace="log_analytics",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(log_analytics_entities=result)


if __name__ == "__main__":
    main()
