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
module: oci_apm_synthetics_monitor
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_apm_synthetics_monitor_module.html)
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
    from oci.apm_synthetics import ApmSyntheticClient
    from oci.apm_synthetics.models import CreateMonitorDetails
    from oci.apm_synthetics.models import UpdateMonitorDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MonitorHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(MonitorHelperGen, self).get_possible_entity_types() + [
            "monitor",
            "monitors",
            "apmSyntheticsmonitor",
            "apmSyntheticsmonitors",
            "monitorresource",
            "monitorsresource",
            "apmsynthetics",
        ]

    def get_module_resource_id_param(self):
        return "monitor_id"

    def get_module_resource_id(self):
        return self.module.params.get("monitor_id")

    def get_get_fn(self):
        return self.client.get_monitor

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_monitor,
            apm_domain_id=self.module.params.get("apm_domain_id"),
            monitor_id=self.module.params.get("monitor_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "apm_domain_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = (
            ["display_name", "monitor_type"]
            if self._use_name_as_identifier()
            else ["display_name", "script_id", "monitor_type", "status"]
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
        return oci_common_utils.list_all_resources(self.client.list_monitors, **kwargs)

    def get_create_model_class(self):
        return CreateMonitorDetails

    def get_exclude_attributes(self):
        return ["script_parameters.param_value", "script_parameters.param_name"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_monitor,
            call_fn_args=(),
            call_fn_kwargs=dict(
                apm_domain_id=self.module.params.get("apm_domain_id"),
                create_monitor_details=create_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateMonitorDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_monitor,
            call_fn_args=(),
            call_fn_kwargs=dict(
                apm_domain_id=self.module.params.get("apm_domain_id"),
                monitor_id=self.module.params.get("monitor_id"),
                update_monitor_details=update_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_monitor,
            call_fn_args=(),
            call_fn_kwargs=dict(
                apm_domain_id=self.module.params.get("apm_domain_id"),
                monitor_id=self.module.params.get("monitor_id"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


MonitorHelperCustom = get_custom_class("MonitorHelperCustom")


class ResourceHelper(MonitorHelperCustom, MonitorHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            monitor_type=dict(
                type="str",
                choices=[
                    "SCRIPTED_BROWSER",
                    "BROWSER",
                    "SCRIPTED_REST",
                    "REST",
                    "NETWORK",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
            vantage_points=dict(type="list", elements="str"),
            script_id=dict(type="str"),
            status=dict(type="str", choices=["ENABLED", "DISABLED", "INVALID"]),
            repeat_interval_in_seconds=dict(type="int"),
            is_run_once=dict(type="bool"),
            timeout_in_seconds=dict(type="int"),
            target=dict(type="str"),
            script_parameters=dict(
                type="list",
                elements="dict",
                options=dict(
                    param_name=dict(type="str", required=True),
                    param_value=dict(type="str", required=True),
                ),
            ),
            configuration=dict(
                type="dict",
                options=dict(
                    is_redirection_enabled=dict(type="bool"),
                    request_method=dict(type="str", choices=["GET", "POST"]),
                    req_authentication_scheme=dict(
                        type="str",
                        choices=[
                            "NONE",
                            "RESOURCE_PRINCIPAL",
                            "OAUTH",
                            "BASIC",
                            "BEARER",
                        ],
                    ),
                    req_authentication_details=dict(
                        type="dict",
                        options=dict(
                            oauth_scheme=dict(type="str", choices=["NONE", "BASIC"]),
                            auth_user_name=dict(type="str"),
                            auth_user_password=dict(type="str", no_log=True),
                            auth_token=dict(type="str", no_log=True),
                            auth_url=dict(type="str"),
                            auth_headers=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    header_name=dict(type="str", required=True),
                                    header_value=dict(type="str"),
                                ),
                            ),
                            auth_request_method=dict(
                                type="str", choices=["GET", "POST"]
                            ),
                            auth_request_post_body=dict(type="str"),
                        ),
                    ),
                    client_certificate_details=dict(
                        type="dict",
                        options=dict(
                            client_certificate=dict(
                                type="dict",
                                options=dict(
                                    file_name=dict(type="str", required=True),
                                    content=dict(type="str", required=True),
                                ),
                            ),
                            private_key=dict(
                                type="dict",
                                no_log=False,
                                options=dict(
                                    file_name=dict(type="str", required=True),
                                    content=dict(type="str", required=True),
                                ),
                            ),
                        ),
                    ),
                    request_headers=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            header_name=dict(type="str", required=True),
                            header_value=dict(type="str"),
                        ),
                    ),
                    request_query_params=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            param_name=dict(type="str", required=True),
                            param_value=dict(type="str"),
                        ),
                    ),
                    request_post_body=dict(type="str"),
                    verify_response_content=dict(type="str"),
                    is_certificate_validation_enabled=dict(type="bool"),
                    is_default_snapshot_enabled=dict(type="bool"),
                    verify_texts=dict(
                        type="list",
                        elements="dict",
                        options=dict(text=dict(type="str")),
                    ),
                    verify_response_codes=dict(type="list", elements="str"),
                    config_type=dict(
                        type="str",
                        required=True,
                        choices=[
                            "SCRIPTED_REST_CONFIG",
                            "SCRIPTED_BROWSER_CONFIG",
                            "REST_CONFIG",
                            "BROWSER_CONFIG",
                            "NETWORK_CONFIG",
                        ],
                    ),
                    is_failure_retried=dict(type="bool"),
                    dns_configuration=dict(
                        type="dict",
                        options=dict(
                            is_override_dns=dict(type="bool"),
                            override_dns_ip=dict(type="str"),
                        ),
                    ),
                    network_configuration=dict(
                        type="dict",
                        options=dict(
                            number_of_hops=dict(type="int"),
                            probe_per_hop=dict(type="int"),
                            transmission_rate=dict(type="int"),
                            protocol=dict(type="str", choices=["ICMP", "TCP"]),
                            probe_mode=dict(type="str", choices=["SACK", "SYN"]),
                        ),
                    ),
                ),
            ),
            availability_configuration=dict(
                type="dict",
                options=dict(
                    max_allowed_failures_per_interval=dict(type="int"),
                    min_allowed_runs_per_interval=dict(type="int"),
                ),
            ),
            maintenance_window_schedule=dict(
                type="dict",
                options=dict(
                    time_started=dict(type="str"), time_ended=dict(type="str")
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            is_run_now=dict(type="bool"),
            scheduling_policy=dict(
                type="str", choices=["ALL", "ROUND_ROBIN", "BATCHED_ROUND_ROBIN"]
            ),
            batch_interval_in_seconds=dict(type="int"),
            apm_domain_id=dict(type="str", required=True),
            monitor_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="monitor",
        service_client_class=ApmSyntheticClient,
        namespace="apm_synthetics",
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
