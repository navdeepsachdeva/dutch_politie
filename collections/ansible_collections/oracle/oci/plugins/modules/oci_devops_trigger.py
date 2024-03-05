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
module: oci_devops_trigger
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_devops_trigger_module.html)
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
    from oci.devops.models import CreateTriggerDetails
    from oci.devops.models import UpdateTriggerDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DevopsTriggerHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(DevopsTriggerHelperGen, self).get_possible_entity_types() + [
            "trigger",
            "triggers",
            "devopstrigger",
            "devopstriggers",
            "triggerresource",
            "triggersresource",
            "devops",
        ]

    def get_module_resource_id_param(self):
        return "trigger_id"

    def get_module_resource_id(self):
        return self.module.params.get("trigger_id")

    def get_get_fn(self):
        return self.client.get_trigger

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_trigger, trigger_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_trigger, trigger_id=self.module.params.get("trigger_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["project_id", "display_name"]

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
        return oci_common_utils.list_all_resources(self.client.list_triggers, **kwargs)

    def get_create_model_class(self):
        return CreateTriggerDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_trigger,
            call_fn_args=(),
            call_fn_kwargs=dict(create_trigger_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateTriggerDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_trigger,
            call_fn_args=(),
            call_fn_kwargs=dict(
                trigger_id=self.module.params.get("trigger_id"),
                update_trigger_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_trigger,
            call_fn_args=(),
            call_fn_kwargs=dict(trigger_id=self.module.params.get("trigger_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DevopsTriggerHelperCustom = get_custom_class("DevopsTriggerHelperCustom")


class ResourceHelper(DevopsTriggerHelperCustom, DevopsTriggerHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            project_id=dict(type="str"),
            repository_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            trigger_source=dict(
                type="str",
                choices=[
                    "GITHUB",
                    "VBS",
                    "DEVOPS_CODE_REPOSITORY",
                    "BITBUCKET_CLOUD",
                    "GITLAB_SERVER",
                    "GITLAB",
                    "BITBUCKET_SERVER",
                ],
            ),
            actions=dict(
                type="list",
                elements="dict",
                options=dict(
                    type=dict(
                        type="str", required=True, choices=["TRIGGER_BUILD_PIPELINE"]
                    ),
                    filter=dict(
                        type="dict",
                        options=dict(
                            trigger_source=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "VBS",
                                    "DEVOPS_CODE_REPOSITORY",
                                    "BITBUCKET_CLOUD",
                                    "BITBUCKET_SERVER",
                                    "GITLAB",
                                    "GITHUB",
                                    "GITLAB_SERVER",
                                ],
                            ),
                            events=dict(
                                type="list",
                                elements="str",
                                choices=[
                                    "PUSH",
                                    "MERGE_REQUEST_CREATED",
                                    "MERGE_REQUEST_UPDATED",
                                    "MERGE_REQUEST_MERGED",
                                    "PULL_REQUEST_CREATED",
                                    "PULL_REQUEST_UPDATED",
                                    "PULL_REQUEST_MERGED",
                                    "PULL_REQUEST_OPENED",
                                    "PULL_REQUEST_MODIFIED",
                                    "PULL_REQUEST_REOPENED",
                                ],
                            ),
                            include=dict(
                                type="dict",
                                options=dict(
                                    repository_name=dict(type="str"),
                                    head_ref=dict(type="str"),
                                    base_ref=dict(type="str"),
                                    file_filter=dict(
                                        type="dict",
                                        options=dict(
                                            file_paths=dict(type="list", elements="str")
                                        ),
                                    ),
                                ),
                            ),
                            exclude=dict(
                                type="dict",
                                options=dict(
                                    file_filter=dict(
                                        type="dict",
                                        options=dict(
                                            file_paths=dict(type="list", elements="str")
                                        ),
                                    )
                                ),
                            ),
                        ),
                    ),
                    build_pipeline_id=dict(type="str", required=True),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            connection_id=dict(type="str"),
            trigger_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="trigger",
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
