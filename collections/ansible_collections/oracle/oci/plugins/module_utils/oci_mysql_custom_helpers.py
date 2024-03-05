# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible.module_utils import six

try:
    import oci
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

import logging

logger = logging.getLogger(__name__)


class MysqlDbSystemHelperCustom:

    # get model doesn't return admin_username and admin_password of existing database resources. Thus, excluding
    # these for idempotency.
    def get_update_model(self):
        # right now this happens to be the same as exclude attributes
        # if the service eventually supports updating username / password
        # we should empty this list and leave exlude attributes, thus I am
        # keeping them as separate
        # this is a unique case for this API because it has fields on the Update model
        # that are not possible to update
        update_attributes_not_present_on_get_model_which_dont_support_update = [
            "admin_password",
            "admin_username",
        ]
        existing_resource_dict = self.get_existing_resource_dict_for_update()
        params_to_pass_in_update_call = {}

        # MySQL UpdateDbSystem will throw an error if you specify any fields in the update request that the service
        # does not allow updating (which is most of the fields)
        # Thus, we only want to pass through values that are updated relative to the existing value on the resource
        # For example, if we pass subnet_id, even if it is set to the same value as resource.subnet_id the service will
        # throw an error, so we have custom logic to exclude it
        for key, input_value in six.iteritems(self.module.params):
            if (
                key
                in update_attributes_not_present_on_get_model_which_dont_support_update
            ):
                continue

            if input_value is not None and key in existing_resource_dict:
                existing_value = existing_resource_dict[key]
                values_are_equal = input_value == existing_value
                dicts_are_equivalent = (
                    isinstance(input_value, dict)
                    and isinstance(existing_value, dict)
                    and oci_common_utils.compare_dicts(input_value, existing_value)
                )
                if values_are_equal or dicts_are_equivalent:
                    logger.debug(
                        "skipping updating field {field_name} because it already matches the value on the resource.".format(
                            field_name=key
                        )
                    )
                    continue

            params_to_pass_in_update_call[key] = input_value

        return oci_common_utils.convert_input_data_to_model_class(
            params_to_pass_in_update_call, self.get_update_model_class()
        )


class MysqlBackupHelperCustom:
    # Handling backup creation using lifecycle state waiter due to below Jira-SD.
    # https://jira-sd.mc1.oracleiaas.com/browse/MYOPS-13837
    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_backup,
            call_fn_args=(),
            call_fn_kwargs=dict(create_backup_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY
            ),
        )


class MysqlAnalyticsClusterActionsHelperCustom:
    ADD_ACTION_KEY = "add"

    def perform_action(self, action):
        if action != self.ADD_ACTION_KEY:
            return super(MysqlAnalyticsClusterActionsHelperCustom, self).perform_action(
                action
            )

        try:
            db_system_get_response = oci_common_utils.call_with_backoff(
                self.client.get_db_system,
                db_system_id=self.module.params.get("db_system_id"),
            )
        except ServiceError as se:
            self.module.fail_json(
                msg="Getting db system failed with exception: {0}".format(se.message)
            )
        else:
            db_system = to_dict(db_system_get_response.data)

        if db_system.get("is_analytics_cluster_attached") or self.check_mode:
            resource = self.get_resource().data
            return self.prepare_result(
                changed=False,
                resource_type=self.get_response_field_name(action),
                resource=to_dict(resource),
            )

        try:
            actioned_resource = self.add()
        except MaximumWaitTimeExceeded as mwtex:
            self.module.fail_json(msg=str(mwtex))
        except ServiceError as se:
            self.module.fail_json(
                msg="Performing action failed with exception: {0}".format(se.message)
            )
        else:
            return self.prepare_result(
                changed=True,
                resource_type=self.get_response_field_name(action),
                resource=to_dict(actioned_resource),
            )


class MysqlAnalyticsClusterMemoryEstimateActionsHelperCustom:
    GENERATE_ACTION_KEY = "generate"

    def perform_action(self, action):
        if action != self.GENERATE_ACTION_KEY:
            return super(
                MysqlAnalyticsClusterMemoryEstimateActionsHelperCustom, self
            ).perform_action(action)

        try:
            oci_common_utils.call_with_backoff(
                self.client.generate_analytics_cluster_memory_estimate,
                db_system_id=self.module.params.get("db_system_id"),
            )
            initial_response = self.get_resource()
            wait_response = oci.wait_until(
                self.client,
                initial_response,
                evaluate_response=lambda response: response.data.status
                in oci_common_utils.WORK_REQUEST_COMPLETED_STATES,
                max_wait_seconds=self.get_wait_timeout(),
            )
            if wait_response.data and hasattr(wait_response.data, "status"):
                if (
                    wait_response.data.status
                    in oci_common_utils.WORK_REQUEST_FAILED_STATES
                ):
                    self.module.fail_json(msg="Generating memory estimate failed.")
            actioned_resource = wait_response.data
        except MaximumWaitTimeExceeded as mwtex:
            self.module.fail_json(msg=str(mwtex))
        except ServiceError as se:
            self.module.fail_json(
                msg="Performing action failed with exception: {0}".format(se.message)
            )
        else:
            return self.prepare_result(
                changed=True,
                resource_type=self.get_response_field_name(action),
                resource=to_dict(actioned_resource),
            )


