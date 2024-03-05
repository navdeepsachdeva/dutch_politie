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
module: oci_cloud_guard_target_detector_recipe
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_cloud_guard_target_detector_recipe_module.html)
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
    from oci.cloud_guard import CloudGuardClient
    from oci.cloud_guard.models import AttachTargetDetectorRecipeDetails
    from oci.cloud_guard.models import UpdateTargetDetectorRecipeDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TargetDetectorRecipeHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            TargetDetectorRecipeHelperGen, self
        ).get_possible_entity_types() + [
            "cloudguardtarget",
            "cloudguardtargets",
            "cloudGuardcloudguardtarget",
            "cloudGuardcloudguardtargets",
            "cloudguardtargetresource",
            "cloudguardtargetsresource",
            "targetdetectorrecipe",
            "targetdetectorrecipes",
            "cloudGuardtargetdetectorrecipe",
            "cloudGuardtargetdetectorrecipes",
            "targetdetectorreciperesource",
            "targetdetectorrecipesresource",
            "cloudguard",
        ]

    def get_module_resource_id_param(self):
        return "target_detector_recipe_id"

    def get_module_resource_id(self):
        return self.module.params.get("target_detector_recipe_id")

    def get_get_fn(self):
        return self.client.get_target_detector_recipe

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_target_detector_recipe,
            target_detector_recipe_id=summary_model.id,
            target_id=self.module.params.get("target_id"),
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_target_detector_recipe,
            target_id=self.module.params.get("target_id"),
            target_detector_recipe_id=self.module.params.get(
                "target_detector_recipe_id"
            ),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "target_id",
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_target_detector_recipes, **kwargs
        )

    def get_create_model_class(self):
        return AttachTargetDetectorRecipeDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_target_detector_recipe,
            call_fn_args=(),
            call_fn_kwargs=dict(
                target_id=self.module.params.get("target_id"),
                attach_target_detector_recipe_details=create_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateTargetDetectorRecipeDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_target_detector_recipe,
            call_fn_args=(),
            call_fn_kwargs=dict(
                target_id=self.module.params.get("target_id"),
                target_detector_recipe_id=self.module.params.get(
                    "target_detector_recipe_id"
                ),
                update_target_detector_recipe_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_target_detector_recipe,
            call_fn_args=(),
            call_fn_kwargs=dict(
                target_id=self.module.params.get("target_id"),
                target_detector_recipe_id=self.module.params.get(
                    "target_detector_recipe_id"
                ),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


TargetDetectorRecipeHelperCustom = get_custom_class("TargetDetectorRecipeHelperCustom")


class ResourceHelper(TargetDetectorRecipeHelperCustom, TargetDetectorRecipeHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            detector_recipe_id=dict(type="str"),
            is_validation_only_query=dict(type="bool"),
            detector_rules=dict(
                type="list",
                elements="dict",
                options=dict(
                    detector_rule_id=dict(type="str", required=True),
                    details=dict(
                        type="dict",
                        required=True,
                        options=dict(
                            condition_groups=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    compartment_id=dict(type="str", required=True),
                                    condition=dict(
                                        type="dict",
                                        required=True,
                                        options=dict(
                                            parameter=dict(type="str"),
                                            operator=dict(
                                                type="str",
                                                choices=[
                                                    "IN",
                                                    "NOT_IN",
                                                    "EQUALS",
                                                    "NOT_EQUALS",
                                                ],
                                            ),
                                            value=dict(type="str"),
                                            value_type=dict(
                                                type="str",
                                                choices=["MANAGED", "CUSTOM"],
                                            ),
                                            kind=dict(
                                                type="str",
                                                required=True,
                                                choices=["SIMPLE", "COMPOSITE"],
                                            ),
                                            left_operand=dict(
                                                type="dict",
                                                options=dict(
                                                    kind=dict(
                                                        type="str",
                                                        required=True,
                                                        choices=["COMPOSITE", "SIMPLE"],
                                                    )
                                                ),
                                            ),
                                            composite_operator=dict(
                                                type="str", choices=["AND", "OR"]
                                            ),
                                            right_operand=dict(
                                                type="dict",
                                                options=dict(
                                                    kind=dict(
                                                        type="str",
                                                        required=True,
                                                        choices=["COMPOSITE", "SIMPLE"],
                                                    )
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                            )
                        ),
                    ),
                ),
            ),
            target_id=dict(type="str", required=True),
            target_detector_recipe_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="target_detector_recipe",
        service_client_class=CloudGuardClient,
        namespace="cloud_guard",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
