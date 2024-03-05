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
module: oci_devops_repository_commit_facts
description: >-
    Due to size constraints we have not included the documentation in the module. Please check L(here,
    https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/oci_devops_repository_commit_facts_module.html)
    for the module documentation.
author: Oracle (@oracle)
"""


from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.devops import DevopsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DevopsRepositoryCommitFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "repository_id",
            "commit_id",
        ]

    def get_required_params_for_list(self):
        return [
            "repository_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_commit,
            repository_id=self.module.params.get("repository_id"),
            commit_id=self.module.params.get("commit_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "ref_name",
            "exclude_ref_name",
            "file_path",
            "timestamp_greater_than_or_equal_to",
            "timestamp_less_than_or_equal_to",
            "commit_message",
            "author_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_commits,
            repository_id=self.module.params.get("repository_id"),
            **optional_kwargs
        )


DevopsRepositoryCommitFactsHelperCustom = get_custom_class(
    "DevopsRepositoryCommitFactsHelperCustom"
)


class ResourceFactsHelper(
    DevopsRepositoryCommitFactsHelperCustom, DevopsRepositoryCommitFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            commit_id=dict(aliases=["id"], type="str"),
            repository_id=dict(type="str", required=True),
            ref_name=dict(type="str"),
            exclude_ref_name=dict(type="str"),
            file_path=dict(type="str"),
            timestamp_greater_than_or_equal_to=dict(type="str"),
            timestamp_less_than_or_equal_to=dict(type="str"),
            commit_message=dict(type="str"),
            author_name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="repository_commit",
        service_client_class=DevopsClient,
        namespace="devops",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(repository_commits=result)


if __name__ == "__main__":
    main()
