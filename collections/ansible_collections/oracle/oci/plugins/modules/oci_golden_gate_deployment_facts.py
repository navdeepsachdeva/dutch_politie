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
module: oci_golden_gate_deployment_facts
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_golden_gate_deployment_facts_module.html)
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
    from oci.golden_gate import GoldenGateClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DeploymentFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "deployment_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_deployment,
            deployment_id=self.module.params.get("deployment_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "supported_connection_type",
            "assigned_connection_id",
            "assignable_connection_id",
            "lifecycle_state",
            "lifecycle_sub_state",
            "display_name",
            "fqdn",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_deployments,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


DeploymentFactsHelperCustom = get_custom_class("DeploymentFactsHelperCustom")


class ResourceFactsHelper(DeploymentFactsHelperCustom, DeploymentFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            deployment_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            supported_connection_type=dict(
                type="str",
                choices=[
                    "GOLDENGATE",
                    "KAFKA",
                    "KAFKA_SCHEMA_REGISTRY",
                    "MYSQL",
                    "JAVA_MESSAGE_SERVICE",
                    "MICROSOFT_SQLSERVER",
                    "OCI_OBJECT_STORAGE",
                    "ORACLE",
                    "AZURE_DATA_LAKE_STORAGE",
                    "POSTGRESQL",
                    "AZURE_SYNAPSE_ANALYTICS",
                    "SNOWFLAKE",
                    "AMAZON_S3",
                    "HDFS",
                    "ORACLE_NOSQL",
                    "MONGODB",
                    "AMAZON_KINESIS",
                    "AMAZON_REDSHIFT",
                    "REDIS",
                    "ELASTICSEARCH",
                    "GENERIC",
                    "GOOGLE_CLOUD_STORAGE",
                    "GOOGLE_BIGQUERY",
                ],
            ),
            assigned_connection_id=dict(type="str"),
            assignable_connection_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "INACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                    "NEEDS_ATTENTION",
                    "IN_PROGRESS",
                    "CANCELING",
                    "CANCELED",
                    "SUCCEEDED",
                    "WAITING",
                ],
            ),
            lifecycle_sub_state=dict(
                type="str",
                choices=[
                    "RECOVERING",
                    "STARTING",
                    "STOPPING",
                    "MOVING",
                    "UPGRADING",
                    "RESTORING",
                    "BACKUP_IN_PROGRESS",
                    "ROLLBACK_IN_PROGRESS",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
            fqdn=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="deployment",
        service_client_class=GoldenGateClient,
        namespace="golden_gate",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(deployments=result)


if __name__ == "__main__":
    main()
