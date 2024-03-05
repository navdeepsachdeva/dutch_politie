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
module: oci_data_science_pipeline_run
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_data_science_pipeline_run_module.html)
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
    from oci.data_science import DataScienceClient
    from oci.data_science.models import CreatePipelineRunDetails
    from oci.data_science.models import UpdatePipelineRunDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataSciencePipelineRunHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            DataSciencePipelineRunHelperGen, self
        ).get_possible_entity_types() + [
            "pipelinerun",
            "pipelineruns",
            "dataSciencepipelinerun",
            "dataSciencepipelineruns",
            "pipelinerunresource",
            "pipelinerunsresource",
            "datascience",
        ]

    def get_module_resource_id_param(self):
        return "pipeline_run_id"

    def get_module_resource_id(self):
        return self.module.params.get("pipeline_run_id")

    def get_get_fn(self):
        return self.client.get_pipeline_run

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_pipeline_run, pipeline_run_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_pipeline_run,
            pipeline_run_id=self.module.params.get("pipeline_run_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["pipeline_id", "display_name"]

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
            self.client.list_pipeline_runs, **kwargs
        )

    def get_create_model_class(self):
        return CreatePipelineRunDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_pipeline_run,
            call_fn_args=(),
            call_fn_kwargs=dict(create_pipeline_run_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdatePipelineRunDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_pipeline_run,
            call_fn_args=(),
            call_fn_kwargs=dict(
                pipeline_run_id=self.module.params.get("pipeline_run_id"),
                update_pipeline_run_details=update_details,
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
            call_fn=self.client.delete_pipeline_run,
            call_fn_args=(),
            call_fn_kwargs=dict(
                pipeline_run_id=self.module.params.get("pipeline_run_id"),
                delete_related_job_runs=self.module.params.get(
                    "delete_related_job_runs"
                ),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


DataSciencePipelineRunHelperCustom = get_custom_class(
    "DataSciencePipelineRunHelperCustom"
)


class ResourceHelper(
    DataSciencePipelineRunHelperCustom, DataSciencePipelineRunHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            project_id=dict(type="str"),
            compartment_id=dict(type="str"),
            pipeline_id=dict(type="str"),
            configuration_override_details=dict(
                type="dict",
                options=dict(
                    type=dict(type="str", required=True, choices=["DEFAULT"]),
                    maximum_runtime_in_minutes=dict(type="int"),
                    environment_variables=dict(type="dict"),
                    command_line_arguments=dict(type="str"),
                ),
            ),
            log_configuration_override_details=dict(
                type="dict",
                options=dict(
                    enable_logging=dict(type="bool"),
                    enable_auto_log_creation=dict(type="bool"),
                    log_group_id=dict(type="str"),
                    log_id=dict(type="str"),
                ),
            ),
            step_override_details=dict(
                type="list",
                elements="dict",
                options=dict(
                    step_name=dict(type="str", required=True),
                    step_configuration_details=dict(
                        type="dict",
                        required=True,
                        options=dict(
                            maximum_runtime_in_minutes=dict(type="int"),
                            environment_variables=dict(type="dict"),
                            command_line_arguments=dict(type="str"),
                        ),
                    ),
                ),
            ),
            system_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            pipeline_run_id=dict(aliases=["id"], type="str"),
            delete_related_job_runs=dict(type="bool"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="pipeline_run",
        service_client_class=DataScienceClient,
        namespace="data_science",
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
