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
module: oci_resource_manager_stack
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_resource_manager_stack_module.html)
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
    from oci.resource_manager import ResourceManagerClient
    from oci.resource_manager.models import CreateStackDetails
    from oci.resource_manager.models import UpdateStackDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class StackHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(StackHelperGen, self).get_possible_entity_types() + [
            "stack",
            "stacks",
            "resourceManagerstack",
            "resourceManagerstacks",
            "stackresource",
            "stacksresource",
            "resourcemanager",
        ]

    def get_module_resource_id_param(self):
        return "stack_id"

    def get_module_resource_id(self):
        return self.module.params.get("stack_id")

    def get_get_fn(self):
        return self.client.get_stack

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_stack, stack_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_stack, stack_id=self.module.params.get("stack_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["compartment_id", "display_name"]

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
        return oci_common_utils.list_all_resources(self.client.list_stacks, **kwargs)

    def get_create_model_class(self):
        return CreateStackDetails

    def get_exclude_attributes(self):
        return ["config_source.template_id", "config_source.zip_file_base64_encoded"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_stack,
            call_fn_args=(),
            call_fn_kwargs=dict(create_stack_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateStackDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_stack,
            call_fn_args=(),
            call_fn_kwargs=dict(
                stack_id=self.module.params.get("stack_id"),
                update_stack_details=update_details,
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
            call_fn=self.client.delete_stack,
            call_fn_args=(),
            call_fn_kwargs=dict(stack_id=self.module.params.get("stack_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


StackHelperCustom = get_custom_class("StackHelperCustom")


class ResourceHelper(StackHelperCustom, StackHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            config_source=dict(
                type="dict",
                options=dict(
                    compartment_id=dict(type="str"),
                    services_to_discover=dict(type="list", elements="str"),
                    template_id=dict(type="str"),
                    workspace_id=dict(type="str"),
                    configuration_source_provider_id=dict(type="str"),
                    repository_url=dict(type="str"),
                    region=dict(type="str"),
                    namespace=dict(type="str"),
                    bucket_name=dict(type="str"),
                    zip_file_base64_encoded=dict(type="str"),
                    config_source_type=dict(
                        type="str",
                        required=True,
                        choices=[
                            "DEVOPS_CONFIG_SOURCE",
                            "BITBUCKET_CLOUD_CONFIG_SOURCE",
                            "ZIP_UPLOAD",
                            "BITBUCKET_SERVER_CONFIG_SOURCE",
                            "GIT_CONFIG_SOURCE",
                            "OBJECT_STORAGE_CONFIG_SOURCE",
                            "COMPARTMENT_CONFIG_SOURCE",
                            "TEMPLATE_CONFIG_SOURCE",
                        ],
                    ),
                    working_directory=dict(type="str"),
                    project_id=dict(type="str"),
                    repository_id=dict(type="str"),
                    branch_name=dict(type="str"),
                ),
            ),
            custom_terraform_provider=dict(
                type="dict",
                options=dict(
                    region=dict(type="str", required=True),
                    namespace=dict(type="str", required=True),
                    bucket_name=dict(type="str", required=True),
                ),
            ),
            is_third_party_provider_experience_enabled=dict(type="bool"),
            variables=dict(type="dict"),
            terraform_version=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            stack_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="stack",
        service_client_class=ResourceManagerClient,
        namespace="resource_manager",
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
