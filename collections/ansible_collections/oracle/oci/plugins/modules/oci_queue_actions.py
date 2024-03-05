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
module: oci_queue_actions
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_queue_actions_module.html)
    for the module documentation.
author: Oracle (@oracle)
"""


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
    from oci.queue import QueueAdminClient
    from oci.queue.models import ChangeQueueCompartmentDetails
    from oci.queue.models import PurgeQueueDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class QueueActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        purge
    """

    @staticmethod
    def get_module_resource_id_param():
        return "queue_id"

    def get_module_resource_id(self):
        return self.module.params.get("queue_id")

    def get_get_fn(self):
        return self.client.get_queue

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_queue, queue_id=self.module.params.get("queue_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeQueueCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_queue_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                queue_id=self.module.params.get("queue_id"),
                change_queue_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def purge(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, PurgeQueueDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.purge_queue,
            call_fn_args=(),
            call_fn_kwargs=dict(
                queue_id=self.module.params.get("queue_id"),
                purge_queue_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


QueueActionsHelperCustom = get_custom_class("QueueActionsHelperCustom")


class ResourceHelper(QueueActionsHelperCustom, QueueActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            queue_id=dict(aliases=["id"], type="str", required=True),
            purge_type=dict(type="str", choices=["NORMAL", "DLQ", "BOTH"]),
            action=dict(
                type="str", required=True, choices=["change_compartment", "purge"]
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="queue",
        service_client_class=QueueAdminClient,
        namespace="queue",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
