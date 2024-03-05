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
module: oci_functions_function_actions
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_functions_function_actions_module.html)
    for the module documentation.
author: Oracle (@oracle)
"""


from ansible.module_utils._text import to_bytes
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
    from oci.functions import FunctionsManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class FunctionActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        invoke
    """

    @staticmethod
    def get_module_resource_id_param():
        return "function_id"

    def get_module_resource_id(self):
        return self.module.params.get("function_id")

    def get_get_fn(self):
        return self.client.get_function

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_function, function_id=self.module.params.get("function_id"),
        )

    def invoke(self):
        response = oci_wait_utils.call_and_wait(
            call_fn=self.client.invoke_function,
            call_fn_args=(),
            call_fn_kwargs=dict(
                function_id=self.module.params.get("function_id"),
                invoke_function_body=self.module.params.get("invoke_function_body"),
                fn_intent=self.module.params.get("fn_intent"),
                fn_invoke_type=self.module.params.get("fn_invoke_type"),
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
        dest = self.module.params.get("dest")
        chunk_size = oci_common_utils.MEBIBYTE
        with open(to_bytes(dest), "wb") as dest_file:
            for chunk in response.raw.stream(chunk_size, decode_content=True):
                dest_file.write(chunk)
        return None


FunctionActionsHelperCustom = get_custom_class("FunctionActionsHelperCustom")


class ResourceHelper(FunctionActionsHelperCustom, FunctionActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            dest=dict(type="str", required=True),
            function_id=dict(aliases=["id"], type="str", required=True),
            invoke_function_body=dict(type="str"),
            fn_intent=dict(type="str", choices=["httprequest", "cloudevent"]),
            fn_invoke_type=dict(type="str", choices=["detached", "sync"]),
            action=dict(type="str", required=True, choices=["invoke"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="function",
        service_client_class=FunctionsManagementClient,
        namespace="functions",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
