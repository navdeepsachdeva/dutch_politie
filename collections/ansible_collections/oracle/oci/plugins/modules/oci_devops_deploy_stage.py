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
module: oci_devops_deploy_stage
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_devops_deploy_stage_module.html)
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
    from oci.devops import DevopsClient
    from oci.devops.models import CreateDeployStageDetails
    from oci.devops.models import UpdateDeployStageDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DevopsDeployStageHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(DevopsDeployStageHelperGen, self).get_possible_entity_types() + [
            "devopsdeploystage",
            "devopsdeploystages",
            "devopsdevopsdeploystage",
            "devopsdevopsdeploystages",
            "devopsdeploystageresource",
            "devopsdeploystagesresource",
            "deploystage",
            "deploystages",
            "deploystageresource",
            "deploystagesresource",
            "devops",
        ]

    def get_module_resource_id_param(self):
        return "deploy_stage_id"

    def get_module_resource_id(self):
        return self.module.params.get("deploy_stage_id")

    def get_get_fn(self):
        return self.client.get_deploy_stage

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_deploy_stage, deploy_stage_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_deploy_stage,
            deploy_stage_id=self.module.params.get("deploy_stage_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["deploy_pipeline_id", "display_name"]

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
            self.client.list_deploy_stages, **kwargs
        )

    def get_create_model_class(self):
        return CreateDeployStageDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_deploy_stage,
            call_fn_args=(),
            call_fn_kwargs=dict(create_deploy_stage_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateDeployStageDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_deploy_stage,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deploy_stage_id=self.module.params.get("deploy_stage_id"),
                update_deploy_stage_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_deploy_stage,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deploy_stage_id=self.module.params.get("deploy_stage_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DevopsDeployStageHelperCustom = get_custom_class("DevopsDeployStageHelperCustom")


class ResourceHelper(DevopsDeployStageHelperCustom, DevopsDeployStageHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            oke_canary_deploy_stage_id=dict(type="str"),
            oke_blue_green_deploy_stage_id=dict(type="str"),
            compute_instance_group_blue_green_deployment_deploy_stage_id=dict(
                type="str"
            ),
            blue_green_strategy=dict(
                type="dict",
                options=dict(
                    strategy_type=dict(
                        type="str", required=True, choices=["NGINX_BLUE_GREEN_STRATEGY"]
                    ),
                    namespace_a=dict(type="str", required=True),
                    namespace_b=dict(type="str", required=True),
                    ingress_name=dict(type="str", required=True),
                ),
            ),
            canary_strategy=dict(
                type="dict",
                options=dict(
                    strategy_type=dict(
                        type="str", required=True, choices=["NGINX_CANARY_STRATEGY"]
                    ),
                    namespace=dict(type="str", required=True),
                    ingress_name=dict(type="str", required=True),
                ),
            ),
            compute_instance_group_canary_deploy_stage_id=dict(type="str"),
            compute_instance_group_canary_traffic_shift_deploy_stage_id=dict(
                type="str"
            ),
            deploy_environment_id_a=dict(type="str"),
            deploy_environment_id_b=dict(type="str"),
            production_load_balancer_config=dict(
                type="dict",
                options=dict(
                    load_balancer_id=dict(type="str", required=True),
                    listener_name=dict(type="str", required=True),
                    backend_port=dict(type="int"),
                ),
            ),
            deploy_pipeline_id=dict(type="str"),
            oke_canary_traffic_shift_deploy_stage_id=dict(type="str"),
            helm_chart_deploy_artifact_id=dict(type="str"),
            values_artifact_ids=dict(type="list", elements="str"),
            release_name=dict(type="str"),
            set_values=dict(
                type="dict",
                options=dict(
                    items=dict(
                        type="list",
                        elements="dict",
                        required=True,
                        options=dict(
                            name=dict(type="str", required=True),
                            value=dict(type="str", required=True),
                        ),
                    )
                ),
            ),
            set_string=dict(
                type="dict",
                options=dict(
                    items=dict(
                        type="list",
                        elements="dict",
                        required=True,
                        options=dict(
                            name=dict(type="str", required=True),
                            value=dict(type="str", required=True),
                        ),
                    )
                ),
            ),
            are_hooks_enabled=dict(type="bool"),
            should_reuse_values=dict(type="bool"),
            should_reset_values=dict(type="bool"),
            is_force_enabled=dict(type="bool"),
            should_cleanup_on_fail=dict(type="bool"),
            max_history=dict(type="int"),
            should_skip_crds=dict(type="bool"),
            should_skip_render_subchart_notes=dict(type="bool"),
            should_not_wait=dict(type="bool"),
            is_debug_enabled=dict(type="bool"),
            compute_instance_group_deploy_environment_id=dict(type="str"),
            container_config=dict(
                type="dict",
                options=dict(
                    container_config_type=dict(
                        type="str", required=True, choices=["CONTAINER_INSTANCE_CONFIG"]
                    ),
                    compartment_id=dict(type="str"),
                    availability_domain=dict(type="str"),
                    shape_name=dict(type="str", required=True),
                    shape_config=dict(
                        type="dict",
                        required=True,
                        options=dict(
                            ocpus=dict(type="float", required=True),
                            memory_in_gbs=dict(type="float"),
                        ),
                    ),
                    network_channel=dict(
                        type="dict",
                        required=True,
                        options=dict(
                            network_channel_type=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "SERVICE_VNIC_CHANNEL",
                                    "PRIVATE_ENDPOINT_CHANNEL",
                                ],
                            ),
                            subnet_id=dict(type="str", required=True),
                            nsg_ids=dict(type="list", elements="str"),
                        ),
                    ),
                ),
            ),
            command_spec_deploy_artifact_id=dict(type="str"),
            timeout_in_seconds=dict(type="int"),
            oke_cluster_deploy_environment_id=dict(type="str"),
            namespace=dict(type="str"),
            blue_backend_ips=dict(
                type="dict", options=dict(items=dict(type="list", elements="str"))
            ),
            green_backend_ips=dict(
                type="dict", options=dict(items=dict(type="list", elements="str"))
            ),
            traffic_shift_target=dict(type="str"),
            load_balancer_config=dict(
                type="dict",
                options=dict(
                    load_balancer_id=dict(type="str", required=True),
                    listener_name=dict(type="str", required=True),
                    backend_port=dict(type="int"),
                ),
            ),
            rollback_policy=dict(
                type="dict",
                options=dict(
                    policy_type=dict(
                        type="str",
                        required=True,
                        choices=[
                            "NO_STAGE_ROLLBACK_POLICY",
                            "AUTOMATED_STAGE_ROLLBACK_POLICY",
                        ],
                    )
                ),
            ),
            kubernetes_manifest_deploy_artifact_ids=dict(type="list", elements="str"),
            wait_criteria=dict(
                type="dict",
                options=dict(
                    wait_type=dict(
                        type="str", required=True, choices=["ABSOLUTE_WAIT"]
                    ),
                    wait_duration=dict(type="str", required=True),
                ),
            ),
            approval_policy=dict(
                type="dict",
                options=dict(
                    approval_policy_type=dict(
                        type="str", required=True, choices=["COUNT_BASED_APPROVAL"]
                    ),
                    number_of_approvals_required=dict(type="int", required=True),
                ),
            ),
            failure_policy=dict(
                type="dict",
                options=dict(
                    failure_percentage=dict(type="int"),
                    policy_type=dict(
                        type="str",
                        required=True,
                        choices=[
                            "COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_PERCENTAGE",
                            "COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_COUNT",
                        ],
                    ),
                    failure_count=dict(type="int"),
                ),
            ),
            deployment_spec_deploy_artifact_id=dict(type="str"),
            deploy_artifact_ids=dict(type="list", elements="str"),
            test_load_balancer_config=dict(
                type="dict",
                options=dict(
                    load_balancer_id=dict(type="str", required=True),
                    listener_name=dict(type="str", required=True),
                    backend_port=dict(type="int"),
                ),
            ),
            docker_image_deploy_artifact_id=dict(type="str"),
            config=dict(type="dict"),
            max_memory_in_mbs=dict(type="int"),
            function_timeout_in_seconds=dict(type="int"),
            rollout_policy=dict(
                type="dict",
                options=dict(
                    ramp_limit_percent=dict(type="float"),
                    batch_percentage=dict(type="int"),
                    policy_type=dict(
                        type="str",
                        choices=[
                            "COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE",
                            "COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_COUNT",
                        ],
                    ),
                    batch_delay_in_seconds=dict(type="int"),
                    batch_count=dict(type="int"),
                ),
            ),
            description=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            deploy_stage_type=dict(
                type="str",
                choices=[
                    "OKE_CANARY_TRAFFIC_SHIFT",
                    "OKE_BLUE_GREEN_TRAFFIC_SHIFT",
                    "COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT",
                    "WAIT",
                    "LOAD_BALANCER_TRAFFIC_SHIFT",
                    "SHELL",
                    "COMPUTE_INSTANCE_GROUP_BLUE_GREEN_TRAFFIC_SHIFT",
                    "OKE_BLUE_GREEN_DEPLOYMENT",
                    "COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT",
                    "INVOKE_FUNCTION",
                    "DEPLOY_FUNCTION",
                    "OKE_CANARY_DEPLOYMENT",
                    "COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT",
                    "COMPUTE_INSTANCE_GROUP_CANARY_APPROVAL",
                    "OKE_HELM_CHART_DEPLOYMENT",
                    "MANUAL_APPROVAL",
                    "OKE_DEPLOYMENT",
                    "COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT",
                    "OKE_CANARY_APPROVAL",
                ],
            ),
            deploy_stage_predecessor_collection=dict(
                type="dict",
                options=dict(
                    items=dict(
                        type="list",
                        elements="dict",
                        required=True,
                        options=dict(id=dict(type="str", required=True)),
                    )
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            function_deploy_environment_id=dict(type="str"),
            deploy_artifact_id=dict(type="str"),
            is_async=dict(type="bool"),
            is_validation_enabled=dict(type="bool"),
            deploy_stage_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="deploy_stage",
        service_client_class=DevopsClient,
        namespace="devops",
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
