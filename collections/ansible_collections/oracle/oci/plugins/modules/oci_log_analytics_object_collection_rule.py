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
module: oci_log_analytics_object_collection_rule
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_log_analytics_object_collection_rule_module.html)
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
    from oci.log_analytics import LogAnalyticsClient
    from oci.log_analytics.models import CreateLogAnalyticsObjectCollectionRuleDetails
    from oci.log_analytics.models import UpdateLogAnalyticsObjectCollectionRuleDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class LogAnalyticsObjectCollectionRuleHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            LogAnalyticsObjectCollectionRuleHelperGen, self
        ).get_possible_entity_types() + [
            "loganalyticsobjectcollectionrule",
            "loganalyticsobjectcollectionrules",
            "logAnalyticsloganalyticsobjectcollectionrule",
            "logAnalyticsloganalyticsobjectcollectionrules",
            "loganalyticsobjectcollectionruleresource",
            "loganalyticsobjectcollectionrulesresource",
            "loganalytics",
        ]

    def get_module_resource_id_param(self):
        return "log_analytics_object_collection_rule_id"

    def get_module_resource_id(self):
        return self.module.params.get("log_analytics_object_collection_rule_id")

    def get_get_fn(self):
        return self.client.get_log_analytics_object_collection_rule

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_log_analytics_object_collection_rule,
            log_analytics_object_collection_rule_id=summary_model.id,
            namespace_name=self.module.params.get("namespace_name"),
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_log_analytics_object_collection_rule,
            namespace_name=self.module.params.get("namespace_name"),
            log_analytics_object_collection_rule_id=self.module.params.get(
                "log_analytics_object_collection_rule_id"
            ),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "namespace_name",
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
        return oci_common_utils.list_all_resources(
            self.client.list_log_analytics_object_collection_rules, **kwargs
        )

    def get_create_model_class(self):
        return CreateLogAnalyticsObjectCollectionRuleDetails

    def get_exclude_attributes(self):
        return ["poll_since", "poll_till"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_log_analytics_object_collection_rule,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                create_log_analytics_object_collection_rule_details=create_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateLogAnalyticsObjectCollectionRuleDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_log_analytics_object_collection_rule,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                log_analytics_object_collection_rule_id=self.module.params.get(
                    "log_analytics_object_collection_rule_id"
                ),
                update_log_analytics_object_collection_rule_details=update_details,
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
            call_fn=self.client.delete_log_analytics_object_collection_rule,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                log_analytics_object_collection_rule_id=self.module.params.get(
                    "log_analytics_object_collection_rule_id"
                ),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


LogAnalyticsObjectCollectionRuleHelperCustom = get_custom_class(
    "LogAnalyticsObjectCollectionRuleHelperCustom"
)


class ResourceHelper(
    LogAnalyticsObjectCollectionRuleHelperCustom,
    LogAnalyticsObjectCollectionRuleHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            name=dict(type="str"),
            compartment_id=dict(type="str"),
            os_namespace=dict(type="str"),
            os_bucket_name=dict(type="str"),
            collection_type=dict(
                type="str", choices=["LIVE", "HISTORIC", "HISTORIC_LIVE"]
            ),
            poll_since=dict(type="str"),
            poll_till=dict(type="str"),
            description=dict(type="str"),
            log_group_id=dict(type="str"),
            log_source_name=dict(type="str"),
            entity_id=dict(type="str"),
            char_encoding=dict(type="str"),
            is_enabled=dict(type="bool"),
            timezone=dict(type="str"),
            log_set=dict(type="str"),
            log_set_key=dict(type="str", choices=["OBJECT_PATH"], no_log=True),
            log_set_ext_regex=dict(type="str"),
            overrides=dict(type="dict"),
            object_name_filters=dict(type="list", elements="str"),
            defined_tags=dict(type="dict"),
            freeform_tags=dict(type="dict"),
            namespace_name=dict(type="str", required=True),
            log_analytics_object_collection_rule_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="log_analytics_object_collection_rule",
        service_client_class=LogAnalyticsClient,
        namespace="log_analytics",
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
