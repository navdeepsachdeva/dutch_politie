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
module: oci_waas_policy_config
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_waas_policy_config_module.html)
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
    from oci.waas import WaasClient
    from oci.waas.models import PolicyConfig

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PolicyConfigHelperGen(OCIResourceHelperBase):
    """Supported operations: update and get"""

    def get_possible_entity_types(self):
        return super(PolicyConfigHelperGen, self).get_possible_entity_types() + [
            "policyconfig",
            "policyconfigs",
            "waaspolicyconfig",
            "waaspolicyconfigs",
            "policyconfigresource",
            "policyconfigsresource",
            "waas",
        ]

    def get_module_resource_id_param(self):
        return "waas_policy_id"

    def get_module_resource_id(self):
        return self.module.params.get("waas_policy_id")

    def get_get_fn(self):
        return self.client.get_policy_config

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_policy_config,
            waas_policy_id=self.module.params.get("waas_policy_id"),
        )

    def get_update_model_class(self):
        return PolicyConfig

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_policy_config,
            call_fn_args=(),
            call_fn_kwargs=dict(
                waas_policy_id=self.module.params.get("waas_policy_id"),
                update_policy_config_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


PolicyConfigHelperCustom = get_custom_class("PolicyConfigHelperCustom")


class ResourceHelper(PolicyConfigHelperCustom, PolicyConfigHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            waas_policy_id=dict(aliases=["id"], type="str", required=True),
            certificate_id=dict(type="str"),
            is_https_enabled=dict(type="bool"),
            is_https_forced=dict(type="bool"),
            tls_protocols=dict(
                type="list",
                elements="str",
                choices=["TLS_V1", "TLS_V1_1", "TLS_V1_2", "TLS_V1_3"],
            ),
            is_origin_compression_enabled=dict(type="bool"),
            is_behind_cdn=dict(type="bool"),
            client_address_header=dict(
                type="str",
                choices=[
                    "X_FORWARDED_FOR",
                    "X_CLIENT_IP",
                    "X_REAL_IP",
                    "CLIENT_IP",
                    "TRUE_CLIENT_IP",
                ],
            ),
            is_cache_control_respected=dict(type="bool"),
            is_response_buffering_enabled=dict(type="bool"),
            cipher_group=dict(type="str", choices=["DEFAULT"]),
            load_balancing_method=dict(
                type="dict",
                options=dict(
                    name=dict(type="str"),
                    domain=dict(type="str"),
                    expiration_time_in_seconds=dict(type="int"),
                    method=dict(
                        type="str",
                        required=True,
                        choices=["ROUND_ROBIN", "STICKY_COOKIE", "IP_HASH"],
                    ),
                ),
            ),
            websocket_path_prefixes=dict(type="list", elements="str"),
            is_sni_enabled=dict(type="bool"),
            health_checks=dict(
                type="dict",
                options=dict(
                    is_enabled=dict(type="bool"),
                    method=dict(type="str", choices=["GET", "HEAD", "POST"]),
                    path=dict(type="str"),
                    headers=dict(type="dict"),
                    expected_response_code_group=dict(
                        type="list",
                        elements="str",
                        choices=["2XX", "3XX", "4XX", "5XX"],
                    ),
                    is_response_text_check_enabled=dict(type="bool"),
                    expected_response_text=dict(type="str"),
                    interval_in_seconds=dict(type="int"),
                    timeout_in_seconds=dict(type="int"),
                    healthy_threshold=dict(type="int"),
                    unhealthy_threshold=dict(type="int"),
                ),
            ),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="policy_config",
        service_client_class=WaasClient,
        namespace="waas",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
