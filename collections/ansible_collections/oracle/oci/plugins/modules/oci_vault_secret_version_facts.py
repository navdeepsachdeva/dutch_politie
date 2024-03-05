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
module: oci_vault_secret_version_facts
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_vault_secret_version_facts_module.html)
    for the module documentation.
author: Oracle (@oracle)
"""


from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.vault import VaultsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SecretVersionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "secret_id",
            "secret_version_number",
        ]

    def get_required_params_for_list(self):
        return [
            "secret_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_secret_version,
            secret_id=self.module.params.get("secret_id"),
            secret_version_number=self.module.params.get("secret_version_number"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "sort_by",
            "sort_order",
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_secret_versions,
            secret_id=self.module.params.get("secret_id"),
            **optional_kwargs
        )


SecretVersionFactsHelperCustom = get_custom_class("SecretVersionFactsHelperCustom")


class ResourceFactsHelper(SecretVersionFactsHelperCustom, SecretVersionFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            secret_version_number=dict(type="int", no_log=True),
            secret_id=dict(type="str", required=True),
            sort_by=dict(type="str", choices=["VERSION_NUMBER"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="secret_version",
        service_client_class=VaultsClient,
        namespace="vault",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(secret_versions=result)


if __name__ == "__main__":
    main()
