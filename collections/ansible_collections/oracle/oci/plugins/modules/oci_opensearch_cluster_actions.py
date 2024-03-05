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
module: oci_opensearch_cluster_actions
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_opensearch_cluster_actions_module.html)
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
    from oci.opensearch import OpensearchClusterClient
    from oci.opensearch.models import BackupOpensearchClusterDetails
    from oci.opensearch.models import RestoreOpensearchClusterDetails
    from oci.opensearch.models import ResizeOpensearchClusterHorizontalDetails
    from oci.opensearch.models import ResizeOpensearchClusterVerticalDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OpensearchClusterActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        backup
        opensearch_cluster_restore
        resize_opensearch_cluster_horizontal
        resize_opensearch_cluster_vertical
    """

    @staticmethod
    def get_module_resource_id_param():
        return "opensearch_cluster_id"

    def get_module_resource_id(self):
        return self.module.params.get("opensearch_cluster_id")

    def get_get_fn(self):
        return self.client.get_opensearch_cluster

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_opensearch_cluster,
            opensearch_cluster_id=self.module.params.get("opensearch_cluster_id"),
        )

    def backup(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, BackupOpensearchClusterDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.backup_opensearch_cluster,
            call_fn_args=(),
            call_fn_kwargs=dict(
                opensearch_cluster_id=self.module.params.get("opensearch_cluster_id"),
                backup_opensearch_cluster_details=action_details,
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

    def opensearch_cluster_restore(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RestoreOpensearchClusterDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.opensearch_cluster_restore,
            call_fn_args=(),
            call_fn_kwargs=dict(
                opensearch_cluster_id=self.module.params.get("opensearch_cluster_id"),
                restore_opensearch_cluster_details=action_details,
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

    def resize_opensearch_cluster_horizontal(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ResizeOpensearchClusterHorizontalDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.resize_opensearch_cluster_horizontal,
            call_fn_args=(),
            call_fn_kwargs=dict(
                opensearch_cluster_id=self.module.params.get("opensearch_cluster_id"),
                resize_opensearch_cluster_horizontal_details=action_details,
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

    def resize_opensearch_cluster_vertical(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ResizeOpensearchClusterVerticalDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.resize_opensearch_cluster_vertical,
            call_fn_args=(),
            call_fn_kwargs=dict(
                opensearch_cluster_id=self.module.params.get("opensearch_cluster_id"),
                resize_opensearch_cluster_vertical_details=action_details,
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


OpensearchClusterActionsHelperCustom = get_custom_class(
    "OpensearchClusterActionsHelperCustom"
)


class ResourceHelper(
    OpensearchClusterActionsHelperCustom, OpensearchClusterActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            display_name=dict(aliases=["name"], type="str"),
            opensearch_cluster_backup_id=dict(type="str"),
            compartment_id=dict(type="str"),
            prefix=dict(type="str"),
            master_node_count=dict(type="int"),
            data_node_count=dict(type="int"),
            opendashboard_node_count=dict(type="int"),
            opensearch_cluster_id=dict(aliases=["id"], type="str", required=True),
            master_node_host_ocpu_count=dict(type="int"),
            master_node_host_memory_gb=dict(type="int"),
            data_node_host_ocpu_count=dict(type="int"),
            data_node_host_memory_gb=dict(type="int"),
            data_node_storage_gb=dict(type="int"),
            opendashboard_node_host_ocpu_count=dict(type="int"),
            opendashboard_node_host_memory_gb=dict(type="int"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "backup",
                    "opensearch_cluster_restore",
                    "resize_opensearch_cluster_horizontal",
                    "resize_opensearch_cluster_vertical",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="opensearch_cluster",
        service_client_class=OpensearchClusterClient,
        namespace="opensearch",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
