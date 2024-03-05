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
module: oci_apm_config_config
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_apm_config_config_module.html)
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
    from oci.apm_config import ConfigClient
    from oci.apm_config.models import CreateConfigDetails
    from oci.apm_config.models import UpdateConfigDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ConfigHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(ConfigHelperGen, self).get_possible_entity_types() + [
            "config",
            "configs",
            "apmConfigconfig",
            "apmConfigconfigs",
            "configresource",
            "configsresource",
            "apmconfig",
        ]

    def get_module_resource_id_param(self):
        return "config_id"

    def get_module_resource_id(self):
        return self.module.params.get("config_id")

    def get_get_fn(self):
        return self.client.get_config

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_config,
            apm_domain_id=self.module.params.get("apm_domain_id"),
            config_id=self.module.params.get("config_id"),
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
            ["display_name"]
            if self._use_name_as_identifier()
            else ["config_type", "display_name"]
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
        return oci_common_utils.list_all_resources(self.client.list_configs, **kwargs)

    def get_create_model_class(self):
        return CreateConfigDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_config,
            call_fn_args=(),
            call_fn_kwargs=dict(
                apm_domain_id=self.module.params.get("apm_domain_id"),
                create_config_details=create_details,
                opc_dry_run=self.module.params.get("opc_dry_run"),
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
        return UpdateConfigDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_config,
            call_fn_args=(),
            call_fn_kwargs=dict(
                apm_domain_id=self.module.params.get("apm_domain_id"),
                config_id=self.module.params.get("config_id"),
                update_config_details=update_details,
                opc_dry_run=self.module.params.get("opc_dry_run"),
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
            call_fn=self.client.delete_config,
            call_fn_args=(),
            call_fn_kwargs=dict(
                apm_domain_id=self.module.params.get("apm_domain_id"),
                config_id=self.module.params.get("config_id"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


ConfigHelperCustom = get_custom_class("ConfigHelperCustom")


class ResourceHelper(ConfigHelperCustom, ConfigHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            filter_id=dict(type="str"),
            namespace=dict(type="str"),
            dimensions=dict(
                type="list",
                elements="dict",
                options=dict(
                    name=dict(type="str", required=True), value_source=dict(type="str")
                ),
            ),
            metrics=dict(
                type="list",
                elements="dict",
                options=dict(
                    name=dict(type="str", required=True),
                    value_source=dict(type="str"),
                    unit=dict(type="str"),
                    description=dict(type="str"),
                ),
            ),
            rules=dict(
                type="list",
                elements="dict",
                options=dict(
                    filter_text=dict(type="str", required=True),
                    priority=dict(type="int", required=True),
                    is_enabled=dict(type="bool"),
                    satisfied_response_time=dict(type="int"),
                    tolerating_response_time=dict(type="int"),
                    is_apply_to_error_spans=dict(type="bool"),
                    display_name=dict(aliases=["name"], type="str"),
                ),
            ),
            filter_text=dict(type="str"),
            config_type=dict(
                type="str", choices=["SPAN_FILTER", "METRIC_GROUP", "OPTIONS", "APDEX"]
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            options=dict(type="dict"),
            group=dict(type="str"),
            description=dict(type="str"),
            opc_dry_run=dict(type="str"),
            apm_domain_id=dict(type="str", required=True),
            config_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="config",
        service_client_class=ConfigClient,
        namespace="apm_config",
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
