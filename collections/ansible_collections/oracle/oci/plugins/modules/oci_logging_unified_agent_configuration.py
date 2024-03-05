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
module: oci_logging_unified_agent_configuration
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_logging_unified_agent_configuration_module.html)
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
    from oci.logging import LoggingManagementClient
    from oci.logging.models import CreateUnifiedAgentConfigurationDetails
    from oci.logging.models import UpdateUnifiedAgentConfigurationDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class UnifiedAgentConfigurationHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            UnifiedAgentConfigurationHelperGen, self
        ).get_possible_entity_types() + [
            "unifiedagentconfiguration",
            "unifiedagentconfigurations",
            "loggingunifiedagentconfiguration",
            "loggingunifiedagentconfigurations",
            "unifiedagentconfigurationresource",
            "unifiedagentconfigurationsresource",
            "logging",
        ]

    def get_module_resource_id_param(self):
        return "unified_agent_configuration_id"

    def get_module_resource_id(self):
        return self.module.params.get("unified_agent_configuration_id")

    def get_get_fn(self):
        return self.client.get_unified_agent_configuration

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_unified_agent_configuration,
            unified_agent_configuration_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_unified_agent_configuration,
            unified_agent_configuration_id=self.module.params.get(
                "unified_agent_configuration_id"
            ),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
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
            self.client.list_unified_agent_configurations, **kwargs
        )

    def get_create_model_class(self):
        return CreateUnifiedAgentConfigurationDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_unified_agent_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_unified_agent_configuration_details=create_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateUnifiedAgentConfigurationDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_unified_agent_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                unified_agent_configuration_id=self.module.params.get(
                    "unified_agent_configuration_id"
                ),
                update_unified_agent_configuration_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_unified_agent_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                unified_agent_configuration_id=self.module.params.get(
                    "unified_agent_configuration_id"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


UnifiedAgentConfigurationHelperCustom = get_custom_class(
    "UnifiedAgentConfigurationHelperCustom"
)


class ResourceHelper(
    UnifiedAgentConfigurationHelperCustom, UnifiedAgentConfigurationHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            is_enabled=dict(type="bool"),
            defined_tags=dict(type="dict"),
            freeform_tags=dict(type="dict"),
            description=dict(type="str"),
            service_configuration=dict(
                type="dict",
                options=dict(
                    configuration_type=dict(
                        type="str", required=True, choices=["LOGGING"]
                    ),
                    sources=dict(
                        type="list",
                        elements="dict",
                        required=True,
                        options=dict(
                            channels=dict(type="list", elements="str"),
                            name=dict(type="str", required=True),
                            source_type=dict(
                                type="str",
                                required=True,
                                choices=["WINDOWS_EVENT_LOG", "LOG_TAIL"],
                            ),
                            paths=dict(type="list", elements="str"),
                            parser=dict(
                                type="dict",
                                options=dict(
                                    multi_line_start_regexp=dict(type="str"),
                                    time_type=dict(
                                        type="str",
                                        choices=["FLOAT", "UNIXTIME", "STRING"],
                                    ),
                                    grok_name_key=dict(type="str", no_log=True),
                                    grok_failure_key=dict(type="str", no_log=True),
                                    patterns=dict(
                                        type="list",
                                        elements="dict",
                                        options=dict(
                                            pattern=dict(type="str", required=True),
                                            name=dict(type="str"),
                                            field_time_key=dict(
                                                type="str", no_log=True
                                            ),
                                            field_time_format=dict(type="str"),
                                            field_time_zone=dict(type="str"),
                                        ),
                                    ),
                                    message_key=dict(type="str", no_log=True),
                                    rfc5424_time_format=dict(type="str"),
                                    message_format=dict(
                                        type="str",
                                        choices=["RFC3164", "RFC5424", "AUTO"],
                                    ),
                                    is_with_priority=dict(type="bool"),
                                    is_support_colonless_ident=dict(type="bool"),
                                    syslog_parser_type=dict(
                                        type="str", choices=["STRING", "REGEXP"]
                                    ),
                                    expression=dict(type="str"),
                                    time_format=dict(type="str"),
                                    format_firstline=dict(type="str"),
                                    format=dict(type="list", elements="str"),
                                    is_merge_cri_fields=dict(type="bool"),
                                    nested_parser=dict(
                                        type="dict",
                                        options=dict(
                                            parser_type=dict(
                                                type="str",
                                                required=True,
                                                choices=[
                                                    "AUDITD",
                                                    "CRI",
                                                    "JSON",
                                                    "TSV",
                                                    "CSV",
                                                    "NONE",
                                                    "SYSLOG",
                                                    "APACHE2",
                                                    "APACHE_ERROR",
                                                    "MSGPACK",
                                                    "REGEXP",
                                                    "MULTILINE",
                                                    "GROK",
                                                    "MULTILINE_GROK",
                                                ],
                                            ),
                                            field_time_key=dict(
                                                type="str", no_log=True
                                            ),
                                            types=dict(type="dict"),
                                            null_value_pattern=dict(type="str"),
                                            is_null_empty_string=dict(type="bool"),
                                            is_estimate_current_event=dict(type="bool"),
                                            is_keep_time_key=dict(
                                                type="bool", no_log=True
                                            ),
                                            timeout_in_milliseconds=dict(type="int"),
                                            time_type=dict(
                                                type="str",
                                                choices=["FLOAT", "UNIXTIME", "STRING"],
                                            ),
                                            time_format=dict(type="str"),
                                        ),
                                    ),
                                    parser_type=dict(
                                        type="str",
                                        required=True,
                                        choices=[
                                            "MULTILINE_GROK",
                                            "JSON",
                                            "GROK",
                                            "NONE",
                                            "SYSLOG",
                                            "AUDITD",
                                            "APACHE2",
                                            "REGEXP",
                                            "MULTILINE",
                                            "TSV",
                                            "CRI",
                                            "APACHE_ERROR",
                                            "MSGPACK",
                                            "CSV",
                                        ],
                                    ),
                                    field_time_key=dict(type="str", no_log=True),
                                    types=dict(type="dict"),
                                    null_value_pattern=dict(type="str"),
                                    is_null_empty_string=dict(type="bool"),
                                    is_estimate_current_event=dict(type="bool"),
                                    is_keep_time_key=dict(type="bool", no_log=True),
                                    timeout_in_milliseconds=dict(type="int"),
                                    delimiter=dict(type="str"),
                                    keys=dict(type="list", elements="str", no_log=True),
                                ),
                            ),
                        ),
                    ),
                    destination=dict(
                        type="dict",
                        required=True,
                        options=dict(
                            log_object_id=dict(type="str", required=True),
                            operational_metrics_configuration=dict(
                                type="dict",
                                options=dict(
                                    source=dict(
                                        type="dict",
                                        required=True,
                                        options=dict(
                                            type=dict(
                                                type="str",
                                                required=True,
                                                choices=["UMA_METRICS"],
                                            ),
                                            metrics=dict(type="list", elements="str"),
                                            record_input=dict(
                                                type="dict",
                                                options=dict(
                                                    namespace=dict(
                                                        type="str", required=True
                                                    ),
                                                    resource_group=dict(type="str"),
                                                ),
                                            ),
                                        ),
                                    ),
                                    destination=dict(
                                        type="dict",
                                        required=True,
                                        options=dict(
                                            compartment_id=dict(
                                                type="str", required=True
                                            )
                                        ),
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
            group_association=dict(
                type="dict", options=dict(group_list=dict(type="list", elements="str"))
            ),
            unified_agent_configuration_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="unified_agent_configuration",
        service_client_class=LoggingManagementClient,
        namespace="logging",
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
