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
module: oci_container_engine_node_pool
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_container_engine_node_pool_module.html)
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
    from oci.container_engine import ContainerEngineClient
    from oci.container_engine.models import CreateNodePoolDetails
    from oci.container_engine.models import UpdateNodePoolDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class NodePoolHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(NodePoolHelperGen, self).get_possible_entity_types() + [
            "nodepool",
            "nodepools",
            "containerEnginenodepool",
            "containerEnginenodepools",
            "nodepoolresource",
            "nodepoolsresource",
            "containerengine",
        ]

    def get_module_resource_id_param(self):
        return "node_pool_id"

    def get_module_resource_id(self):
        return self.module.params.get("node_pool_id")

    def get_get_fn(self):
        return self.client.get_node_pool

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_node_pool, node_pool_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_node_pool,
            node_pool_id=self.module.params.get("node_pool_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["cluster_id", "name"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_node_pools, **kwargs
        )

    def get_create_model_class(self):
        return CreateNodePoolDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_node_pool,
            call_fn_args=(),
            call_fn_kwargs=dict(create_node_pool_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateNodePoolDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_node_pool,
            call_fn_args=(),
            call_fn_kwargs=dict(
                node_pool_id=self.module.params.get("node_pool_id"),
                update_node_pool_details=update_details,
                override_eviction_grace_duration=self.module.params.get(
                    "override_eviction_grace_duration"
                ),
                is_force_deletion_after_override_grace_duration=self.module.params.get(
                    "is_force_deletion_after_override_grace_duration"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_node_pool,
            call_fn_args=(),
            call_fn_kwargs=dict(
                node_pool_id=self.module.params.get("node_pool_id"),
                override_eviction_grace_duration=self.module.params.get(
                    "override_eviction_grace_duration"
                ),
                is_force_deletion_after_override_grace_duration=self.module.params.get(
                    "is_force_deletion_after_override_grace_duration"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


NodePoolHelperCustom = get_custom_class("NodePoolHelperCustom")


class ResourceHelper(NodePoolHelperCustom, NodePoolHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            cluster_id=dict(type="str"),
            node_image_name=dict(type="str"),
            name=dict(type="str"),
            kubernetes_version=dict(type="str"),
            initial_node_labels=dict(
                type="list",
                elements="dict",
                options=dict(key=dict(type="str", no_log=True), value=dict(type="str")),
            ),
            quantity_per_subnet=dict(type="int"),
            subnet_ids=dict(type="list", elements="str"),
            node_config_details=dict(
                type="dict",
                options=dict(
                    size=dict(type="int"),
                    nsg_ids=dict(type="list", elements="str"),
                    kms_key_id=dict(type="str"),
                    is_pv_encryption_in_transit_enabled=dict(type="bool"),
                    freeform_tags=dict(type="dict"),
                    defined_tags=dict(type="dict"),
                    placement_configs=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            availability_domain=dict(type="str", required=True),
                            subnet_id=dict(type="str", required=True),
                            capacity_reservation_id=dict(type="str"),
                            preemptible_node_config=dict(
                                type="dict",
                                options=dict(
                                    preemption_action=dict(
                                        type="dict",
                                        required=True,
                                        options=dict(
                                            type=dict(
                                                type="str",
                                                required=True,
                                                choices=["TERMINATE"],
                                            ),
                                            is_preserve_boot_volume=dict(type="bool"),
                                        ),
                                    )
                                ),
                            ),
                            fault_domains=dict(type="list", elements="str"),
                        ),
                    ),
                    node_pool_pod_network_option_details=dict(
                        type="dict",
                        options=dict(
                            max_pods_per_node=dict(type="int"),
                            pod_nsg_ids=dict(type="list", elements="str"),
                            pod_subnet_ids=dict(type="list", elements="str"),
                            cni_type=dict(
                                type="str",
                                required=True,
                                choices=["OCI_VCN_IP_NATIVE", "FLANNEL_OVERLAY"],
                            ),
                        ),
                    ),
                ),
            ),
            node_metadata=dict(type="dict"),
            node_source_details=dict(
                type="dict",
                options=dict(
                    source_type=dict(type="str", required=True, choices=["IMAGE"]),
                    image_id=dict(type="str", required=True),
                    boot_volume_size_in_gbs=dict(type="int"),
                ),
            ),
            ssh_public_key=dict(type="str", no_log=True),
            node_shape=dict(type="str"),
            node_shape_config=dict(
                type="dict",
                options=dict(
                    ocpus=dict(type="float"), memory_in_gbs=dict(type="float")
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            node_eviction_node_pool_settings=dict(
                type="dict",
                options=dict(
                    eviction_grace_duration=dict(type="str"),
                    is_force_delete_after_grace_duration=dict(type="bool"),
                ),
            ),
            node_pool_cycling_details=dict(
                type="dict",
                options=dict(
                    maximum_unavailable=dict(type="str"),
                    maximum_surge=dict(type="str"),
                    is_node_cycling_enabled=dict(type="bool"),
                ),
            ),
            node_pool_id=dict(aliases=["id"], type="str"),
            override_eviction_grace_duration=dict(type="str"),
            is_force_deletion_after_override_grace_duration=dict(type="bool"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="node_pool",
        service_client_class=ContainerEngineClient,
        namespace="container_engine",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