class MysqlChannelHelperCustom:
    def update_resource(self):
        wait_states = oci_common_utils.DEFAULT_READY_STATES

        # the resource can be turned to inactive state by setting the option
        # is_enabled to False. That is a proper case and we should return back as
        # a successful operation when the resource enters Inactive state
        if self.module.params.get("is_enabled") is False:
            wait_states = ["INACTIVE"]

        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_channel,
            call_fn_args=(),
            call_fn_kwargs=dict(
                channel_id=self.module.params.get("channel_id"),
                update_channel_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=wait_states,
        )


class MysqlChannelActionsHelperCustom:
    # this action is being overridden as the channel goes from INACTIVE state to
    # INACTIVE state with the reset action. This change is not being picked up by
    # the waiter clent of mysql as it expects a SUCCESS in the return parameters
    def reset(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.reset_channel,
            call_fn_args=(),
            call_fn_kwargs=dict(channel_id=self.module.params.get("channel_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            # waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=["INACTIVE"],
        )


class MysqlHeatWaveClusterActionsHelperCustom:
    ADD_ACTION_KEY = "add"

    def perform_action(self, action):
        if action != self.ADD_ACTION_KEY:
            return super(MysqlHeatWaveClusterActionsHelperCustom, self).perform_action(
                action
            )

        try:
            db_system_get_response = oci_common_utils.call_with_backoff(
                self.client.get_db_system,
                db_system_id=self.module.params.get("db_system_id"),
            )
        except ServiceError as se:
            self.module.fail_json(
                msg="Getting db system failed with exception: {0}".format(se.message)
            )
        else:
            db_system = to_dict(db_system_get_response.data)

        if db_system.get("is_analytics_cluster_attached") or self.check_mode:
            resource = self.get_resource().data
            return self.prepare_result(
                changed=False,
                resource_type=self.get_response_field_name(action),
                resource=to_dict(resource),
            )

        try:
            actioned_resource = self.add()
        except MaximumWaitTimeExceeded as mwtex:
            self.module.fail_json(msg=str(mwtex))
        except ServiceError as se:
            self.module.fail_json(
                msg="Performing action failed with exception: {0}".format(se.message)
            )
        else:
            return self.prepare_result(
                changed=True,
                resource_type=self.get_response_field_name(action),
                resource=to_dict(actioned_resource),
            )


class MysqlHeatWaveClusterMemoryEstimateActionsHelperCustom:
    GENERATE_ACTION_KEY = "generate"

    def perform_action(self, action):
        if action != self.GENERATE_ACTION_KEY:
            return super(
                MysqlHeatWaveClusterMemoryEstimateActionsHelperCustom, self
            ).perform_action(action)

        try:
            oci_common_utils.call_with_backoff(
                self.client.generate_heat_wave_cluster_memory_estimate,
                db_system_id=self.module.params.get("db_system_id"),
            )
            initial_response = self.get_resource()
            wait_response = oci.wait_until(
                self.client,
                initial_response,
                evaluate_response=lambda response: response.data.status
                in oci_common_utils.WORK_REQUEST_COMPLETED_STATES,
                max_wait_seconds=self.get_wait_timeout(),
            )
            if wait_response.data and hasattr(wait_response.data, "status"):
                if (
                    wait_response.data.status
                    in oci_common_utils.WORK_REQUEST_FAILED_STATES
                ):
                    self.module.fail_json(msg="Generating memory estimate failed.")
            actioned_resource = wait_response.data
        except MaximumWaitTimeExceeded as mwtex:
            self.module.fail_json(msg=str(mwtex))
        except ServiceError as se:
            self.module.fail_json(
                msg="Performing action failed with exception: {0}".format(se.message)
            )
        else:
            return self.prepare_result(
                changed=True,
                resource_type=self.get_response_field_name(action),
                resource=to_dict(actioned_resource),
            )
