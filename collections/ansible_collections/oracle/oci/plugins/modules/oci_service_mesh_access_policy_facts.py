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
module: oci_service_mesh_access_policy_facts
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_service_mesh_access_policy_facts_module.html)
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
    from oci.service_mesh import ServiceMeshClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AccessPolicyFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "access_policy_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_access_policy,
            access_policy_id=self.module.params.get("access_policy_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "name",
            "sort_order",
            "sort_by",
            "mesh_id",
            "lifecycle_state",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_access_policies,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


AccessPolicyFactsHelperCustom = get_custom_class("AccessPolicyFactsHelperCustom")


class ResourceFactsHelper(AccessPolicyFactsHelperCustom, AccessPolicyFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            access_policy_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            name=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["id", "timeCreated", "name"]),
            mesh_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="access_policy",
        service_client_class=ServiceMeshClient,
        namespace="service_mesh",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(access_policies=result)


if __name__ == "__main__":
    main()
