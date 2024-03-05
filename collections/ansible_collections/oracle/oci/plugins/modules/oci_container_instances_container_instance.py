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
module: oci_container_instances_container_instance
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_container_instances_container_instance_module.html)
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
    from oci.container_instances import ContainerInstanceClient
    from oci.container_instances.models import CreateContainerInstanceDetails
    from oci.container_instances.models import UpdateContainerInstanceDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ContainerInstanceHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(ContainerInstanceHelperGen, self).get_possible_entity_types() + [
            "containerinstance",
            "containerinstances",
            "containerInstancescontainerinstance",
            "containerInstancescontainerinstances",
            "containerinstanceresource",
            "containerinstancesresource",
        ]

    def get_module_resource_id_param(self):
        return "container_instance_id"

    def get_module_resource_id(self):
        return self.module.params.get("container_instance_id")

    def get_get_fn(self):
        return self.client.get_container_instance

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_container_instance, container_instance_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_container_instance,
            container_instance_id=self.module.params.get("container_instance_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name", "availability_domain"]

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
            self.client.list_container_instances, **kwargs
        )

    def get_create_model_class(self):
        return CreateContainerInstanceDetails

    def get_exclude_attributes(self):
        return [
            "containers.resource_config",
            "vnics.freeform_tags",
            "containers.defined_tags",
            "vnics.subnet_id",
            "containers.working_directory",
            "containers.freeform_tags",
            "vnics.defined_tags",
            "vnics.private_ip",
            "vnics.nsg_ids",
            "containers.arguments",
            "vnics.is_public_ip_assigned",
            "vnics.display_name",
            "containers.health_checks",
            "containers.security_context",
            "containers.environment_variables",
            "containers.is_resource_principal_disabled",
            "vnics.skip_source_dest_check",
            "image_pull_secrets.username",
            "containers.image_url",
            "vnics.hostname_label",
            "image_pull_secrets.password",
            "containers.volume_mounts",
            "containers.command",
        ]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_container_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(create_container_instance_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateContainerInstanceDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_container_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                container_instance_id=self.module.params.get("container_instance_id"),
                update_container_instance_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_container_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                container_instance_id=self.module.params.get("container_instance_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ContainerInstanceHelperCustom = get_custom_class("ContainerInstanceHelperCustom")


class ResourceHelper(ContainerInstanceHelperCustom, ContainerInstanceHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            availability_domain=dict(type="str"),
            fault_domain=dict(type="str"),
            shape=dict(type="str"),
            shape_config=dict(
                type="dict",
                options=dict(
                    ocpus=dict(type="float", required=True),
                    memory_in_gbs=dict(type="float"),
                ),
            ),
            volumes=dict(
                type="list",
                elements="dict",
                options=dict(
                    configs=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            file_name=dict(type="str", required=True),
                            data=dict(type="str", required=True),
                            path=dict(type="str"),
                        ),
                    ),
                    name=dict(type="str", required=True),
                    volume_type=dict(
                        type="str",
                        required=True,
                        default="null",
                        choices=["CONFIGFILE", "EMPTYDIR"],
                    ),
                    backing_store=dict(type="str"),
                ),
            ),
            containers=dict(
                type="list",
                elements="dict",
                options=dict(
                    display_name=dict(aliases=["name"], type="str"),
                    image_url=dict(type="str", required=True),
                    command=dict(type="list", elements="str"),
                    arguments=dict(type="list", elements="str"),
                    working_directory=dict(type="str"),
                    environment_variables=dict(type="dict"),
                    volume_mounts=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            mount_path=dict(type="str", required=True),
                            volume_name=dict(type="str", required=True),
                            sub_path=dict(type="str"),
                            is_read_only=dict(type="bool"),
                            partition=dict(type="int"),
                        ),
                    ),
                    is_resource_principal_disabled=dict(type="bool"),
                    resource_config=dict(
                        type="dict",
                        options=dict(
                            vcpus_limit=dict(type="float"),
                            memory_limit_in_gbs=dict(type="float"),
                        ),
                    ),
                    health_checks=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            path=dict(type="str"),
                            port=dict(type="int"),
                            headers=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    name=dict(type="str", required=True),
                                    value=dict(type="str", required=True),
                                ),
                            ),
                            name=dict(type="str"),
                            health_check_type=dict(
                                type="str",
                                required=True,
                                choices=["TCP", "HTTP", "COMMAND"],
                            ),
                            initial_delay_in_seconds=dict(type="int"),
                            interval_in_seconds=dict(type="int"),
                            failure_threshold=dict(type="int"),
                            success_threshold=dict(type="int"),
                            timeout_in_seconds=dict(type="int"),
                            failure_action=dict(type="str", choices=["KILL", "NONE"]),
                            command=dict(type="list", elements="str"),
                        ),
                    ),
                    security_context=dict(
                        type="dict",
                        options=dict(
                            security_context_type=dict(
                                type="str", default="LINUX", choices=["LINUX"]
                            ),
                            run_as_user=dict(type="int"),
                            run_as_group=dict(type="int"),
                            is_non_root_user_check_enabled=dict(type="bool"),
                            is_root_file_system_readonly=dict(type="bool"),
                        ),
                    ),
                    freeform_tags=dict(type="dict"),
                    defined_tags=dict(type="dict"),
                ),
            ),
            vnics=dict(
                type="list",
                elements="dict",
                options=dict(
                    display_name=dict(aliases=["name"], type="str"),
                    hostname_label=dict(type="str"),
                    is_public_ip_assigned=dict(type="bool"),
                    skip_source_dest_check=dict(type="bool"),
                    nsg_ids=dict(type="list", elements="str"),
                    private_ip=dict(type="str"),
                    subnet_id=dict(type="str", required=True),
                    freeform_tags=dict(type="dict"),
                    defined_tags=dict(type="dict"),
                ),
            ),
            dns_config=dict(
                type="dict",
                options=dict(
                    nameservers=dict(type="list", elements="str"),
                    searches=dict(type="list", elements="str"),
                    options=dict(type="list", elements="str"),
                ),
            ),
            graceful_shutdown_timeout_in_seconds=dict(type="int"),
            image_pull_secrets=dict(
                type="list",
                elements="dict",
                no_log=False,
                options=dict(
                    secret_id=dict(type="str"),
                    secret_type=dict(
                        type="str", required=True, choices=["VAULT", "BASIC"]
                    ),
                    registry_endpoint=dict(type="str", required=True),
                    username=dict(type="str"),
                    password=dict(type="str", no_log=True),
                ),
            ),
            container_restart_policy=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            container_instance_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="container_instance",
        service_client_class=ContainerInstanceClient,
        namespace="container_instances",
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
