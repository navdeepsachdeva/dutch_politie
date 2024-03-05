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
module: oci_key_management_generated_key
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_key_management_generated_key_module.html)
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
    from oci.key_management import KmsCryptoClient
    from oci.key_management.models import GenerateKeyDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class GeneratedKeyHelperGen(OCIResourceHelperBase):
    """Supported operations: create"""

    def get_possible_entity_types(self):
        return super(GeneratedKeyHelperGen, self).get_possible_entity_types() + [
            "generatedkey",
            "generatedkeys",
            "keyManagementgeneratedkey",
            "keyManagementgeneratedkeys",
            "generatedkeyresource",
            "generatedkeysresource",
            "generatedataencryptionkey",
            "generatedataencryptionkeys",
            "keyManagementgeneratedataencryptionkey",
            "keyManagementgeneratedataencryptionkeys",
            "generatedataencryptionkeyresource",
            "generatedataencryptionkeysresource",
            "keymanagement",
        ]

    def get_module_resource_id(self):
        return None

    # There is no idempotency for this module (no get or list ops)
    def get_matching_resource(self):
        return None

    def get_create_model_class(self):
        return GenerateKeyDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.generate_data_encryption_key,
            call_fn_args=(),
            call_fn_kwargs=dict(generate_key_details=create_details,),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )


GeneratedKeyHelperCustom = get_custom_class("GeneratedKeyHelperCustom")


class ResourceHelper(GeneratedKeyHelperCustom, GeneratedKeyHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            associated_data=dict(type="dict"),
            include_plaintext_key=dict(type="bool", required=True, no_log=True),
            key_id=dict(type="str", required=True),
            key_shape=dict(
                type="dict",
                required=True,
                no_log=False,
                options=dict(
                    algorithm=dict(
                        type="str", required=True, choices=["AES", "RSA", "ECDSA"]
                    ),
                    length=dict(type="int", required=True),
                    curve_id=dict(
                        type="str", choices=["NIST_P256", "NIST_P384", "NIST_P521"]
                    ),
                ),
            ),
            logging_context=dict(type="dict"),
            service_endpoint=dict(type="str", required=True),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="generated_key",
        service_client_class=KmsCryptoClient,
        namespace="key_management",
    )

    result = dict(changed=False)

    if resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
