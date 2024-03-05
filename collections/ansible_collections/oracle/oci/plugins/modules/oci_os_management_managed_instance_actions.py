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
module: oci_os_management_managed_instance_actions
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_os_management_managed_instance_actions_module.html)
    for the module documentation.
author: Oracle (@oracle)
"""


from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.os_management import OsManagementClient
    from oci.os_management.models import (
        AttachChildSoftwareSourceToManagedInstanceDetails,
    )
    from oci.os_management.models import (
        AttachParentSoftwareSourceToManagedInstanceDetails,
    )
    from oci.os_management.models import (
        DetachChildSoftwareSourceFromManagedInstanceDetails,
    )
    from oci.os_management.models import (
        DetachParentSoftwareSourceFromManagedInstanceDetails,
    )
    from oci.os_management.models import ManageModuleStreamsOnManagedInstanceDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ManagedInstanceActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        attach_child_software_source
        attach_parent_software_source
        detach_child_software_source
        detach_parent_software_source
        disable_module_stream
        enable_module_stream
        install_all_package_updates
        install_all_windows_updates
        install_module_stream_profile
        install_package
        install_package_update
        install_windows_update
        manage_module_streams
        remove_module_stream_profile
        remove_package
        switch_module_stream
    """

    def get_default_module_wait_timeout(self):
        return 3600

    @staticmethod
    def get_module_resource_id_param():
        return "managed_instance_id"

    def get_module_resource_id(self):
        return self.module.params.get("managed_instance_id")

    def get_get_fn(self):
        return self.client.get_managed_instance

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_managed_instance,
            managed_instance_id=self.module.params.get("managed_instance_id"),
        )

    def attach_child_software_source(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AttachChildSoftwareSourceToManagedInstanceDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.attach_child_software_source_to_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                attach_child_software_source_to_managed_instance_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def attach_parent_software_source(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AttachParentSoftwareSourceToManagedInstanceDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.attach_parent_software_source_to_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                attach_parent_software_source_to_managed_instance_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def detach_child_software_source(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, DetachChildSoftwareSourceFromManagedInstanceDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.detach_child_software_source_from_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                detach_child_software_source_from_managed_instance_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def detach_parent_software_source(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, DetachParentSoftwareSourceFromManagedInstanceDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.detach_parent_software_source_from_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                detach_parent_software_source_from_managed_instance_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def disable_module_stream(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.disable_module_stream_on_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                module_name=self.module.params.get("module_name"),
                stream_name=self.module.params.get("stream_name"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def enable_module_stream(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.enable_module_stream_on_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                module_name=self.module.params.get("module_name"),
                stream_name=self.module.params.get("stream_name"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def install_all_package_updates(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.install_all_package_updates_on_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                update_type=self.module.params.get("update_type"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def install_all_windows_updates(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.install_all_windows_updates_on_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                update_type=self.module.params.get("update_type"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def install_module_stream_profile(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.install_module_stream_profile_on_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                module_name=self.module.params.get("module_name"),
                stream_name=self.module.params.get("stream_name"),
                profile_name=self.module.params.get("profile_name"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def install_package(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.install_package_on_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                software_package_name=self.module.params.get("software_package_name"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def install_package_update(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.install_package_update_on_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                software_package_name=self.module.params.get("software_package_name"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def install_windows_update(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.install_windows_update_on_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                windows_update_name=self.module.params.get("windows_update_name"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def manage_module_streams(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ManageModuleStreamsOnManagedInstanceDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.manage_module_streams_on_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                manage_module_streams_on_managed_instance_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def remove_module_stream_profile(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_module_stream_profile_from_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                module_name=self.module.params.get("module_name"),
                stream_name=self.module.params.get("stream_name"),
                profile_name=self.module.params.get("profile_name"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def remove_package(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_package_from_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                software_package_name=self.module.params.get("software_package_name"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def switch_module_stream(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.switch_module_stream_on_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                module_name=self.module.params.get("module_name"),
                stream_name=self.module.params.get("stream_name"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ManagedInstanceActionsHelperCustom = get_custom_class(
    "ManagedInstanceActionsHelperCustom"
)


class ResourceHelper(
    ManagedInstanceActionsHelperCustom, ManagedInstanceActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            software_source_id=dict(type="str"),
            update_type=dict(
                type="str",
                choices=[
                    "SECURITY",
                    "BUGFIX",
                    "ENHANCEMENT",
                    "OTHER",
                    "KSPLICE",
                    "ALL",
                ],
            ),
            windows_update_name=dict(type="str"),
            is_dry_run=dict(type="bool"),
            enable=dict(
                type="list",
                elements="dict",
                options=dict(
                    module_name=dict(type="str", required=True),
                    stream_name=dict(type="str", required=True),
                ),
            ),
            disable=dict(
                type="list",
                elements="dict",
                options=dict(
                    module_name=dict(type="str", required=True),
                    stream_name=dict(type="str", required=True),
                ),
            ),
            install=dict(
                type="list",
                elements="dict",
                options=dict(
                    module_name=dict(type="str", required=True),
                    stream_name=dict(type="str", required=True),
                    profile_name=dict(type="str", required=True),
                ),
            ),
            remove=dict(
                type="list",
                elements="dict",
                options=dict(
                    module_name=dict(type="str", required=True),
                    stream_name=dict(type="str", required=True),
                    profile_name=dict(type="str", required=True),
                ),
            ),
            profile_name=dict(type="str"),
            software_package_name=dict(type="str"),
            managed_instance_id=dict(aliases=["id"], type="str", required=True),
            module_name=dict(type="str"),
            stream_name=dict(type="str"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "attach_child_software_source",
                    "attach_parent_software_source",
                    "detach_child_software_source",
                    "detach_parent_software_source",
                    "disable_module_stream",
                    "enable_module_stream",
                    "install_all_package_updates",
                    "install_all_windows_updates",
                    "install_module_stream_profile",
                    "install_package",
                    "install_package_update",
                    "install_windows_update",
                    "manage_module_streams",
                    "remove_module_stream_profile",
                    "remove_package",
                    "switch_module_stream",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="managed_instance",
        service_client_class=OsManagementClient,
        namespace="os_management",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
