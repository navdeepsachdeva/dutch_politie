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
module: oci_autoscaling_auto_scaling_configuration_policy
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_autoscaling_auto_scaling_configuration_policy_module.html)
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
    from oci.autoscaling import AutoScalingClient
    from oci.autoscaling.models import UpdateAutoScalingPolicyDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AutoScalingConfigurationPolicyHelperGen(OCIResourceHelperBase):
    """Supported operations: update, get and list"""

    def get_possible_entity_types(self):
        return super(
            AutoScalingConfigurationPolicyHelperGen, self
        ).get_possible_entity_types() + [
            "autoscalingconfigurationpolicy",
            "autoscalingconfigurationpolicies",
            "autoscalingautoscalingconfigurationpolicy",
            "autoscalingautoscalingconfigurationpolicies",
            "autoscalingconfigurationpolicyresource",
            "autoscalingconfigurationpoliciesresource",
            "policy",
            "policies",
            "autoscalingpolicy",
            "autoscalingpolicies",
            "policyresource",
            "policiesresource",
            "autoscaling",
        ]

    def get_module_resource_id_param(self):
        return "auto_scaling_policy_id"

    def get_module_resource_id(self):
        return self.module.params.get("auto_scaling_policy_id")

    def get_get_fn(self):
        return self.client.get_auto_scaling_policy

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_auto_scaling_policy,
            auto_scaling_policy_id=summary_model.id,
            auto_scaling_configuration_id=self.module.params.get(
                "auto_scaling_configuration_id"
            ),
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_auto_scaling_policy,
            auto_scaling_configuration_id=self.module.params.get(
                "auto_scaling_configuration_id"
            ),
            auto_scaling_policy_id=self.module.params.get("auto_scaling_policy_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "auto_scaling_configuration_id",
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
            self.client.list_auto_scaling_policies, **kwargs
        )

    def get_update_model_class(self):
        return UpdateAutoScalingPolicyDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_auto_scaling_policy,
            call_fn_args=(),
            call_fn_kwargs=dict(
                auto_scaling_configuration_id=self.module.params.get(
                    "auto_scaling_configuration_id"
                ),
                auto_scaling_policy_id=self.module.params.get("auto_scaling_policy_id"),
                update_auto_scaling_policy_details=update_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )


AutoScalingConfigurationPolicyHelperCustom = get_custom_class(
    "AutoScalingConfigurationPolicyHelperCustom"
)


class ResourceHelper(
    AutoScalingConfigurationPolicyHelperCustom, AutoScalingConfigurationPolicyHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            auto_scaling_configuration_id=dict(type="str", required=True),
            auto_scaling_policy_id=dict(aliases=["id"], type="str"),
            rules=dict(
                type="list",
                elements="dict",
                options=dict(
                    action=dict(
                        type="dict",
                        required=True,
                        options=dict(
                            type=dict(
                                type="str", required=True, choices=["CHANGE_COUNT_BY"]
                            ),
                            value=dict(type="int", required=True),
                        ),
                    ),
                    display_name=dict(aliases=["name"], type="str"),
                    metric=dict(
                        type="dict",
                        required=True,
                        options=dict(
                            metric_type=dict(
                                type="str",
                                required=True,
                                choices=["CPU_UTILIZATION", "MEMORY_UTILIZATION"],
                            ),
                            threshold=dict(
                                type="dict",
                                required=True,
                                options=dict(
                                    operator=dict(
                                        type="str",
                                        required=True,
                                        choices=["GT", "GTE", "LT", "LTE"],
                                    ),
                                    value=dict(type="int", required=True),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
            display_name=dict(aliases=["name"], type="str"),
            capacity=dict(
                type="dict",
                options=dict(
                    max=dict(type="int"), min=dict(type="int"), initial=dict(type="int")
                ),
            ),
            policy_type=dict(
                type="str", required=True, choices=["threshold", "scheduled"]
            ),
            is_enabled=dict(type="bool"),
            execution_schedule=dict(
                type="dict",
                options=dict(
                    type=dict(type="str", required=True, choices=["cron"]),
                    timezone=dict(type="str", required=True, choices=["UTC"]),
                    expression=dict(type="str", required=True),
                ),
            ),
            resource_action=dict(
                type="dict",
                options=dict(
                    action_type=dict(type="str", required=True, choices=["power"]),
                    action=dict(
                        type="str",
                        required=True,
                        choices=["STOP", "START", "SOFTRESET", "RESET"],
                    ),
                ),
            ),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="auto_scaling_configuration_policy",
        service_client_class=AutoScalingClient,
        namespace="autoscaling",
    )

    result = dict(changed=False)

    if resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
