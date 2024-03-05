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
module: oci_usage_schedule
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_usage_schedule_module.html)
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
    from oci.usage_api import UsageapiClient
    from oci.usage_api.models import CreateScheduleDetails
    from oci.usage_api.models import UpdateScheduleDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ScheduleHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(ScheduleHelperGen, self).get_possible_entity_types() + [
            "schedule",
            "schedules",
            "usageApischedule",
            "usageApischedules",
            "scheduleresource",
            "schedulesresource",
            "usageapi",
        ]

    def get_module_resource_id_param(self):
        return "schedule_id"

    def get_module_resource_id(self):
        return self.module.params.get("schedule_id")

    def get_get_fn(self):
        return self.client.get_schedule

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_schedule, schedule_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_schedule, schedule_id=self.module.params.get("schedule_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["name"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(self.client.list_schedules, **kwargs)

    def get_create_model_class(self):
        return CreateScheduleDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_schedule,
            call_fn_args=(),
            call_fn_kwargs=dict(create_schedule_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateScheduleDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_schedule,
            call_fn_args=(),
            call_fn_kwargs=dict(
                update_schedule_details=update_details,
                schedule_id=self.module.params.get("schedule_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_schedule,
            call_fn_args=(),
            call_fn_kwargs=dict(schedule_id=self.module.params.get("schedule_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


ScheduleHelperCustom = get_custom_class("ScheduleHelperCustom")


class ResourceHelper(ScheduleHelperCustom, ScheduleHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            name=dict(type="str"),
            compartment_id=dict(type="str"),
            saved_report_id=dict(type="str"),
            schedule_recurrences=dict(type="str"),
            time_scheduled=dict(type="str"),
            query_properties=dict(
                type="dict",
                options=dict(
                    group_by=dict(type="list", elements="str"),
                    group_by_tag=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            namespace=dict(type="str"),
                            key=dict(type="str", no_log=True),
                            value=dict(type="str"),
                        ),
                    ),
                    filter=dict(
                        type="dict",
                        options=dict(
                            operator=dict(type="str", choices=["AND", "NOT", "OR"]),
                            dimensions=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    key=dict(type="str", required=True, no_log=True),
                                    value=dict(type="str", required=True),
                                ),
                            ),
                            tags=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    namespace=dict(type="str"),
                                    key=dict(type="str", no_log=True),
                                    value=dict(type="str"),
                                ),
                            ),
                            filters=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    operator=dict(
                                        type="str", choices=["AND", "NOT", "OR"]
                                    ),
                                    dimensions=dict(type="list", elements="dict"),
                                    tags=dict(type="list", elements="dict"),
                                    filters=dict(type="list", elements="dict"),
                                ),
                            ),
                        ),
                    ),
                    compartment_depth=dict(type="float"),
                    granularity=dict(
                        type="str", required=True, choices=["DAILY", "MONTHLY"]
                    ),
                    query_type=dict(
                        type="str", choices=["USAGE", "COST", "USAGE_AND_COST"]
                    ),
                    is_aggregate_by_time=dict(type="bool"),
                    date_range=dict(
                        type="dict",
                        required=True,
                        options=dict(
                            time_usage_started=dict(type="str"),
                            time_usage_ended=dict(type="str"),
                            date_range_type=dict(
                                type="str", required=True, choices=["STATIC", "DYNAMIC"]
                            ),
                            dynamic_date_range_type=dict(
                                type="str",
                                choices=[
                                    "LAST_7_DAYS",
                                    "LAST_10_DAYS",
                                    "LAST_CALENDAR_WEEK",
                                    "LAST_CALENDAR_MONTH",
                                    "LAST_2_CALENDAR_MONTHS",
                                    "LAST_3_CALENDAR_MONTHS",
                                    "LAST_6_CALENDAR_MONTHS",
                                    "LAST_30_DAYS",
                                    "MONTH_TO_DATE",
                                    "LAST_YEAR",
                                    "YEAR_TODATE",
                                    "ALL",
                                ],
                            ),
                        ),
                    ),
                ),
            ),
            description=dict(type="str"),
            output_file_format=dict(type="str", choices=["CSV", "PDF"]),
            result_location=dict(
                type="dict",
                options=dict(
                    location_type=dict(
                        type="str", required=True, choices=["OBJECT_STORAGE"]
                    ),
                    region=dict(type="str", required=True),
                    namespace=dict(type="str", required=True),
                    bucket_name=dict(type="str", required=True),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            schedule_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="schedule",
        service_client_class=UsageapiClient,
        namespace="usage_api",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
