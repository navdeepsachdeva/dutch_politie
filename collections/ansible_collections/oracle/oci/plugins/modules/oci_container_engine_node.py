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
module: oci_container_engine_node
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_container_engine_node_module.html)
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
    from oci.container_engine import ContainerEngineClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class NodeHelperGen(OCIResourceHelperBase):
    """Supported operations: delete"""

    def get_possible_entity_types(self):
        return super(NodeHelperGen, self).get_possible_entity_types() + [
            "node",
            "nodes",
            "containerEnginenode",
            "containerEnginenodes",
            "noderesource",
            "nodesresource",
            "containerengine",
        ]

    def get_module_resource_id_param(self):
        return "node_id"

    def get_module_resource_id(self):
        return self.module.params.get("node_id")

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_node,
            call_fn_args=(),
            call_fn_kwargs=dict(
                node_pool_id=self.module.params.get("node_pool_id"),
                node_id=self.module.params.get("node_id"),
                is_decrement_size=self.module.params.get("is_decrement_size"),
                override_eviction_grace_duration=self.module.params.get(
                    "override_eviction_grace_duration"
                ),
                is_force_deletion_after_override_grace_duration=self.module.params.get(
                    "is_force_deletion_after_override_grace_duration"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


NodeHelperCustom = get_custom_class("NodeHelperCustom")


class ResourceHelper(NodeHelperCustom, NodeHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            node_pool_id=dict(type="str", required=True),
            node_id=dict(aliases=["id"], type="str", required=True),
            is_decrement_size=dict(type="bool"),
            override_eviction_grace_duration=dict(type="str"),
            is_force_deletion_after_override_grace_duration=dict(type="bool"),
            state=dict(type="str", default="present", choices=["absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="node",
        service_client_class=ContainerEngineClient,
        namespace="container_engine",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
