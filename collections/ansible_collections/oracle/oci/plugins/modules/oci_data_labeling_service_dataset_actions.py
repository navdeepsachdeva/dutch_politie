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
module: oci_data_labeling_service_dataset_actions
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_data_labeling_service_dataset_actions_module.html)
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
    from oci.data_labeling_service import DataLabelingManagementClient
    from oci.data_labeling_service.models import AddDatasetLabelsDetails
    from oci.data_labeling_service.models import ChangeDatasetCompartmentDetails
    from oci.data_labeling_service.models import GenerateDatasetRecordsDetails
    from oci.data_labeling_service.models import ImportPreAnnotatedDataDetails
    from oci.data_labeling_service.models import RemoveDatasetLabelsDetails
    from oci.data_labeling_service.models import RenameDatasetLabelsDetails
    from oci.data_labeling_service.models import SnapshotDatasetDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DatasetActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        add_dataset_labels
        change_compartment
        generate_dataset_records
        import_pre_annotated_data
        remove_dataset_labels
        rename_dataset_labels
        snapshot
    """

    @staticmethod
    def get_module_resource_id_param():
        return "dataset_id"

    def get_module_resource_id(self):
        return self.module.params.get("dataset_id")

    def get_get_fn(self):
        return self.client.get_dataset

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_dataset, dataset_id=self.module.params.get("dataset_id"),
        )

    def add_dataset_labels(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AddDatasetLabelsDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.add_dataset_labels,
            call_fn_args=(),
            call_fn_kwargs=dict(
                dataset_id=self.module.params.get("dataset_id"),
                add_dataset_labels_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeDatasetCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_dataset_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                dataset_id=self.module.params.get("dataset_id"),
                change_dataset_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def generate_dataset_records(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, GenerateDatasetRecordsDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.generate_dataset_records,
            call_fn_args=(),
            call_fn_kwargs=dict(
                dataset_id=self.module.params.get("dataset_id"),
                generate_dataset_records_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def import_pre_annotated_data(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ImportPreAnnotatedDataDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.import_pre_annotated_data,
            call_fn_args=(),
            call_fn_kwargs=dict(
                dataset_id=self.module.params.get("dataset_id"),
                import_pre_annotated_data_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def remove_dataset_labels(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RemoveDatasetLabelsDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_dataset_labels,
            call_fn_args=(),
            call_fn_kwargs=dict(
                dataset_id=self.module.params.get("dataset_id"),
                remove_dataset_labels_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def rename_dataset_labels(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RenameDatasetLabelsDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.rename_dataset_labels,
            call_fn_args=(),
            call_fn_kwargs=dict(
                dataset_id=self.module.params.get("dataset_id"),
                rename_dataset_labels_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def snapshot(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, SnapshotDatasetDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.snapshot_dataset,
            call_fn_args=(),
            call_fn_kwargs=dict(
                dataset_id=self.module.params.get("dataset_id"),
                snapshot_dataset_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DatasetActionsHelperCustom = get_custom_class("DatasetActionsHelperCustom")


class ResourceHelper(DatasetActionsHelperCustom, DatasetActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            limit=dict(type="float"),
            import_format=dict(
                type="dict",
                options=dict(
                    name=dict(
                        type="str",
                        required=True,
                        choices=[
                            "JSONL_CONSOLIDATED",
                            "JSONL_COMPACT_PLUS_CONTENT",
                            "CONLL",
                            "SPACY",
                            "COCO",
                            "YOLO",
                            "PASCAL_VOC",
                        ],
                    ),
                    version=dict(type="str", choices=["V2003", "V5"]),
                ),
            ),
            import_metadata_path=dict(
                type="dict",
                options=dict(
                    source_type=dict(
                        type="str", required=True, choices=["OBJECT_STORAGE"]
                    ),
                    namespace=dict(type="str", required=True),
                    bucket=dict(type="str", required=True),
                    path=dict(type="str", required=True),
                ),
            ),
            label_set=dict(
                type="dict",
                options=dict(
                    items=dict(
                        type="list",
                        elements="dict",
                        options=dict(name=dict(type="str")),
                    )
                ),
            ),
            source_label_set=dict(
                type="dict",
                options=dict(
                    items=dict(
                        type="list",
                        elements="dict",
                        options=dict(name=dict(type="str")),
                    )
                ),
            ),
            target_label_set=dict(
                type="dict",
                options=dict(
                    items=dict(
                        type="list",
                        elements="dict",
                        options=dict(name=dict(type="str")),
                    )
                ),
            ),
            dataset_id=dict(aliases=["id"], type="str", required=True),
            are_annotations_included=dict(type="bool"),
            are_unannotated_records_included=dict(type="bool"),
            export_details=dict(
                type="dict",
                options=dict(
                    export_type=dict(
                        type="str", required=True, choices=["OBJECT_STORAGE"]
                    ),
                    namespace=dict(type="str", required=True),
                    bucket=dict(type="str", required=True),
                    prefix=dict(type="str"),
                ),
            ),
            export_format=dict(
                type="dict",
                options=dict(
                    name=dict(
                        type="str",
                        choices=[
                            "JSONL",
                            "JSONL_CONSOLIDATED",
                            "CONLL",
                            "SPACY",
                            "COCO",
                            "YOLO",
                            "PASCAL_VOC",
                            "JSONL_COMPACT_PLUS_CONTENT",
                        ],
                    ),
                    version=dict(type="str", choices=["V2003", "V5"]),
                ),
            ),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "add_dataset_labels",
                    "change_compartment",
                    "generate_dataset_records",
                    "import_pre_annotated_data",
                    "remove_dataset_labels",
                    "rename_dataset_labels",
                    "snapshot",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="dataset",
        service_client_class=DataLabelingManagementClient,
        namespace="data_labeling_service",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
