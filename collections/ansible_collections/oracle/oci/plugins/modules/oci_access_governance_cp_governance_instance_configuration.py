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
module: oci_access_governance_cp_governance_instance_configuration
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_access_governance_cp_governance_instance_configuration_module.html)
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
    from oci.access_governance_cp import AccessGovernanceCPClient
    from oci.access_governance_cp.models import (
        UpdateGovernanceInstanceConfigurationDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class GovernanceInstanceConfigurationHelperGen(OCIResourceHelperBase):
    """Supported operations: update and get"""

    def get_possible_entity_types(self):
        return super(
            GovernanceInstanceConfigurationHelperGen, self
        ).get_possible_entity_types() + [
            "governanceinstanceconfiguration",
            "governanceinstanceconfigurations",
            "accessGovernanceCpgovernanceinstanceconfiguration",
            "accessGovernanceCpgovernanceinstanceconfigurations",
            "governanceinstanceconfigurationresource",
            "governanceinstanceconfigurationsresource",
            "configuration",
            "configurations",
            "accessGovernanceCpconfiguration",
            "accessGovernanceCpconfigurations",
            "configurationresource",
            "configurationsresource",
            "accessgovernancecp",
        ]

    def get_get_fn(self):
        return self.client.get_governance_instance_configuration

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_governance_instance_configuration,
            compartment_id=self.module.params.get("compartment_id"),
        )

    def get_update_model_class(self):
        return UpdateGovernanceInstanceConfigurationDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_governance_instance_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                update_governance_instance_configuration_details=update_details,
                compartment_id=self.module.params.get("compartment_id"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )


GovernanceInstanceConfigurationHelperCustom = get_custom_class(
    "GovernanceInstanceConfigurationHelperCustom"
)


class ResourceHelper(
    GovernanceInstanceConfigurationHelperCustom,
    GovernanceInstanceConfigurationHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            sender_info=dict(
                type="dict",
                options=dict(
                    display_name=dict(aliases=["name"], type="str"),
                    email=dict(type="str", required=True),
                    is_inbox_configured=dict(type="bool", required=True),
                    is_resend_notification_email=dict(type="bool"),
                ),
            ),
            compartment_id=dict(type="str", required=True),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="governance_instance_configuration",
        service_client_class=AccessGovernanceCPClient,
        namespace="access_governance_cp",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
