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
module: oci_disaster_recovery_dr_plan
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_disaster_recovery_dr_plan_module.html)
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
    from oci.disaster_recovery import DisasterRecoveryClient
    from oci.disaster_recovery.models import CreateDrPlanDetails
    from oci.disaster_recovery.models import UpdateDrPlanDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DrPlanHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(DrPlanHelperGen, self).get_possible_entity_types() + [
            "drplan",
            "drplans",
            "disasterRecoverydrplan",
            "disasterRecoverydrplans",
            "drplanresource",
            "drplansresource",
            "disasterrecovery",
        ]

    def get_module_resource_id_param(self):
        return "dr_plan_id"

    def get_module_resource_id(self):
        return self.module.params.get("dr_plan_id")

    def get_get_fn(self):
        return self.client.get_dr_plan

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_dr_plan, dr_plan_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_dr_plan, dr_plan_id=self.module.params.get("dr_plan_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "dr_protection_group_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["dr_plan_id", "display_name"]

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
        return oci_common_utils.list_all_resources(self.client.list_dr_plans, **kwargs)

    def get_create_model_class(self):
        return CreateDrPlanDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_dr_plan,
            call_fn_args=(),
            call_fn_kwargs=dict(create_dr_plan_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateDrPlanDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_dr_plan,
            call_fn_args=(),
            call_fn_kwargs=dict(
                update_dr_plan_details=update_details,
                dr_plan_id=self.module.params.get("dr_plan_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_dr_plan,
            call_fn_args=(),
            call_fn_kwargs=dict(dr_plan_id=self.module.params.get("dr_plan_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


DrPlanHelperCustom = get_custom_class("DrPlanHelperCustom")


class ResourceHelper(DrPlanHelperCustom, DrPlanHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            type=dict(type="str", choices=["SWITCHOVER", "FAILOVER"]),
            dr_protection_group_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            plan_groups=dict(
                type="list",
                elements="dict",
                options=dict(
                    id=dict(type="str"),
                    display_name=dict(aliases=["name"], type="str"),
                    type=dict(
                        type="str",
                        choices=["USER_DEFINED", "BUILT_IN", "BUILT_IN_PRECHECK"],
                    ),
                    steps=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            id=dict(type="str"),
                            display_name=dict(aliases=["name"], type="str"),
                            error_mode=dict(
                                type="str",
                                choices=["STOP_ON_ERROR", "CONTINUE_ON_ERROR"],
                            ),
                            timeout=dict(type="int"),
                            is_enabled=dict(type="bool"),
                            user_defined_step=dict(
                                type="dict",
                                options=dict(
                                    function_id=dict(type="str"),
                                    request_body=dict(type="str"),
                                    object_storage_script_location=dict(
                                        type="dict",
                                        options=dict(
                                            namespace=dict(type="str", required=True),
                                            bucket=dict(type="str", required=True),
                                            object=dict(type="str", required=True),
                                        ),
                                    ),
                                    step_type=dict(
                                        type="str",
                                        required=True,
                                        choices=[
                                            "RUN_LOCAL_SCRIPT_PRECHECK",
                                            "INVOKE_FUNCTION_PRECHECK",
                                            "INVOKE_FUNCTION",
                                            "RUN_OBJECTSTORE_SCRIPT",
                                            "RUN_OBJECTSTORE_SCRIPT_PRECHECK",
                                            "RUN_LOCAL_SCRIPT",
                                        ],
                                    ),
                                    run_on_instance_id=dict(type="str"),
                                    script_command=dict(type="str"),
                                    run_as_user=dict(type="str"),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            dr_plan_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="dr_plan",
        service_client_class=DisasterRecoveryClient,
        namespace="disaster_recovery",
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
