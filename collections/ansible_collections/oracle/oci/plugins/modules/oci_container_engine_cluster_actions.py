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
module: oci_container_engine_cluster_actions
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_container_engine_cluster_actions_module.html)
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
    from oci.container_engine import ContainerEngineClient
    from oci.container_engine.models import ClusterMigrateToNativeVcnDetails
    from oci.container_engine.models import StartCredentialRotationDetails
    from oci.container_engine.models import UpdateClusterEndpointConfigDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ClusterActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        cluster_migrate_to_native_vcn
        complete_credential_rotation
        start_credential_rotation
        update_cluster_endpoint_config
    """

    @staticmethod
    def get_module_resource_id_param():
        return "cluster_id"

    def get_module_resource_id(self):
        return self.module.params.get("cluster_id")

    def get_get_fn(self):
        return self.client.get_cluster

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_cluster, cluster_id=self.module.params.get("cluster_id"),
        )

    def cluster_migrate_to_native_vcn(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ClusterMigrateToNativeVcnDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.cluster_migrate_to_native_vcn,
            call_fn_args=(),
            call_fn_kwargs=dict(
                cluster_id=self.module.params.get("cluster_id"),
                cluster_migrate_to_native_vcn_details=action_details,
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

    def complete_credential_rotation(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.complete_credential_rotation,
            call_fn_args=(),
            call_fn_kwargs=dict(cluster_id=self.module.params.get("cluster_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def start_credential_rotation(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, StartCredentialRotationDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.start_credential_rotation,
            call_fn_args=(),
            call_fn_kwargs=dict(
                cluster_id=self.module.params.get("cluster_id"),
                start_credential_rotation_details=action_details,
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

    def update_cluster_endpoint_config(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, UpdateClusterEndpointConfigDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_cluster_endpoint_config,
            call_fn_args=(),
            call_fn_kwargs=dict(
                cluster_id=self.module.params.get("cluster_id"),
                update_cluster_endpoint_config_details=action_details,
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


ClusterActionsHelperCustom = get_custom_class("ClusterActionsHelperCustom")


class ResourceHelper(ClusterActionsHelperCustom, ClusterActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            endpoint_config=dict(
                type="dict",
                options=dict(
                    subnet_id=dict(type="str"),
                    nsg_ids=dict(type="list", elements="str"),
                    is_public_ip_enabled=dict(type="bool"),
                ),
            ),
            decommission_delay_duration=dict(type="str"),
            auto_completion_delay_duration=dict(type="str"),
            cluster_id=dict(aliases=["id"], type="str", required=True),
            nsg_ids=dict(type="list", elements="str"),
            is_public_ip_enabled=dict(type="bool"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "cluster_migrate_to_native_vcn",
                    "complete_credential_rotation",
                    "start_credential_rotation",
                    "update_cluster_endpoint_config",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="cluster",
        service_client_class=ContainerEngineClient,
        namespace="container_engine",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
