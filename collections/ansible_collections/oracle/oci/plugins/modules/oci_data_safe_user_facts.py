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
module: oci_data_safe_user_facts
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_data_safe_user_facts_module.html)
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
    from oci.data_safe import DataSafeClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataSafeUserFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "user_assessment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id_in_subtree",
            "access_level",
            "user_category",
            "user_role",
            "user_profile",
            "user_type",
            "user_key",
            "account_status",
            "authentication_type",
            "user_name",
            "target_id",
            "time_last_login_greater_than_or_equal_to",
            "time_last_login_less_than",
            "time_user_created_greater_than_or_equal_to",
            "time_user_created_less_than",
            "time_password_last_changed_greater_than_or_equal_to",
            "time_password_last_changed_less_than",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_users,
            user_assessment_id=self.module.params.get("user_assessment_id"),
            **optional_kwargs
        )


DataSafeUserFactsHelperCustom = get_custom_class("DataSafeUserFactsHelperCustom")


class ResourceFactsHelper(DataSafeUserFactsHelperCustom, DataSafeUserFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            user_assessment_id=dict(type="str", required=True),
            compartment_id_in_subtree=dict(type="bool"),
            access_level=dict(type="str", choices=["RESTRICTED", "ACCESSIBLE"]),
            user_category=dict(type="str"),
            user_role=dict(type="str"),
            user_profile=dict(type="str"),
            user_type=dict(type="str"),
            user_key=dict(type="str", no_log=True),
            account_status=dict(type="str"),
            authentication_type=dict(type="str"),
            user_name=dict(type="str"),
            target_id=dict(type="str"),
            time_last_login_greater_than_or_equal_to=dict(type="str"),
            time_last_login_less_than=dict(type="str"),
            time_user_created_greater_than_or_equal_to=dict(type="str"),
            time_user_created_less_than=dict(type="str"),
            time_password_last_changed_greater_than_or_equal_to=dict(
                type="str", no_log=True
            ),
            time_password_last_changed_less_than=dict(type="str", no_log=True),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(
                type="str",
                choices=[
                    "userName",
                    "userCategory",
                    "accountStatus",
                    "timeLastLogin",
                    "targetId",
                    "timeUserCreated",
                    "authenticationType",
                    "timePasswordChanged",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="user",
        service_client_class=DataSafeClient,
        namespace="data_safe",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(users=result)


if __name__ == "__main__":
    main()
