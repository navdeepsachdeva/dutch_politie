# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils

try:
    from oci.log_analytics.models import Namespace
    from oci.exceptions import ServiceError
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class NamespaceActionsHelperCustom:
    # As per API documentation `GetNamespace` gets the namespace details of a tenancy already on-boarded.
    # if tenancy is off-boarded API returns 404.
    def get_resource(self):
        return oci_common_utils.get_default_response_from_resource(
            resource=oci_common_utils.convert_input_data_to_model_class(
                self.module.params, Namespace
            )
        )

    def is_action_necessary(self, action, resource=None):

        # check if tenancy is already on-boarded
        if action == "onboard":
            try:
                oci_common_utils.call_with_backoff(
                    self.client.get_namespace,
                    namespace_name=self.module.params.get("namespace_name"),
                )
                return False
            except ServiceError as se:
                if se.status == 404:
                    return True
                self.module.fail_json(msg=se.message)

        # check if tenancy is already off-boarded
        elif action == "offboard":
            try:
                oci_common_utils.call_with_backoff(
                    self.client.get_namespace,
                    namespace_name=self.module.params.get("namespace_name"),
                )
                return True
            except ServiceError as se:
                if se.status == 404:
                    return False
                self.module.fail_json(msg=se.message)

        return super(NamespaceActionsHelperCustom, self).is_action_necessary(
            action, resource
        )


class LogAnalyticsEntityHelperCustom:
    def get_update_model(self):
        # updating name is not supported yet by the service team. In the update using id scenario, the user
        # can just skip sending this field. But in update using name scenario, we expect the user to pass the
        # name and it is populated in the update model since it exists in the model. API throws an error in this
        # case even though the name is same. So remove the name parameter from the update model.
        update_model = super(LogAnalyticsEntityHelperCustom, self).get_update_model()
        if self._use_name_as_identifier:
            setattr(update_model, "name", None)
        return update_model


class LogAnalyticsEntityActionsHelperCustom:
    ADD_ENTITY_ASSOCIATION_KEY = "add_entity_association"
    REMOVE_ENTITY_ASSOCIATIONS_KEY = "remove_entity_associations"
    ASSOCIATION_ENTITIES_KEY = "association_entities"

    def list_associated_entities(self, entity):
        return oci_common_utils.list_all_resources(
            self.client.list_associated_entities,
            namespace_name=self.module.params.get("namespace_name"),
            compartment_id=entity.compartment_id,
            entity_id=entity.id,
        )

    def is_action_necessary(self, action, resource=None):
        resource = resource or self.get_resource().data
        if action in [
            self.ADD_ENTITY_ASSOCIATION_KEY,
            self.REMOVE_ENTITY_ASSOCIATIONS_KEY,
        ]:
            if self.module.params.get(self.ASSOCIATION_ENTITIES_KEY) is None:
                self.module.fail_json(
                    msg="association_entities required for this action."
                )
        if action == self.ADD_ENTITY_ASSOCIATION_KEY:
            existing_associated_entities = self.list_associated_entities(resource)
            for associated_entity in self.module.params.get(
                self.ASSOCIATION_ENTITIES_KEY
            ):
                if associated_entity not in existing_associated_entities:
                    return True
            return False
        elif action == self.REMOVE_ENTITY_ASSOCIATIONS_KEY:
            existing_associated_entities = self.list_associated_entities(resource)
            for associated_entity in self.module.params.get(
                self.ASSOCIATION_ENTITIES_KEY
            ):
                if associated_entity in existing_associated_entities:
                    return True
            return False
        return super(LogAnalyticsEntityActionsHelperCustom, self).is_action_necessary(
            action, resource
        )


class LogAnalyticsEntityTypeHelperCustom:
    def create_resource(self):
        super(LogAnalyticsEntityTypeHelperCustom, self).create_resource()
        return self.get_resource().data

    def delete_resource(self):
        super(LogAnalyticsEntityTypeHelperCustom, self).delete_resource()
        return self.get_resource().data


class LogAnalyticsObjectCollectionRuleHelperCustom:
    # If is_enabled = false, Resource goes in INACTIVE state. After performing update operation,
    # we currently wait for only ACTIVE state and FAILED state. Adding INACTIVE state as a wait state.
    def get_wait_for_states_for_operation(self, operation):
        if operation == oci_common_utils.UPDATE_OPERATION_KEY:
            wait_for_states = self.get_resource_active_states()
            wait_for_states.append("INACTIVE")
            return wait_for_states
        else:
            return super(
                LogAnalyticsObjectCollectionRuleHelperCustom, self
            ).get_wait_for_states_for_operation(operation)


class ImportCustomContentActionsHelperCustom:
    # As we have created separate module for this action,
    # we are copying get_resource() method from actual resource.
    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_namespace,
            namespace_name=self.module.params.get("namespace_name"),
        )

    # Adding this override to handle passing file path instead of passing binary data.
    def import_custom_content(self):
        file_path = self.module.params.get("import_custom_content_file_body_input_file")
        try:
            with open(file_path, "rb") as input_file:
                self.module.params["import_custom_content_file_body"] = input_file
                resource = super(
                    ImportCustomContentActionsHelperCustom, self
                ).import_custom_content()
                self.module.params.pop("import_custom_content_file_body", None)
                return resource
        finally:
            self.module.params.pop("import_custom_content_file_body", None)


class PreferencesManagementActionsHelperCustom:
    UPDATE_PREFERENCES_ACTION = "update_preferences"
    REMOVE_PREFERENCES_ACTION = "remove_preferences"

    # Preferences Management resource doesn't support get operation.
    def get_resource(self):
        return oci_common_utils.get_default_response_from_resource(
            oci_common_utils.list_all_resources(
                self.client.get_preferences,
                namespace_name=self.module.params.get("namespace_name"),
            )
        )

    # Handling idempotency for `update_preferences` & `remove_preferences` action operations.
    def is_action_necessary(self, action, resource=None):
        resource_dict = to_dict(resource)
        if action.lower() == self.UPDATE_PREFERENCES_ACTION:
            source_list = self.module.params.get("items")
            for item_dict in source_list:
                if item_dict not in resource_dict:
                    return True
            return False
        elif action.lower() == self.REMOVE_PREFERENCES_ACTION:
            source_list = self.module.params.get("items")
            for item_dict in source_list:
                if item_dict in resource_dict:
                    return True
            return False
        return super(
            PreferencesManagementActionsHelperCustom, self
        ).is_action_necessary(action, resource)


class UnprocessedDataBucketFactsHelperCustom:
    def get_resource(self):
        """ hanlding the service error for 404. This response means the resource does not exist"""
        try:
            return oci_common_utils.call_with_backoff(
                self.client.get_unprocessed_data_bucket,
                namespace_name=self.module.params.get("namespace_name"),
            )
        # first time `set_unprocessed_data_bucket` action should be performed for bucket.
        # otherwise, 404 error is received.
        except ServiceError as se:
            if se.status == 404 and se.code == "NotAuthorizedOrNotFound":
                return oci_common_utils.get_default_response_from_resource(
                    resource=None
                )
            raise


class UnprocessedDataBucketActionsHelperCustom:
    SET_ACTION = "set"

    def is_action_necessary(self, action, resource=None):
        if action.lower() == self.SET_ACTION:
            if (
                resource is not None
                and self.module.params.get("bucket_name") == resource.bucket_name
            ):
                return False
        return super(
            UnprocessedDataBucketActionsHelperCustom, self
        ).is_action_necessary(action, resource)
