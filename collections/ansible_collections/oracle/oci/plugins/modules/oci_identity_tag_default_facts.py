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
module: oci_identity_tag_default_facts
short_description: Fetches details about one or multiple TagDefault resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple TagDefault resources in Oracle Cloud Infrastructure
    - Lists the tag defaults for tag definitions in the specified compartment.
    - If I(tag_default_id) is specified, the details of a single TagDefault will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    tag_default_id:
        description:
            - The OCID of the tag default.
            - Required to get a specific tag_default.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the compartment (remember that the tenancy is simply the root compartment).
        type: str
    tag_definition_id:
        description:
            - The OCID of the tag definition.
        type: str
    lifecycle_state:
        description:
            - A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.
        type: str
        choices:
            - "ACTIVE"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific tag_default
  oci_identity_tag_default_facts:
    # required
    tag_default_id: "ocid1.tagdefault.oc1..xxxxxxEXAMPLExxxxxx"

- name: List tag_defaults
  oci_identity_tag_default_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    tag_definition_id: "ocid1.tagdefinition.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: ACTIVE

"""

RETURN = """
tag_defaults:
    description:
        - List of TagDefault resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the tag default.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment. The tag default applies to all new resources that get created in the
                  compartment. Resources that existed before the tag default was created are not tagged.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        tag_namespace_id:
            description:
                - The OCID of the tag namespace that contains the tag definition.
            returned: on success
            type: str
            sample: "ocid1.tagnamespace.oc1..xxxxxxEXAMPLExxxxxx"
        tag_definition_id:
            description:
                - The OCID of the tag definition. The tag default will always assign a default value for this tag definition.
            returned: on success
            type: str
            sample: "ocid1.tagdefinition.oc1..xxxxxxEXAMPLExxxxxx"
        tag_definition_name:
            description:
                - The name used in the tag definition. This field is informational in the context of the tag default.
            returned: on success
            type: str
            sample: tag_definition_name_example
        value:
            description:
                - The default value for the tag definition. This will be applied to all resources created in the compartment.
            returned: on success
            type: str
            sample: value_example
        time_created:
            description:
                - Date and time the `TagDefault` object was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The tag default's current state. After creating a `TagDefault`, make sure its `lifecycleState` is ACTIVE before using it.
            returned: on success
            type: str
            sample: ACTIVE
        locks:
            description:
                - Locks associated with this resource.
                - Returned for list operation
            returned: on success
            type: complex
            contains:
                type:
                    description:
                        - Type of the lock.
                    returned: on success
                    type: str
                    sample: FULL
                related_resource_id:
                    description:
                        - The ID of the resource that is locking this resource. Indicates that deleting this resource will remove the lock.
                    returned: on success
                    type: str
                    sample: "ocid1.relatedresource.oc1..xxxxxxEXAMPLExxxxxx"
                message:
                    description:
                        - A message added by the creator of the lock. This is typically used to give an
                          indication of why the resource is locked.
                    returned: on success
                    type: str
                    sample: message_example
                time_created:
                    description:
                        - When the lock was created.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                is_active:
                    description:
                        - Indicates if the lock is active or not. For example, if there are mutliple FULL locks, the first-created FULL lock will be effective.
                    returned: on success
                    type: bool
                    sample: true
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "tag_namespace_id": "ocid1.tagnamespace.oc1..xxxxxxEXAMPLExxxxxx",
        "tag_definition_id": "ocid1.tagdefinition.oc1..xxxxxxEXAMPLExxxxxx",
        "tag_definition_name": "tag_definition_name_example",
        "value": "value_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
        "locks": [{
            "type": "FULL",
            "related_resource_id": "ocid1.relatedresource.oc1..xxxxxxEXAMPLExxxxxx",
            "message": "message_example",
            "time_created": "2013-10-20T19:20:30+01:00",
            "is_active": true
        }]
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.identity import IdentityClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TagDefaultFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "tag_default_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_tag_default,
            tag_default_id=self.module.params.get("tag_default_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "tag_definition_id",
            "lifecycle_state",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_tag_defaults, **optional_kwargs
        )


TagDefaultFactsHelperCustom = get_custom_class("TagDefaultFactsHelperCustom")


class ResourceFactsHelper(TagDefaultFactsHelperCustom, TagDefaultFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            tag_default_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            tag_definition_id=dict(type="str"),
            lifecycle_state=dict(type="str", choices=["ACTIVE"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="tag_default",
        service_client_class=IdentityClient,
        namespace="identity",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(tag_defaults=result)


if __name__ == "__main__":
    main()
