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
module: oci_container_engine_cluster
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_container_engine_cluster_module.html)
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
    from oci.container_engine.models import CreateClusterDetails
    from oci.container_engine.models import UpdateClusterDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ClusterHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_default_module_wait_timeout(self):
        return 1800

    def get_possible_entity_types(self):
        return super(ClusterHelperGen, self).get_possible_entity_types() + [
            "cluster",
            "clusters",
            "containerEnginecluster",
            "containerEngineclusters",
            "clusterresource",
            "clustersresource",
            "containerengine",
        ]

    def get_module_resource_id_param(self):
        return "cluster_id"

    def get_module_resource_id(self):
        return self.module.params.get("cluster_id")

    def get_get_fn(self):
        return self.client.get_cluster

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_cluster, cluster_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_cluster, cluster_id=self.module.params.get("cluster_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["name"]

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
        return oci_common_utils.list_all_resources(self.client.list_clusters, **kwargs)

    def get_create_model_class(self):
        return CreateClusterDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_cluster,
            call_fn_args=(),
            call_fn_kwargs=dict(create_cluster_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateClusterDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_cluster,
            call_fn_args=(),
            call_fn_kwargs=dict(
                cluster_id=self.module.params.get("cluster_id"),
                update_cluster_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_cluster,
            call_fn_args=(),
            call_fn_kwargs=dict(cluster_id=self.module.params.get("cluster_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ClusterHelperCustom = get_custom_class("ClusterHelperCustom")


class ResourceHelper(ClusterHelperCustom, ClusterHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            endpoint_config=dict(
                type="dict",
                options=dict(
                    subnet_id=dict(type="str"),
                    nsg_ids=dict(type="list", elements="str"),
                    is_public_ip_enabled=dict(type="bool"),
                ),
            ),
            vcn_id=dict(type="str"),
            kms_key_id=dict(type="str"),
            cluster_pod_network_options=dict(
                type="list",
                elements="dict",
                options=dict(
                    cni_type=dict(
                        type="str",
                        required=True,
                        choices=["FLANNEL_OVERLAY", "OCI_VCN_IP_NATIVE"],
                    )
                ),
            ),
            name=dict(type="str"),
            kubernetes_version=dict(type="str"),
            options=dict(
                type="dict",
                options=dict(
                    service_lb_subnet_ids=dict(type="list", elements="str"),
                    kubernetes_network_config=dict(
                        type="dict",
                        options=dict(
                            pods_cidr=dict(type="str"), services_cidr=dict(type="str")
                        ),
                    ),
                    add_ons=dict(
                        type="dict",
                        options=dict(
                            is_kubernetes_dashboard_enabled=dict(type="bool"),
                            is_tiller_enabled=dict(type="bool"),
                        ),
                    ),
                    admission_controller_options=dict(
                        type="dict",
                        options=dict(is_pod_security_policy_enabled=dict(type="bool")),
                    ),
                    persistent_volume_config=dict(
                        type="dict",
                        options=dict(
                            freeform_tags=dict(type="dict"),
                            defined_tags=dict(type="dict"),
                        ),
                    ),
                    service_lb_config=dict(
                        type="dict",
                        options=dict(
                            freeform_tags=dict(type="dict"),
                            defined_tags=dict(type="dict"),
                        ),
                    ),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            image_policy_config=dict(
                type="dict",
                options=dict(
                    is_policy_enabled=dict(type="bool"),
                    key_details=dict(
                        type="list",
                        elements="dict",
                        no_log=False,
                        options=dict(kms_key_id=dict(type="str")),
                    ),
                ),
            ),
            type=dict(type="str", choices=["BASIC_CLUSTER", "ENHANCED_CLUSTER"]),
            cluster_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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
