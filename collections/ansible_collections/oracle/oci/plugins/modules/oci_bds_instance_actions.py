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
module: oci_bds_instance_actions
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_bds_instance_actions_module.html)
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
    from oci.bds import BdsClient
    from oci.bds.models import AddBlockStorageDetails
    from oci.bds.models import AddCloudSqlDetails
    from oci.bds.models import AddKafkaDetails
    from oci.bds.models import AddMasterNodesDetails
    from oci.bds.models import AddUtilityNodesDetails
    from oci.bds.models import AddWorkerNodesDetails
    from oci.bds.models import CertificateServiceInfoDetails
    from oci.bds.models import ChangeBdsInstanceCompartmentDetails
    from oci.bds.models import ChangeShapeDetails
    from oci.bds.models import DisableCertificateDetails
    from oci.bds.models import EnableCertificateDetails
    from oci.bds.models import ExecuteBootstrapScriptDetails
    from oci.bds.models import InstallOsPatchDetails
    from oci.bds.models import InstallPatchDetails
    from oci.bds.models import RemoveCloudSqlDetails
    from oci.bds.models import RemoveKafkaDetails
    from oci.bds.models import RemoveNodeDetails
    from oci.bds.models import RenewCertificateDetails
    from oci.bds.models import RestartNodeDetails
    from oci.bds.models import StartBdsInstanceDetails
    from oci.bds.models import StopBdsInstanceDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BdsInstanceActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        add_block_storage
        add_cloud_sql
        add_kafka
        add_master_nodes
        add_utility_nodes
        add_worker_nodes
        certificate_service_info
        change_compartment
        change_shape
        disable_certificate
        enable_certificate
        execute_bootstrap_script
        get_os_patch_details
        install_os_patch
        install_patch
        list_os_patches
        remove_cloud_sql
        remove_kafka
        remove_node
        renew_certificate
        restart_node
        start
        stop
    """

    @staticmethod
    def get_module_resource_id_param():
        return "bds_instance_id"

    def get_module_resource_id(self):
        return self.module.params.get("bds_instance_id")

    def get_get_fn(self):
        return self.client.get_bds_instance

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_bds_instance,
            bds_instance_id=self.module.params.get("bds_instance_id"),
        )

    def get_response_field_name(self, action):
        response_fields = dict(
            stop="bds_instance",
            start="bds_instance",
            add_block_storage="bds_instance",
            add_cloud_sql="bds_instance",
            add_kafka="bds_instance",
            add_master_nodes="bds_instance",
            add_utility_nodes="bds_instance",
            add_worker_nodes="bds_instance",
            certificate_service_info="certificate_service_info_summary",
            change_shape="bds_instance",
            disable_certificate="bds_instance",
            enable_certificate="bds_instance",
            execute_bootstrap_script="bds_instance",
            get_os_patch_details="os_patch_details",
            install_os_patch="bds_instance",
            install_patch="bds_instance",
            list_os_patches="os_patch_summary",
            remove_cloud_sql="bds_instance",
            remove_kafka="bds_instance",
            remove_node="bds_instance",
            renew_certificate="bds_instance",
            restart_node="bds_instance",
            change_compartment="bds_instance",
        )
        return response_fields.get(action, "bds_instance")

    def add_block_storage(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AddBlockStorageDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.add_block_storage,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                add_block_storage_details=action_details,
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

    def add_cloud_sql(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AddCloudSqlDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.add_cloud_sql,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                add_cloud_sql_details=action_details,
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

    def add_kafka(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AddKafkaDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.add_kafka,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                add_kafka_details=action_details,
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

    def add_master_nodes(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AddMasterNodesDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.add_master_nodes,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                add_master_nodes_details=action_details,
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

    def add_utility_nodes(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AddUtilityNodesDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.add_utility_nodes,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                add_utility_nodes_details=action_details,
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

    def add_worker_nodes(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AddWorkerNodesDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.add_worker_nodes,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                add_worker_nodes_details=action_details,
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

    def certificate_service_info(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, CertificateServiceInfoDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.certificate_service_info,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                certificate_service_info_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeBdsInstanceCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_bds_instance_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                change_bds_instance_compartment_details=action_details,
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

    def change_shape(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeShapeDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_shape,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                change_shape_details=action_details,
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

    def disable_certificate(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, DisableCertificateDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.disable_certificate,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                disable_certificate_details=action_details,
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

    def enable_certificate(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, EnableCertificateDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.enable_certificate,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                enable_certificate_details=action_details,
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

    def execute_bootstrap_script(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ExecuteBootstrapScriptDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.execute_bootstrap_script,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                execute_bootstrap_script_details=action_details,
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

    def get_os_patch_details(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.get_os_patch_details,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                os_patch_version=self.module.params.get("os_patch_version"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def install_os_patch(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, InstallOsPatchDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.install_os_patch,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                install_os_patch_details=action_details,
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

    def install_patch(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, InstallPatchDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.install_patch,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                install_patch_details=action_details,
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

    def list_os_patches(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.list_os_patches,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                sort_by=self.module.params.get("sort_by"),
                sort_order=self.module.params.get("sort_order"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def remove_cloud_sql(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RemoveCloudSqlDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_cloud_sql,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                remove_cloud_sql_details=action_details,
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

    def remove_kafka(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RemoveKafkaDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_kafka,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                remove_kafka_details=action_details,
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

    def remove_node(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RemoveNodeDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_node,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                remove_node_details=action_details,
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

    def renew_certificate(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RenewCertificateDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.renew_certificate,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                renew_certificate_details=action_details,
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

    def restart_node(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RestartNodeDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.restart_node,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                restart_node_details=action_details,
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

    def start(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, StartBdsInstanceDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.start_bds_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                start_bds_instance_details=action_details,
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

    def stop(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, StopBdsInstanceDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.stop_bds_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                stop_bds_instance_details=action_details,
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


BdsInstanceActionsHelperCustom = get_custom_class("BdsInstanceActionsHelperCustom")


class ResourceHelper(BdsInstanceActionsHelperCustom, BdsInstanceActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            number_of_kafka_nodes=dict(type="int"),
            number_of_master_nodes=dict(type="int"),
            number_of_utility_nodes=dict(type="int"),
            number_of_worker_nodes=dict(type="int"),
            node_type=dict(
                type="str",
                choices=["WORKER", "COMPUTE_ONLY_WORKER", "KAFKA_BROKER", "EDGE"],
            ),
            shape=dict(type="str"),
            block_volume_size_in_gbs=dict(type="int"),
            shape_config=dict(
                type="dict",
                options=dict(
                    ocpus=dict(type="int"),
                    memory_in_gbs=dict(type="int"),
                    nvmes=dict(type="int"),
                ),
            ),
            compartment_id=dict(type="str"),
            nodes=dict(
                type="dict",
                options=dict(
                    worker=dict(type="str"),
                    worker_shape_config=dict(
                        type="dict",
                        options=dict(
                            ocpus=dict(type="int"),
                            memory_in_gbs=dict(type="int"),
                            nvmes=dict(type="int"),
                        ),
                    ),
                    compute_only_worker=dict(type="str"),
                    compute_only_worker_shape_config=dict(
                        type="dict",
                        options=dict(
                            ocpus=dict(type="int"),
                            memory_in_gbs=dict(type="int"),
                            nvmes=dict(type="int"),
                        ),
                    ),
                    master=dict(type="str"),
                    master_shape_config=dict(
                        type="dict",
                        options=dict(
                            ocpus=dict(type="int"),
                            memory_in_gbs=dict(type="int"),
                            nvmes=dict(type="int"),
                        ),
                    ),
                    utility=dict(type="str"),
                    utility_shape_config=dict(
                        type="dict",
                        options=dict(
                            ocpus=dict(type="int"),
                            memory_in_gbs=dict(type="int"),
                            nvmes=dict(type="int"),
                        ),
                    ),
                    cloudsql=dict(type="str"),
                    cloudsql_shape_config=dict(
                        type="dict",
                        options=dict(
                            ocpus=dict(type="int"),
                            memory_in_gbs=dict(type="int"),
                            nvmes=dict(type="int"),
                        ),
                    ),
                    edge=dict(type="str"),
                    edge_shape_config=dict(
                        type="dict",
                        options=dict(
                            ocpus=dict(type="int"),
                            memory_in_gbs=dict(type="int"),
                            nvmes=dict(type="int"),
                        ),
                    ),
                    kafka_broker=dict(type="str"),
                    kafka_broker_shape_config=dict(
                        type="dict",
                        options=dict(
                            ocpus=dict(type="int"),
                            memory_in_gbs=dict(type="int"),
                            nvmes=dict(type="int"),
                        ),
                    ),
                ),
            ),
            bootstrap_script_url=dict(type="str"),
            os_patch_version=dict(type="str"),
            version=dict(type="str"),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            is_force_remove_enabled=dict(type="bool"),
            services=dict(type="list", elements="str"),
            root_certificate=dict(type="str"),
            host_cert_details=dict(
                type="list",
                elements="dict",
                options=dict(
                    host_name=dict(type="str", required=True),
                    certificate=dict(type="str", required=True),
                    private_key=dict(type="str", required=True, no_log=True),
                ),
            ),
            server_key_password=dict(type="str", no_log=True),
            node_id=dict(type="str"),
            bds_instance_id=dict(aliases=["id"], type="str", required=True),
            is_force_stop_jobs=dict(type="bool"),
            cluster_admin_password=dict(type="str", no_log=True),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "add_block_storage",
                    "add_cloud_sql",
                    "add_kafka",
                    "add_master_nodes",
                    "add_utility_nodes",
                    "add_worker_nodes",
                    "certificate_service_info",
                    "change_compartment",
                    "change_shape",
                    "disable_certificate",
                    "enable_certificate",
                    "execute_bootstrap_script",
                    "get_os_patch_details",
                    "install_os_patch",
                    "install_patch",
                    "list_os_patches",
                    "remove_cloud_sql",
                    "remove_kafka",
                    "remove_node",
                    "renew_certificate",
                    "restart_node",
                    "start",
                    "stop",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="bds_instance",
        service_client_class=BdsClient,
        namespace="bds",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
