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
module: oci_management_dashboard_actions
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_management_dashboard_actions_module.html)
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
    from oci.management_dashboard import DashxApisClient
    from oci.management_dashboard.models import ManagementDashboardImportDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ManagementDashboardActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        export_dashboard
        import_dashboard
    """

    def get_get_fn(self):
        return self.client.get_management_dashboard

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_management_dashboard,
            management_dashboard_id=self.module.params.get("management_dashboard_id"),
        )

    def export_dashboard(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.export_dashboard,
            call_fn_args=(),
            call_fn_kwargs=dict(
                export_dashboard_id=self.module.params.get("export_dashboard_id"),
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

    def import_dashboard(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ManagementDashboardImportDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.import_dashboard,
            call_fn_args=(),
            call_fn_kwargs=dict(management_dashboard_import_details=action_details,),
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


ManagementDashboardActionsHelperCustom = get_custom_class(
    "ManagementDashboardActionsHelperCustom"
)


class ResourceHelper(
    ManagementDashboardActionsHelperCustom, ManagementDashboardActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            export_dashboard_id=dict(type="str"),
            dashboards=dict(
                type="list",
                elements="dict",
                options=dict(
                    dashboard_id=dict(type="str", required=True),
                    provider_id=dict(type="str", required=True),
                    provider_name=dict(type="str", required=True),
                    provider_version=dict(type="str", required=True),
                    tiles=dict(
                        type="list",
                        elements="dict",
                        required=True,
                        options=dict(
                            display_name=dict(
                                aliases=["name"], type="str", required=True
                            ),
                            saved_search_id=dict(type="str", required=True),
                            row=dict(type="int", required=True),
                            column=dict(type="int", required=True),
                            height=dict(type="int", required=True),
                            width=dict(type="int", required=True),
                            nls=dict(type="dict", required=True),
                            ui_config=dict(type="dict", required=True),
                            data_config=dict(
                                type="list", elements="dict", required=True
                            ),
                            state=dict(
                                type="str",
                                required=True,
                                choices=["DELETED", "UNAUTHORIZED", "DEFAULT"],
                            ),
                            drilldown_config=dict(type="list", required=True),
                            parameters_map=dict(type="dict"),
                        ),
                    ),
                    display_name=dict(aliases=["name"], type="str", required=True),
                    description=dict(type="str", required=True),
                    compartment_id=dict(type="str", required=True),
                    is_oob_dashboard=dict(type="bool", required=True),
                    is_show_in_home=dict(type="bool", required=True),
                    metadata_version=dict(type="str", required=True),
                    is_show_description=dict(type="bool", required=True),
                    screen_image=dict(type="str", required=True),
                    nls=dict(type="dict", required=True),
                    ui_config=dict(type="dict", required=True),
                    data_config=dict(type="list", elements="dict", required=True),
                    type=dict(type="str", required=True),
                    is_favorite=dict(type="bool", required=True),
                    saved_searches=dict(
                        type="list",
                        elements="dict",
                        required=True,
                        options=dict(
                            id=dict(type="str", required=True),
                            display_name=dict(
                                aliases=["name"], type="str", required=True
                            ),
                            provider_id=dict(type="str", required=True),
                            provider_version=dict(type="str", required=True),
                            provider_name=dict(type="str", required=True),
                            compartment_id=dict(type="str", required=True),
                            is_oob_saved_search=dict(type="bool", required=True),
                            description=dict(type="str", required=True),
                            nls=dict(type="dict", required=True),
                            type=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "SEARCH_SHOW_IN_DASHBOARD",
                                    "SEARCH_DONT_SHOW_IN_DASHBOARD",
                                    "WIDGET_SHOW_IN_DASHBOARD",
                                    "WIDGET_DONT_SHOW_IN_DASHBOARD",
                                    "FILTER_SHOW_IN_DASHBOARD",
                                    "FILTER_DONT_SHOW_IN_DASHBOARD",
                                ],
                            ),
                            ui_config=dict(type="dict", required=True),
                            data_config=dict(
                                type="list", elements="dict", required=True
                            ),
                            screen_image=dict(type="str", required=True),
                            metadata_version=dict(type="str", required=True),
                            widget_template=dict(type="str", required=True),
                            widget_vm=dict(type="str", required=True),
                            freeform_tags=dict(type="dict"),
                            defined_tags=dict(type="dict"),
                            parameters_config=dict(type="list", elements="dict"),
                            features_config=dict(type="dict"),
                            drilldown_config=dict(type="list", elements="dict"),
                        ),
                    ),
                    parameters_config=dict(type="list", elements="dict"),
                    features_config=dict(type="dict"),
                    drilldown_config=dict(type="list", elements="dict"),
                    freeform_tags=dict(type="dict"),
                    defined_tags=dict(type="dict"),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            action=dict(
                type="str",
                required=True,
                choices=["export_dashboard", "import_dashboard"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="management_dashboard",
        service_client_class=DashxApisClient,
        namespace="management_dashboard",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
