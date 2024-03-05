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
module: oci_data_labeling_service_dataplane_annotation
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_data_labeling_service_dataplane_annotation_module.html)
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
    from oci.data_labeling_service_dataplane import DataLabelingClient
    from oci.data_labeling_service_dataplane.models import CreateAnnotationDetails
    from oci.data_labeling_service_dataplane.models import UpdateAnnotationDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AnnotationHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(AnnotationHelperGen, self).get_possible_entity_types() + [
            "datalabelingannotation",
            "datalabelingannotations",
            "dataLabelingServiceDataplanedatalabelingannotation",
            "dataLabelingServiceDataplanedatalabelingannotations",
            "datalabelingannotationresource",
            "datalabelingannotationsresource",
            "annotation",
            "annotations",
            "dataLabelingServiceDataplaneannotation",
            "dataLabelingServiceDataplaneannotations",
            "annotationresource",
            "annotationsresource",
            "datalabelingservicedataplane",
        ]

    def get_module_resource_id_param(self):
        return "annotation_id"

    def get_module_resource_id(self):
        return self.module.params.get("annotation_id")

    def get_get_fn(self):
        return self.client.get_annotation

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_annotation, annotation_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_annotation,
            annotation_id=self.module.params.get("annotation_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
            "dataset_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["record_id"]

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
            self.client.list_annotations, **kwargs
        )

    def get_create_model_class(self):
        return CreateAnnotationDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_annotation,
            call_fn_args=(),
            call_fn_kwargs=dict(create_annotation_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateAnnotationDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_annotation,
            call_fn_args=(),
            call_fn_kwargs=dict(
                annotation_id=self.module.params.get("annotation_id"),
                update_annotation_details=update_details,
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
            call_fn=self.client.delete_annotation,
            call_fn_args=(),
            call_fn_kwargs=dict(annotation_id=self.module.params.get("annotation_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


AnnotationHelperCustom = get_custom_class("AnnotationHelperCustom")


class ResourceHelper(AnnotationHelperCustom, AnnotationHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            record_id=dict(type="str"),
            compartment_id=dict(type="str"),
            entities=dict(
                type="list",
                elements="dict",
                options=dict(
                    document_entity_metadata=dict(
                        type="dict",
                        options=dict(page_number=dict(type="float", required=True)),
                    ),
                    text=dict(type="str"),
                    bounding_polygon=dict(
                        type="dict",
                        options=dict(
                            normalized_vertices=dict(
                                type="list",
                                elements="dict",
                                required=True,
                                options=dict(
                                    x=dict(type="float", required=True),
                                    y=dict(type="float", required=True),
                                ),
                            )
                        ),
                    ),
                    rotation=dict(type="float"),
                    confidence=dict(type="float"),
                    page_number=dict(type="float"),
                    entity_type=dict(
                        type="str",
                        required=True,
                        choices=[
                            "IMAGEOBJECTSELECTION",
                            "GENERIC",
                            "KEYVALUESELECTION",
                            "TEXTSELECTION",
                        ],
                    ),
                    labels=dict(
                        type="list",
                        elements="dict",
                        options=dict(label=dict(type="str", required=True)),
                    ),
                    text_span=dict(
                        type="dict",
                        options=dict(
                            offset=dict(type="float"), length=dict(type="float")
                        ),
                    ),
                    extended_metadata=dict(type="dict"),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            annotation_id=dict(aliases=["id"], type="str"),
            dataset_id=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="annotation",
        service_client_class=DataLabelingClient,
        namespace="data_labeling_service_dataplane",
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
