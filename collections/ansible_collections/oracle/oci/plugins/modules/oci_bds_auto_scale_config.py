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
module: oci_bds_auto_scale_config
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_bds_auto_scale_config_module.html)
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
    from oci.bds import BdsClient
    from oci.bds.models import AddAutoScalingConfigurationDetails
    from oci.bds.models import UpdateAutoScalingConfigurationDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BdsAutoScaleConfigHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(BdsAutoScaleConfigHelperGen, self).get_possible_entity_types() + [
            "bdsautoscaleconfig",
            "bdsautoscaleconfigs",
            "bdsbdsautoscaleconfig",
            "bdsbdsautoscaleconfigs",
            "bdsautoscaleconfigresource",
            "bdsautoscaleconfigsresource",
            "autoscalingconfiguration",
            "autoscalingconfigurations",
            "bdsautoscalingconfiguration",
            "bdsautoscalingconfigurations",
            "autoscalingconfigurationresource",
            "autoscalingconfigurationsresource",
            "bds",
        ]

    def get_module_resource_id_param(self):
        return "auto_scaling_configuration_id"

    def get_module_resource_id(self):
        return self.module.params.get("auto_scaling_configuration_id")

    def get_get_fn(self):
        return self.client.get_auto_scaling_configuration

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_auto_scaling_configuration,
            auto_scaling_configuration_id=summary_model.id,
            bds_instance_id=self.module.params.get("bds_instance_id"),
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_auto_scaling_configuration,
            bds_instance_id=self.module.params.get("bds_instance_id"),
            auto_scaling_configuration_id=self.module.params.get(
                "auto_scaling_configuration_id"
            ),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
            "bds_instance_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name"]

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
            self.client.list_auto_scaling_configurations, **kwargs
        )

    def get_create_model_class(self):
        return AddAutoScalingConfigurationDetails

    def get_exclude_attributes(self):
        return ["is_enabled", "cluster_admin_password"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.add_auto_scaling_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                add_auto_scaling_configuration_details=create_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateAutoScalingConfigurationDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_auto_scaling_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                auto_scaling_configuration_id=self.module.params.get(
                    "auto_scaling_configuration_id"
                ),
                update_auto_scaling_configuration_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_auto_scaling_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                auto_scaling_configuration_id=self.module.params.get(
                    "auto_scaling_configuration_id"
                ),
                remove_auto_scaling_configuration_details=self.module.params.get(
                    "remove_auto_scaling_configuration_details"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


BdsAutoScaleConfigHelperCustom = get_custom_class("BdsAutoScaleConfigHelperCustom")


class ResourceHelper(BdsAutoScaleConfigHelperCustom, BdsAutoScaleConfigHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            node_type=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            is_enabled=dict(type="bool"),
            policy=dict(
                type="dict",
                options=dict(
                    policy_type=dict(
                        type="str",
                        required=True,
                        choices=["THRESHOLD_BASED", "SCHEDULE_BASED", "NONE"],
                    ),
                    rules=dict(
                        type="list",
                        elements="dict",
                        required=True,
                        options=dict(
                            action=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "CHANGE_SHAPE_SCALE_UP",
                                    "CHANGE_SHAPE_SCALE_DOWN",
                                ],
                            ),
                            metric=dict(
                                type="dict",
                                required=True,
                                options=dict(
                                    metric_type=dict(
                                        type="str",
                                        required=True,
                                        choices=["CPU_UTILIZATION"],
                                    ),
                                    threshold=dict(
                                        type="dict",
                                        required=True,
                                        options=dict(
                                            duration_in_minutes=dict(
                                                type="int", required=True
                                            ),
                                            operator=dict(
                                                type="str",
                                                required=True,
                                                choices=["GT", "LT"],
                                            ),
                                            value=dict(type="int", required=True),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
            policy_details=dict(
                type="dict",
                options=dict(
                    scale_up_config=dict(
                        type="dict",
                        options=dict(
                            metric=dict(
                                type="dict",
                                options=dict(
                                    metric_type=dict(
                                        type="str",
                                        required=True,
                                        choices=["CPU_UTILIZATION"],
                                    ),
                                    threshold=dict(
                                        type="dict",
                                        required=True,
                                        options=dict(
                                            duration_in_minutes=dict(
                                                type="int", required=True
                                            ),
                                            operator=dict(
                                                type="str",
                                                required=True,
                                                choices=["GT", "LT"],
                                            ),
                                            value=dict(type="int", required=True),
                                        ),
                                    ),
                                ),
                            ),
                            max_ocpus_per_node=dict(type="int"),
                            max_memory_per_node=dict(type="int"),
                            ocpu_step_size=dict(type="int"),
                            memory_step_size=dict(type="int"),
                        ),
                    ),
                    scale_down_config=dict(
                        type="dict",
                        options=dict(
                            metric=dict(
                                type="dict",
                                options=dict(
                                    metric_type=dict(
                                        type="str",
                                        required=True,
                                        choices=["CPU_UTILIZATION"],
                                    ),
                                    threshold=dict(
                                        type="dict",
                                        required=True,
                                        options=dict(
                                            duration_in_minutes=dict(
                                                type="int", required=True
                                            ),
                                            operator=dict(
                                                type="str",
                                                required=True,
                                                choices=["GT", "LT"],
                                            ),
                                            value=dict(type="int", required=True),
                                        ),
                                    ),
                                ),
                            ),
                            min_ocpus_per_node=dict(type="int"),
                            min_memory_per_node=dict(type="int"),
                            ocpu_step_size=dict(type="int"),
                            memory_step_size=dict(type="int"),
                        ),
                    ),
                    scale_out_config=dict(
                        type="dict",
                        options=dict(
                            metric=dict(
                                type="dict",
                                options=dict(
                                    metric_type=dict(
                                        type="str",
                                        required=True,
                                        choices=["CPU_UTILIZATION"],
                                    ),
                                    threshold=dict(
                                        type="dict",
                                        required=True,
                                        options=dict(
                                            duration_in_minutes=dict(
                                                type="int", required=True
                                            ),
                                            operator=dict(
                                                type="str",
                                                required=True,
                                                choices=["GT", "LT"],
                                            ),
                                            value=dict(type="int", required=True),
                                        ),
                                    ),
                                ),
                            ),
                            max_node_count=dict(type="int"),
                            step_size=dict(type="int"),
                        ),
                    ),
                    scale_in_config=dict(
                        type="dict",
                        options=dict(
                            metric=dict(
                                type="dict",
                                options=dict(
                                    metric_type=dict(
                                        type="str",
                                        required=True,
                                        choices=["CPU_UTILIZATION"],
                                    ),
                                    threshold=dict(
                                        type="dict",
                                        required=True,
                                        options=dict(
                                            duration_in_minutes=dict(
                                                type="int", required=True
                                            ),
                                            operator=dict(
                                                type="str",
                                                required=True,
                                                choices=["GT", "LT"],
                                            ),
                                            value=dict(type="int", required=True),
                                        ),
                                    ),
                                ),
                            ),
                            min_node_count=dict(type="int"),
                            step_size=dict(type="int"),
                        ),
                    ),
                    policy_type=dict(
                        type="str",
                        required=True,
                        choices=[
                            "METRIC_BASED_HORIZONTAL_SCALING_POLICY",
                            "SCHEDULE_BASED_VERTICAL_SCALING_POLICY",
                            "SCHEDULE_BASED_HORIZONTAL_SCALING_POLICY",
                            "METRIC_BASED_VERTICAL_SCALING_POLICY",
                        ],
                    ),
                    timezone=dict(type="str"),
                    schedule_details=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            time_and_horizontal_scaling_config=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    time_recurrence=dict(type="str"),
                                    target_node_count=dict(type="int"),
                                ),
                            ),
                            schedule_type=dict(
                                type="str", required=True, choices=["DAY_BASED"]
                            ),
                            time_and_vertical_scaling_config=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    time_recurrence=dict(type="str"),
                                    target_shape=dict(type="str"),
                                    target_ocpus_per_node=dict(type="int"),
                                    target_memory_per_node=dict(type="int"),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
            bds_instance_id=dict(type="str", required=True),
            auto_scaling_configuration_id=dict(aliases=["id"], type="str"),
            cluster_admin_password=dict(type="str", no_log=True),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="bds_auto_scale_config",
        service_client_class=BdsClient,
        namespace="bds",
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
