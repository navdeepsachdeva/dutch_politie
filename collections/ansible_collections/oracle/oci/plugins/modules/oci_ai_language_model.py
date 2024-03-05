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
module: oci_ai_language_model
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_ai_language_model_module.html)
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
    from oci.ai_language import AIServiceLanguageClient
    from oci.ai_language.models import CreateModelDetails
    from oci.ai_language.models import UpdateModelDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AiLanguageModelHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(AiLanguageModelHelperGen, self).get_possible_entity_types() + [
            "ailanguagemodelpre",
            "ailanguagemodelpres",
            "aiLanguageailanguagemodelpre",
            "aiLanguageailanguagemodelpres",
            "ailanguagemodelpreresource",
            "ailanguagemodelpresresource",
            "model",
            "models",
            "aiLanguagemodel",
            "aiLanguagemodels",
            "modelresource",
            "modelsresource",
            "ailanguage",
        ]

    def get_module_resource_id_param(self):
        return "model_id"

    def get_module_resource_id(self):
        return self.module.params.get("model_id")

    def get_get_fn(self):
        return self.client.get_model

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_model, model_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_model, model_id=self.module.params.get("model_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["model_id", "project_id", "display_name"]

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
        return oci_common_utils.list_all_resources(self.client.list_models, **kwargs)

    def get_create_model_class(self):
        return CreateModelDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_model,
            call_fn_args=(),
            call_fn_kwargs=dict(create_model_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateModelDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_model,
            call_fn_args=(),
            call_fn_kwargs=dict(
                model_id=self.module.params.get("model_id"),
                update_model_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_model,
            call_fn_args=(),
            call_fn_kwargs=dict(model_id=self.module.params.get("model_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


AiLanguageModelHelperCustom = get_custom_class("AiLanguageModelHelperCustom")


class ResourceHelper(AiLanguageModelHelperCustom, AiLanguageModelHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            project_id=dict(type="str"),
            model_details=dict(
                type="dict",
                options=dict(
                    classification_mode=dict(
                        type="dict",
                        options=dict(
                            classification_mode=dict(
                                type="str",
                                required=True,
                                choices=["MULTI_CLASS", "MULTI_LABEL"],
                            ),
                            version=dict(type="str"),
                        ),
                    ),
                    language_code=dict(type="str"),
                    model_type=dict(
                        type="str",
                        required=True,
                        choices=[
                            "PRE_TRAINED_KEYPHRASE_EXTRACTION",
                            "PRE_TRAINED_HEALTH_NLU",
                            "PRE_TRAINED_UNIVERSAL",
                            "NAMED_ENTITY_RECOGNITION",
                            "PRE_TRAINED_LANGUAGE_DETECTION",
                            "PRE_TRAINED_NAMED_ENTITY_RECOGNITION",
                            "PRE_TRAINED_SENTIMENT_ANALYSIS",
                            "PRE_TRAINED_PHI",
                            "PRE_TRAINED_TEXT_CLASSIFICATION",
                            "TEXT_CLASSIFICATION",
                            "PRE_TRAINED_SUMMARIZATION",
                            "PRE_TRAINED_PII",
                        ],
                    ),
                    version=dict(type="str"),
                ),
            ),
            training_dataset=dict(
                type="dict",
                options=dict(
                    dataset_id=dict(type="str"),
                    dataset_type=dict(
                        type="str",
                        required=True,
                        choices=["DATA_SCIENCE_LABELING", "OBJECT_STORAGE"],
                    ),
                    location_details=dict(
                        type="dict",
                        options=dict(
                            location_type=dict(
                                type="str", required=True, choices=["OBJECT_LIST"]
                            ),
                            namespace_name=dict(type="str", required=True),
                            bucket_name=dict(type="str", required=True),
                            object_names=dict(
                                type="list", elements="str", required=True
                            ),
                        ),
                    ),
                ),
            ),
            test_strategy=dict(
                type="dict",
                options=dict(
                    strategy_type=dict(
                        type="str",
                        required=True,
                        choices=["TEST_AND_VALIDATION_DATASET"],
                    ),
                    testing_dataset=dict(
                        type="dict",
                        required=True,
                        options=dict(
                            dataset_id=dict(type="str"),
                            dataset_type=dict(
                                type="str",
                                required=True,
                                choices=["DATA_SCIENCE_LABELING", "OBJECT_STORAGE"],
                            ),
                            location_details=dict(
                                type="dict",
                                options=dict(
                                    location_type=dict(
                                        type="str",
                                        required=True,
                                        choices=["OBJECT_LIST"],
                                    ),
                                    namespace_name=dict(type="str", required=True),
                                    bucket_name=dict(type="str", required=True),
                                    object_names=dict(
                                        type="list", elements="str", required=True
                                    ),
                                ),
                            ),
                        ),
                    ),
                    validation_dataset=dict(
                        type="dict",
                        options=dict(
                            dataset_id=dict(type="str"),
                            dataset_type=dict(
                                type="str",
                                required=True,
                                choices=["DATA_SCIENCE_LABELING", "OBJECT_STORAGE"],
                            ),
                            location_details=dict(
                                type="dict",
                                options=dict(
                                    location_type=dict(
                                        type="str",
                                        required=True,
                                        choices=["OBJECT_LIST"],
                                    ),
                                    namespace_name=dict(type="str", required=True),
                                    bucket_name=dict(type="str", required=True),
                                    object_names=dict(
                                        type="list", elements="str", required=True
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            model_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="model",
        service_client_class=AIServiceLanguageClient,
        namespace="ai_language",
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
