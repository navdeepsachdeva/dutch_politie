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
module: oci_stack_monitoring_monitored_resource
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_stack_monitoring_monitored_resource_module.html)
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
    from oci.stack_monitoring import StackMonitoringClient
    from oci.stack_monitoring.models import CreateMonitoredResourceDetails
    from oci.stack_monitoring.models import UpdateMonitoredResourceDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MonitoredResourceHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get and delete"""

    def get_possible_entity_types(self):
        return super(MonitoredResourceHelperGen, self).get_possible_entity_types() + [
            "stackmonitoringresource",
            "stackmonitoringresources",
            "stackMonitoringstackmonitoringresource",
            "stackMonitoringstackmonitoringresources",
            "stackmonitoringresourceresource",
            "stackmonitoringresourcesresource",
            "monitoredresource",
            "monitoredresources",
            "stackMonitoringmonitoredresource",
            "stackMonitoringmonitoredresources",
            "monitoredresourceresource",
            "monitoredresourcesresource",
            "stackmonitoring",
        ]

    def get_module_resource_id_param(self):
        return "monitored_resource_id"

    def get_module_resource_id(self):
        return self.module.params.get("monitored_resource_id")

    def get_get_fn(self):
        return self.client.get_monitored_resource

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_monitored_resource,
            monitored_resource_id=self.module.params.get("monitored_resource_id"),
        )

    def get_create_model_class(self):
        return CreateMonitoredResourceDetails

    def get_exclude_attributes(self):
        return ["additional_aliases", "additional_credentials"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_monitored_resource,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_monitored_resource_details=create_details,
                external_resource_id=self.module.params.get("external_resource_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateMonitoredResourceDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_monitored_resource,
            call_fn_args=(),
            call_fn_kwargs=dict(
                monitored_resource_id=self.module.params.get("monitored_resource_id"),
                update_monitored_resource_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_monitored_resource,
            call_fn_args=(),
            call_fn_kwargs=dict(
                monitored_resource_id=self.module.params.get("monitored_resource_id"),
                is_delete_members=self.module.params.get("is_delete_members"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


MonitoredResourceHelperCustom = get_custom_class("MonitoredResourceHelperCustom")


class ResourceHelper(MonitoredResourceHelperCustom, MonitoredResourceHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            name=dict(type="str"),
            type=dict(type="str"),
            compartment_id=dict(type="str"),
            external_id=dict(type="str"),
            management_agent_id=dict(type="str"),
            external_resource_id=dict(type="str"),
            display_name=dict(type="str"),
            host_name=dict(type="str"),
            resource_time_zone=dict(type="str"),
            properties=dict(
                type="list",
                elements="dict",
                options=dict(name=dict(type="str"), value=dict(type="str")),
            ),
            database_connection_details=dict(
                type="dict",
                options=dict(
                    protocol=dict(type="str", required=True, choices=["TCP", "TCPS"]),
                    port=dict(type="int", required=True),
                    connector_id=dict(type="str"),
                    service_name=dict(type="str", required=True),
                    db_unique_name=dict(type="str"),
                    db_id=dict(type="str"),
                    ssl_secret_id=dict(type="str"),
                ),
            ),
            credentials=dict(
                type="dict",
                options=dict(
                    key_id=dict(type="str"),
                    source=dict(type="str"),
                    name=dict(type="str"),
                    type=dict(type="str"),
                    description=dict(type="str"),
                    credential_type=dict(
                        type="str",
                        required=True,
                        choices=["EXISTING", "ENCRYPTED", "PLAINTEXT"],
                    ),
                    properties=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            name=dict(type="str", required=True),
                            value=dict(type="str", required=True),
                        ),
                    ),
                ),
            ),
            aliases=dict(
                type="dict",
                options=dict(
                    source=dict(type="str", required=True),
                    name=dict(type="str", required=True),
                    credential=dict(
                        type="dict",
                        required=True,
                        options=dict(
                            source=dict(type="str", required=True),
                            name=dict(type="str", required=True),
                            service=dict(type="str", required=True),
                        ),
                    ),
                ),
            ),
            additional_credentials=dict(
                type="list",
                elements="dict",
                options=dict(
                    key_id=dict(type="str"),
                    source=dict(type="str"),
                    name=dict(type="str"),
                    type=dict(type="str"),
                    description=dict(type="str"),
                    credential_type=dict(
                        type="str",
                        required=True,
                        choices=["EXISTING", "ENCRYPTED", "PLAINTEXT"],
                    ),
                    properties=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            name=dict(type="str", required=True),
                            value=dict(type="str", required=True),
                        ),
                    ),
                ),
            ),
            additional_aliases=dict(
                type="list",
                elements="dict",
                options=dict(
                    source=dict(type="str", required=True),
                    name=dict(type="str", required=True),
                    credential=dict(
                        type="dict",
                        required=True,
                        options=dict(
                            source=dict(type="str", required=True),
                            name=dict(type="str", required=True),
                            service=dict(type="str", required=True),
                        ),
                    ),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            monitored_resource_id=dict(aliases=["id"], type="str"),
            is_delete_members=dict(type="bool"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="monitored_resource",
        service_client_class=StackMonitoringClient,
        namespace="stack_monitoring",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
