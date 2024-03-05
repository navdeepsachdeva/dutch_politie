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
module: oci_ai_speech_transcription_job
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_ai_speech_transcription_job_module.html)
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
    from oci.ai_speech import AIServiceSpeechClient
    from oci.ai_speech.models import CreateTranscriptionJobDetails
    from oci.ai_speech.models import UpdateTranscriptionJobDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TranscriptionJobHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get and list"""

    def get_possible_entity_types(self):
        return super(TranscriptionJobHelperGen, self).get_possible_entity_types() + [
            "aispeechtranscriptionjob",
            "aispeechtranscriptionjobs",
            "aiSpeechaispeechtranscriptionjob",
            "aiSpeechaispeechtranscriptionjobs",
            "aispeechtranscriptionjobresource",
            "aispeechtranscriptionjobsresource",
            "transcriptionjob",
            "transcriptionjobs",
            "aiSpeechtranscriptionjob",
            "aiSpeechtranscriptionjobs",
            "transcriptionjobresource",
            "transcriptionjobsresource",
            "aispeech",
        ]

    def get_module_resource_id_param(self):
        return "transcription_job_id"

    def get_module_resource_id(self):
        return self.module.params.get("transcription_job_id")

    def get_get_fn(self):
        return self.client.get_transcription_job

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_transcription_job, transcription_job_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_transcription_job,
            transcription_job_id=self.module.params.get("transcription_job_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["compartment_id", "display_name"]

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
            self.client.list_transcription_jobs, **kwargs
        )

    def get_create_model_class(self):
        return CreateTranscriptionJobDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_transcription_job,
            call_fn_args=(),
            call_fn_kwargs=dict(create_transcription_job_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateTranscriptionJobDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_transcription_job,
            call_fn_args=(),
            call_fn_kwargs=dict(
                transcription_job_id=self.module.params.get("transcription_job_id"),
                update_transcription_job_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )


TranscriptionJobHelperCustom = get_custom_class("TranscriptionJobHelperCustom")


class ResourceHelper(TranscriptionJobHelperCustom, TranscriptionJobHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            additional_transcription_formats=dict(
                type="list", elements="str", choices=["SRT"]
            ),
            model_details=dict(
                type="dict",
                options=dict(
                    domain=dict(type="str", choices=["GENERIC"]),
                    language_code=dict(
                        type="str",
                        choices=[
                            "en-US",
                            "es-ES",
                            "pt-BR",
                            "en-GB",
                            "en-AU",
                            "en-IN",
                            "hi-IN",
                            "fr-FR",
                            "de-DE",
                            "it-IT",
                        ],
                    ),
                ),
            ),
            normalization=dict(
                type="dict",
                options=dict(
                    is_punctuation_enabled=dict(type="bool"),
                    filters=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            type=dict(type="str", required=True, choices=["PROFANITY"]),
                            mode=dict(
                                type="str",
                                required=True,
                                choices=["MASK", "REMOVE", "TAG"],
                            ),
                        ),
                    ),
                ),
            ),
            input_location=dict(
                type="dict",
                options=dict(
                    object_location=dict(
                        type="dict",
                        options=dict(
                            namespace_name=dict(type="str", required=True),
                            bucket_name=dict(type="str", required=True),
                            object_names=dict(
                                type="list", elements="str", required=True
                            ),
                        ),
                    ),
                    location_type=dict(
                        type="str",
                        required=True,
                        choices=[
                            "OBJECT_LIST_FILE_INPUT_LOCATION",
                            "OBJECT_LIST_INLINE_INPUT_LOCATION",
                        ],
                    ),
                    object_locations=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            namespace_name=dict(type="str", required=True),
                            bucket_name=dict(type="str", required=True),
                            object_names=dict(
                                type="list", elements="str", required=True
                            ),
                        ),
                    ),
                ),
            ),
            output_location=dict(
                type="dict",
                options=dict(
                    namespace_name=dict(type="str", required=True),
                    bucket_name=dict(type="str", required=True),
                    prefix=dict(type="str", required=True),
                ),
            ),
            transcription_job_id=dict(aliases=["id"], type="str"),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="transcription_job",
        service_client_class=AIServiceSpeechClient,
        namespace="ai_speech",
    )

    result = dict(changed=False)

    if resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
