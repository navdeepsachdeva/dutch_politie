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
module: oci_cloud_guard_target
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_cloud_guard_target_module.html)
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
    from oci.cloud_guard.models import CreateTargetDetails
    from oci.cloud_guard.models import UpdateTargetDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TargetHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(TargetHelperGen, self).get_possible_entity_types() + [
            "cloudguardtarget",
            "cloudguardtargets",
            "cloudGuardcloudguardtarget",
            "cloudGuardcloudguardtargets",
            "cloudguardtargetresource",
            "cloudguardtargetsresource",
            "target",
            "targets",
            "cloudGuardtarget",
            "cloudGuardtargets",
            "targetresource",
            "targetsresource",
            "cloudguard",
        ]

    def get_module_resource_id_param(self):
        return "target_id"

    def get_module_resource_id(self):
        return self.module.params.get("target_id")

    def get_get_fn(self):
        return self.client.get_target

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_target, target_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_target, target_id=self.module.params.get("target_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = (
            ["display_name"]
            if self._use_name_as_identifier()
            else ["display_name", "lifecycle_state"]
        )

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
        return oci_common_utils.list_all_resources(self.client.list_targets, **kwargs)

    def get_create_model_class(self):
        return CreateTargetDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_target,
            call_fn_args=(),
            call_fn_kwargs=dict(create_target_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateTargetDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_target,
            call_fn_args=(),
            call_fn_kwargs=dict(
                target_id=self.module.params.get("target_id"),
                update_target_details=update_details,
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
            call_fn=self.client.delete_target,
            call_fn_args=(),
            call_fn_kwargs=dict(target_id=self.module.params.get("target_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


TargetHelperCustom = get_custom_class("TargetHelperCustom")


class ResourceHelper(TargetHelperCustom, TargetHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            description=dict(type="str"),
            target_resource_type=dict(
                type="str",
                choices=["COMPARTMENT", "ERPCLOUD", "HCMCLOUD", "SECURITY_ZONE"],
            ),
            target_resource_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
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
                ],
            ),
            target_detector_recipes=dict(
                type="list",
                elements="dict",
                options=dict(
                    detector_recipe_id=dict(type="str"),
                    target_detector_recipe_id=dict(type="str"),
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
                                            compartment_id=dict(
                                                type="str", required=True
                                            ),
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
                                                                choices=[
                                                                    "COMPOSITE",
                                                                    "SIMPLE",
                                                                ],
                                                            )
                                                        ),
                                                    ),
                                                    composite_operator=dict(
                                                        type="str",
                                                        choices=["AND", "OR"],
                                                    ),
                                                    right_operand=dict(
                                                        type="dict",
                                                        options=dict(
                                                            kind=dict(
                                                                type="str",
                                                                required=True,
                                                                choices=[
                                                                    "COMPOSITE",
                                                                    "SIMPLE",
                                                                ],
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
                ),
            ),
            target_responder_recipes=dict(
                type="list",
                elements="dict",
                options=dict(
                    responder_recipe_id=dict(type="str"),
                    target_responder_recipe_id=dict(type="str"),
                    responder_rules=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            responder_rule_id=dict(type="str", required=True),
                            details=dict(
                                type="dict",
                                required=True,
                                options=dict(
                                    condition=dict(
                                        type="dict",
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
                                    configurations=dict(
                                        type="list",
                                        elements="dict",
                                        options=dict(
                                            config_key=dict(
                                                type="str", required=True, no_log=True
                                            ),
                                            name=dict(type="str", required=True),
                                            value=dict(type="str", required=True),
                                        ),
                                    ),
                                    mode=dict(
                                        type="str", choices=["AUTOACTION", "USERACTION"]
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            target_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="target",
        service_client_class=CloudGuardClient,
        namespace="cloud_guard",
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
