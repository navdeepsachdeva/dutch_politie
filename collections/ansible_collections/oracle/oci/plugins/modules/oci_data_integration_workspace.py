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
module: oci_data_integration_workspace
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_data_integration_workspace_module.html)
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
    from oci.data_integration import DataIntegrationClient
    from oci.data_integration.models import CreateWorkspaceDetails
    from oci.data_integration.models import UpdateWorkspaceDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class WorkspaceHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(WorkspaceHelperGen, self).get_possible_entity_types() + [
            "disworkspace",
            "disworkspaces",
            "dataIntegrationdisworkspace",
            "dataIntegrationdisworkspaces",
            "disworkspaceresource",
            "disworkspacesresource",
            "workspace",
            "workspaces",
            "dataIntegrationworkspace",
            "dataIntegrationworkspaces",
            "workspaceresource",
            "workspacesresource",
            "dataintegration",
        ]

    def get_module_resource_id_param(self):
        return "workspace_id"

    def get_module_resource_id(self):
        return self.module.params.get("workspace_id")

    def get_get_fn(self):
        return self.client.get_workspace

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_workspace, workspace_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_workspace,
            workspace_id=self.module.params.get("workspace_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
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
            self.client.list_workspaces, **kwargs
        )

    def get_create_model_class(self):
        return CreateWorkspaceDetails

    def get_exclude_attributes(self):
        return ["registry_compartment_id", "registry_name", "endpoint_compartment_id"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_workspace,
            call_fn_args=(),
            call_fn_kwargs=dict(create_workspace_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateWorkspaceDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_workspace,
            call_fn_args=(),
            call_fn_kwargs=dict(
                workspace_id=self.module.params.get("workspace_id"),
                update_workspace_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_workspace,
            call_fn_args=(),
            call_fn_kwargs=dict(
                workspace_id=self.module.params.get("workspace_id"),
                quiesce_timeout=self.module.params.get("quiesce_timeout"),
                is_force_operation=self.module.params.get("is_force_operation"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


WorkspaceHelperCustom = get_custom_class("WorkspaceHelperCustom")


class ResourceHelper(WorkspaceHelperCustom, WorkspaceHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            vcn_id=dict(type="str"),
            subnet_id=dict(type="str"),
            dns_server_ip=dict(type="str"),
            dns_server_zone=dict(type="str"),
            compartment_id=dict(type="str"),
            is_private_network_enabled=dict(type="bool"),
            registry_id=dict(type="str"),
            endpoint_id=dict(type="str"),
            registry_name=dict(type="str"),
            registry_compartment_id=dict(type="str"),
            endpoint_name=dict(type="str"),
            endpoint_compartment_id=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            description=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            workspace_id=dict(aliases=["id"], type="str"),
            quiesce_timeout=dict(type="int"),
            is_force_operation=dict(type="bool"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="workspace",
        service_client_class=DataIntegrationClient,
        namespace="data_integration",
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
