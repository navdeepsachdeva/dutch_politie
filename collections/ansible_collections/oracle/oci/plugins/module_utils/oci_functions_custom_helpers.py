# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import oci_config_utils

try:
    from oci.functions import FunctionsInvokeClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class FunctionActionsHelperCustom:

    # invoke action uses a different client (FunctionsInvokeClient) than the one that is generated for the function
    # resource (FunctionsManagementClient) based on other operations. Currently codegen only supports one client class
    # for a resource. The other option would have been renaming the resource for this operation which would have
    # generated with the invoke client. But we would still need the FunctionsManagementClient to get the functions
    # endpoint.
    # TODO: Add support for multiple client classes in codegen
    def invoke(self):
        if not self.module.params.get("dest"):
            self.module.fail_json(msg="dest parameter required for invoke action")
        function = self.get_resource().data
        self.module.params["service_endpoint"] = function.invoke_endpoint
        functions_invoke_client = oci_config_utils.create_service_client(
            self.module, FunctionsInvokeClient
        )
        try:
            # Temporarily change self.client in the context of this method. Preferring this over overriding the
            # self.client to use FunctionsInvokeClient since there might be other actions (for ex: change_compartment)
            # in the future which need the client generated by the generated module.
            functions_management_client = self.client
            self.client = functions_invoke_client
            super(FunctionActionsHelperCustom, self).invoke()
            return function
        finally:
            self.client = functions_management_client
