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
module: oci_network_ip_sec_connection
short_description: Manage an IpSecConnection resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an IpSecConnection resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new IPSec connection between the specified DRG and CPE. For more information, see
      L(Site-to-Site VPN Overview,https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/overviewIPsec.htm).
    - "If you configure at least one tunnel to use static routing, then in the request you must provide
      at least one valid static route (you're allowed a maximum of 10). For example: 10.0.0.0/16.
      If you configure both tunnels to use BGP dynamic routing, you can provide an empty list for
      the static routes. For more information, see the important note in
      L(IPSecConnection,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/IPSecConnection/)."
    - For the purposes of access control, you must provide the L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the
      compartment where you want the
      IPSec connection to reside. Notice that the IPSec connection doesn't have to be in the same compartment
      as the DRG, CPE, or other Networking Service components. If you're not sure which compartment to
      use, put the IPSec connection in the same compartment as the DRG. For more information about
      compartments and access control, see
      L(Overview of the IAM Service,https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/overview.htm).
    - "You may optionally specify a *display name* for the IPSec connection, otherwise a default is provided.
      It does not have to be unique, and you can change it. Avoid entering confidential information."
    - "After creating the IPSec connection, you need to configure your on-premises router
      with tunnel-specific information. For tunnel status and the required configuration information, see:"
    - " * L(IPSecConnectionTunnel,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/IPSecConnectionTunnel/)
        * L(IPSecConnectionTunnelSharedSecret,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/IPSecConnectionTunnelSharedSecret/)"
    - For each tunnel, you need the IP address of Oracle's VPN headend and the shared secret
      (that is, the pre-shared key). For more information, see
      L(CPE Configuration,https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/configuringCPE.htm).
    - "This resource has the following action operations in the M(oracle.oci.oci_network_ip_sec_connection_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to contain the IPSec connection.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    cpe_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the L(Cpe,https://docs.cloud.oracle.com/en-
              us/iaas/api/#/en/iaas/latest/Cpe/) object.
            - Required for create using I(state=present).
        type: str
    drg_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DRG.
            - Required for create using I(state=present).
        type: str
    tunnel_configuration:
        description:
            - Information for creating the individual tunnels in the IPSec connection. You can provide a
              maximum of 2 `tunnelConfiguration` objects in the array (one for each of the
              two tunnels).
        type: list
        elements: dict
        suboptions:
            display_name:
                description:
                    - A user-friendly name. Does not have to be unique, and it's changeable.
                      Avoid entering confidential information.
                type: str
                aliases: ["name"]
            routing:
                description:
                    - The type of routing to use for this tunnel (BGP dynamic routing, static routing, or policy-based routing).
                type: str
                choices:
                    - "BGP"
                    - "STATIC"
                    - "POLICY"
            ike_version:
                description:
                    - Internet Key Exchange protocol version.
                type: str
                choices:
                    - "V1"
                    - "V2"
            shared_secret:
                description:
                    - The shared secret (pre-shared key) to use for the IPSec tunnel. Only numbers, letters, and
                      spaces are allowed. If you don't provide a value,
                      Oracle generates a value for you. You can specify your own shared secret later if
                      you like with L(UpdateIPSecConnectionTunnelSharedSecret,https://docs.cloud.oracle.com/en-
                      us/iaas/api/#/en/iaas/latest/IPSecConnectionTunnelSharedSecret/UpdateIPSecConnectionTunnelSharedSecret).
                type: str
            bgp_session_config:
                description:
                    - ""
                type: dict
                suboptions:
                    oracle_interface_ip:
                        description:
                            - The IP address for the Oracle end of the inside tunnel interface.
                            - If the tunnel's `routing` attribute is set to `BGP`
                              (see L(IPSecConnectionTunnel,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/IPSecConnectionTunnel/)), this IP
                              address
                              is required and used for the tunnel's BGP session.
                            - If `routing` is instead set to `STATIC`, this IP address is optional. You can set this IP
                              address to troubleshoot or monitor the tunnel.
                            - The value must be a /30 or /31.
                            - "Example: `10.0.0.4/31`"
                        type: str
                    customer_interface_ip:
                        description:
                            - The IP address for the CPE end of the inside tunnel interface.
                            - If the tunnel's `routing` attribute is set to `BGP`
                              (see L(IPSecConnectionTunnel,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/IPSecConnectionTunnel/)), this IP
                              address
                              is required and used for the tunnel's BGP session.
                            - If `routing` is instead set to `STATIC`, this IP address is optional. You can set this IP
                              address to troubleshoot or monitor the tunnel.
                            - The value must be a /30 or /31.
                            - "Example: `10.0.0.5/31`"
                        type: str
                    oracle_interface_ipv6:
                        description:
                            - The IPv6 address for the Oracle end of the inside tunnel interface. This IP address is optional.
                            - If the tunnel's `routing` attribute is set to `BGP`
                              (see L(IPSecConnectionTunnel,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/IPSecConnectionTunnel/)), this IP
                              address
                              is used for the tunnel's BGP session.
                            - If `routing` is instead set to `STATIC`, you can set this IP
                              address to troubleshoot or monitor the tunnel.
                            - Only subnet masks from /64 up to /127 are allowed.
                            - "Example: `2001:db8::1/64`"
                        type: str
                    customer_interface_ipv6:
                        description:
                            - The IPv6 address for the CPE end of the inside tunnel interface. This IP address is optional.
                            - If the tunnel's `routing` attribute is set to `BGP`
                              (see L(IPSecConnectionTunnel,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/IPSecConnectionTunnel/)), this IP
                              address
                              is used for the tunnel's BGP session.
                            - If `routing` is instead set to `STATIC`, you can set this IP
                              address to troubleshoot or monitor the tunnel.
                            - Only subnet masks from /64 up to /127 are allowed.
                            - "Example: `2001:db8::1/64`"
                        type: str
                    customer_bgp_asn:
                        description:
                            - "If the tunnel's `routing` attribute is set to `BGP`
                              (see L(IPSecConnectionTunnel,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/IPSecConnectionTunnel/)), this ASN
                              is required and used for the tunnel's BGP session. This is the ASN of the network on the
                              CPE end of the BGP session. Can be a 2-byte or 4-byte ASN. Uses \\"asplain\\" format."
                            - If the tunnel's `routing` attribute is set to `STATIC`, the `customerBgpAsn` must be null.
                            - "Example: `12345` (2-byte) or `1587232876` (4-byte)"
                        type: str
            oracle_initiation:
                description:
                    - Indicates whether the Oracle end of the IPSec connection is able to initiate starting up the IPSec tunnel.
                type: str
                choices:
                    - "INITIATOR_OR_RESPONDER"
                    - "RESPONDER_ONLY"
            nat_translation_enabled:
                description:
                    - By default (the `AUTO` setting), IKE sends packets with a source and destination port set to 500,
                      and when it detects that the port used to forward packets has changed (most likely because a NAT device
                      is between the CPE device and the Oracle VPN headend) it will try to negotiate the use of NAT-T.
                    - The `ENABLED` option sets the IKE protocol to use port 4500 instead of 500 and forces encapsulating traffic with the ESP protocol inside
                      UDP packets.
                    - The `DISABLED` option directs IKE to completely refuse to negotiate NAT-T
                      even if it senses there may be a NAT device in use.
                type: str
                choices:
                    - "ENABLED"
                    - "DISABLED"
                    - "AUTO"
            phase_one_config:
                description:
                    - ""
                type: dict
                suboptions:
                    is_custom_phase_one_config:
                        description:
                            - Indicates whether custom configuration is enabled for phase one options.
                        type: bool
                    authentication_algorithm:
                        description:
                            - The custom authentication algorithm proposed during phase one tunnel negotiation.
                        type: str
                        choices:
                            - "SHA2_384"
                            - "SHA2_256"
                            - "SHA1_96"
                    encryption_algorithm:
                        description:
                            - The custom encryption algorithm proposed during phase one tunnel negotiation.
                        type: str
                        choices:
                            - "AES_256_CBC"
                            - "AES_192_CBC"
                            - "AES_128_CBC"
                    diffie_helman_group:
                        description:
                            - The custom Diffie-Hellman group proposed during phase one tunnel negotiation.
                        type: str
                        choices:
                            - "GROUP2"
                            - "GROUP5"
                            - "GROUP14"
                            - "GROUP19"
                            - "GROUP20"
                            - "GROUP24"
                    lifetime_in_seconds:
                        description:
                            - Internet key association (IKE) session key lifetime in seconds for IPSec phase one. The default is 28800 which is equivalent to 8
                              hours.
                        type: int
            phase_two_config:
                description:
                    - ""
                type: dict
                suboptions:
                    is_custom_phase_two_config:
                        description:
                            - Indicates whether custom configuration is enabled for phase two options.
                        type: bool
                    authentication_algorithm:
                        description:
                            - The authentication algorithm proposed during phase two tunnel negotiation.
                        type: str
                        choices:
                            - "HMAC_SHA2_256_128"
                            - "HMAC_SHA1_128"
                    encryption_algorithm:
                        description:
                            - The encryption algorithm proposed during phase two tunnel negotiation.
                        type: str
                        choices:
                            - "AES_256_GCM"
                            - "AES_192_GCM"
                            - "AES_128_GCM"
                            - "AES_256_CBC"
                            - "AES_192_CBC"
                            - "AES_128_CBC"
                    lifetime_in_seconds:
                        description:
                            - Lifetime in seconds for the IPSec session key set in phase two. The default is 3600 which is equivalent to 1 hour.
                        type: int
                    is_pfs_enabled:
                        description:
                            - Indicates whether perfect forward secrecy (PFS) is enabled.
                        type: bool
                    pfs_dh_group:
                        description:
                            - The Diffie-Hellman group used for PFS, if PFS is enabled.
                        type: str
                        choices:
                            - "GROUP2"
                            - "GROUP5"
                            - "GROUP14"
                            - "GROUP19"
                            - "GROUP20"
                            - "GROUP24"
            dpd_config:
                description:
                    - ""
                type: dict
                suboptions:
                    dpd_mode:
                        description:
                            - This option defines whether DPD can be initiated from the Oracle side of the connection.
                        type: str
                        choices:
                            - "INITIATE_AND_RESPOND"
                            - "RESPOND_ONLY"
                    dpd_timeout_in_sec:
                        description:
                            - DPD timeout in seconds. This sets the longest interval between CPE device health messages before the IPSec connection indicates it
                              has lost contact with the CPE. The default is 20 seconds.
                        type: int
            encryption_domain_config:
                description:
                    - ""
                type: dict
                suboptions:
                    oracle_traffic_selector:
                        description:
                            - Lists IPv4 or IPv6-enabled subnets in your Oracle tenancy.
                        type: list
                        elements: str
                    cpe_traffic_selector:
                        description:
                            - Lists IPv4 or IPv6-enabled subnets in your on-premises network.
                        type: list
                        elements: str
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a
              namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable.
              Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    cpe_local_identifier:
        description:
            - Your identifier for your CPE device. Can be either an IP address or a hostname (specifically, the
              fully qualified domain name (FQDN)). The type of identifier you provide here must correspond
              to the value for `cpeLocalIdentifierType`.
            - If you don't provide a value, the `ipAddress` attribute for the L(Cpe,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Cpe/)
              object specified by `cpeId` is used as the `cpeLocalIdentifier`.
            - For information about why you'd provide this value, see
              L(If Your CPE Is Behind a NAT Device,https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/overviewIPsec.htm#nat).
            - "Example IP address: `10.0.3.3`"
            - "Example hostname: `cpe.example.com`"
            - This parameter is updatable.
        type: str
    cpe_local_identifier_type:
        description:
            - The type of identifier for your CPE device. The value you provide here must correspond to the value
              for `cpeLocalIdentifier`.
            - This parameter is updatable.
        type: str
        choices:
            - "IP_ADDRESS"
            - "HOSTNAME"
    static_routes:
        description:
            - Static routes to the CPE. A static route's CIDR must not be a
              multicast address or class E address.
            - Used for routing a given IPSec tunnel's traffic only if the tunnel
              is using static routing. If you configure at least one tunnel to use static routing, then
              you must provide at least one valid static route. If you configure both
              tunnels to use BGP dynamic routing, you can provide an empty list for the static routes.
              For more information, see the important note in L(IPSecConnection,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/IPSecConnection/).
            - The CIDR can be either IPv4 or IPv6. IPv6 addressing is supported for all commercial and government regions.
              See L(IPv6 Addresses,https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/ipv6.htm).
            - "Example: `10.0.1.0/24`"
            - "Example: `2001:db8::/32`"
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: list
        elements: str
    ipsc_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the IPSec connection.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the IpSecConnection.
            - Use I(state=present) to create or update an IpSecConnection.
            - Use I(state=absent) to delete an IpSecConnection.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create ip_sec_connection
  oci_network_ip_sec_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    cpe_id: "ocid1.cpe.oc1..xxxxxxEXAMPLExxxxxx"
    drg_id: "ocid1.drg.oc1..xxxxxxEXAMPLExxxxxx"
    static_routes: [ "static_routes_example" ]

    # optional
    tunnel_configuration:
    - # optional
      display_name: display_name_example
      routing: BGP
      ike_version: V1
      shared_secret: shared_secret_example
      bgp_session_config:
        # optional
        oracle_interface_ip: oracle_interface_ip_example
        customer_interface_ip: customer_interface_ip_example
        oracle_interface_ipv6: oracle_interface_ipv6_example
        customer_interface_ipv6: customer_interface_ipv6_example
        customer_bgp_asn: customer_bgp_asn_example
      oracle_initiation: INITIATOR_OR_RESPONDER
      nat_translation_enabled: ENABLED
      phase_one_config:
        # optional
        is_custom_phase_one_config: true
        authentication_algorithm: SHA2_384
        encryption_algorithm: AES_256_CBC
        diffie_helman_group: GROUP2
        lifetime_in_seconds: 56
      phase_two_config:
        # optional
        is_custom_phase_two_config: true
        authentication_algorithm: HMAC_SHA2_256_128
        encryption_algorithm: AES_256_GCM
        lifetime_in_seconds: 56
        is_pfs_enabled: true
        pfs_dh_group: GROUP2
      dpd_config:
        # optional
        dpd_mode: INITIATE_AND_RESPOND
        dpd_timeout_in_sec: 56
      encryption_domain_config:
        # optional
        oracle_traffic_selector: [ "oracle_traffic_selector_example" ]
        cpe_traffic_selector: [ "cpe_traffic_selector_example" ]
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    cpe_local_identifier: cpe_local_identifier_example
    cpe_local_identifier_type: IP_ADDRESS

- name: Update ip_sec_connection
  oci_network_ip_sec_connection:
    # required
    ipsc_id: "ocid1.ipsc.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    cpe_local_identifier: cpe_local_identifier_example
    cpe_local_identifier_type: IP_ADDRESS
    static_routes: [ "static_routes_example" ]

- name: Update ip_sec_connection using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_ip_sec_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}
    cpe_local_identifier: cpe_local_identifier_example
    cpe_local_identifier_type: IP_ADDRESS
    static_routes: [ "static_routes_example" ]

- name: Delete ip_sec_connection
  oci_network_ip_sec_connection:
    # required
    ipsc_id: "ocid1.ipsc.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete ip_sec_connection using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_ip_sec_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
ip_sec_connection:
    description:
        - Details of the IpSecConnection resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the IPSec connection.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        cpe_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the L(Cpe,https://docs.cloud.oracle.com/en-
                  us/iaas/api/#/en/iaas/latest/Cpe/) object.
            returned: on success
            type: str
            sample: "ocid1.cpe.oc1..xxxxxxEXAMPLExxxxxx"
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        drg_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DRG.
            returned: on success
            type: str
            sample: "ocid1.drg.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The IPSec connection's Oracle ID (L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm)).
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The IPSec connection's current state.
            returned: on success
            type: str
            sample: PROVISIONING
        cpe_local_identifier:
            description:
                - Your identifier for your CPE device. Can be either an IP address or a hostname (specifically,
                  the fully qualified domain name (FQDN)). The type of identifier here must correspond
                  to the value for `cpeLocalIdentifierType`.
                - If you don't provide a value when creating the IPSec connection, the `ipAddress` attribute
                  for the L(Cpe,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Cpe/) object specified by `cpeId` is used as the
                  `cpeLocalIdentifier`.
                - For information about why you'd provide this value, see
                  L(If Your CPE Is Behind a NAT Device,https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/overviewIPsec.htm#nat).
                - "Example IP address: `10.0.3.3`"
                - "Example hostname: `cpe.example.com`"
            returned: on success
            type: str
            sample: cpe_local_identifier_example
        cpe_local_identifier_type:
            description:
                - The type of identifier for your CPE device. The value here must correspond to the value
                  for `cpeLocalIdentifier`.
            returned: on success
            type: str
            sample: IP_ADDRESS
        static_routes:
            description:
                - Static routes to the CPE. The CIDR must not be a
                  multicast address or class E address.
                - Used for routing a given IPSec tunnel's traffic only if the tunnel
                  is using static routing. If you configure at least one tunnel to use static routing, then
                  you must provide at least one valid static route. If you configure both
                  tunnels to use BGP dynamic routing, you can provide an empty list for the static routes.
                - The CIDR can be either IPv4 or IPv6. IPv6 addressing is supported for all commercial and government regions.
                  See L(IPv6 Addresses,https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/ipv6.htm).
                - "Example: `10.0.1.0/24`"
                - "Example: `2001:db8::/32`"
            returned: on success
            type: list
            sample: []
        time_created:
            description:
                - The date and time the IPSec connection was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "cpe_id": "ocid1.cpe.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "drg_id": "ocid1.drg.oc1..xxxxxxEXAMPLExxxxxx",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "PROVISIONING",
        "cpe_local_identifier": "cpe_local_identifier_example",
        "cpe_local_identifier_type": "IP_ADDRESS",
        "static_routes": [],
        "time_created": "2013-10-20T19:20:30+01:00"
    }
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
    from oci.core import VirtualNetworkClient
    from oci.core.models import CreateIPSecConnectionDetails
    from oci.core.models import UpdateIPSecConnectionDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class IpSecConnectionHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(IpSecConnectionHelperGen, self).get_possible_entity_types() + [
            "ipsecconnection",
            "ipsecconnections",
            "coreipsecconnection",
            "coreipsecconnections",
            "ipsecconnectionresource",
            "ipsecconnectionsresource",
            "core",
        ]

    def get_module_resource_id_param(self):
        return "ipsc_id"

    def get_module_resource_id(self):
        return self.module.params.get("ipsc_id")

    def get_get_fn(self):
        return self.client.get_ip_sec_connection

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_ip_sec_connection,
            ipsc_id=self.module.params.get("ipsc_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["drg_id", "cpe_id"]

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
            self.client.list_ip_sec_connections, **kwargs
        )

    def get_create_model_class(self):
        return CreateIPSecConnectionDetails

    def get_exclude_attributes(self):
        return ["tunnel_configuration"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_ip_sec_connection,
            call_fn_args=(),
            call_fn_kwargs=dict(create_ip_sec_connection_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateIPSecConnectionDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_ip_sec_connection,
            call_fn_args=(),
            call_fn_kwargs=dict(
                ipsc_id=self.module.params.get("ipsc_id"),
                update_ip_sec_connection_details=update_details,
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
            call_fn=self.client.delete_ip_sec_connection,
            call_fn_args=(),
            call_fn_kwargs=dict(ipsc_id=self.module.params.get("ipsc_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


IpSecConnectionHelperCustom = get_custom_class("IpSecConnectionHelperCustom")


class ResourceHelper(IpSecConnectionHelperCustom, IpSecConnectionHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            cpe_id=dict(type="str"),
            drg_id=dict(type="str"),
            tunnel_configuration=dict(
                type="list",
                elements="dict",
                options=dict(
                    display_name=dict(aliases=["name"], type="str"),
                    routing=dict(type="str", choices=["BGP", "STATIC", "POLICY"]),
                    ike_version=dict(type="str", choices=["V1", "V2"]),
                    shared_secret=dict(type="str", no_log=True),
                    bgp_session_config=dict(
                        type="dict",
                        options=dict(
                            oracle_interface_ip=dict(type="str"),
                            customer_interface_ip=dict(type="str"),
                            oracle_interface_ipv6=dict(type="str"),
                            customer_interface_ipv6=dict(type="str"),
                            customer_bgp_asn=dict(type="str"),
                        ),
                    ),
                    oracle_initiation=dict(
                        type="str", choices=["INITIATOR_OR_RESPONDER", "RESPONDER_ONLY"]
                    ),
                    nat_translation_enabled=dict(
                        type="str", choices=["ENABLED", "DISABLED", "AUTO"]
                    ),
                    phase_one_config=dict(
                        type="dict",
                        options=dict(
                            is_custom_phase_one_config=dict(type="bool"),
                            authentication_algorithm=dict(
                                type="str", choices=["SHA2_384", "SHA2_256", "SHA1_96"]
                            ),
                            encryption_algorithm=dict(
                                type="str",
                                choices=["AES_256_CBC", "AES_192_CBC", "AES_128_CBC"],
                            ),
                            diffie_helman_group=dict(
                                type="str",
                                choices=[
                                    "GROUP2",
                                    "GROUP5",
                                    "GROUP14",
                                    "GROUP19",
                                    "GROUP20",
                                    "GROUP24",
                                ],
                            ),
                            lifetime_in_seconds=dict(type="int"),
                        ),
                    ),
                    phase_two_config=dict(
                        type="dict",
                        options=dict(
                            is_custom_phase_two_config=dict(type="bool"),
                            authentication_algorithm=dict(
                                type="str",
                                choices=["HMAC_SHA2_256_128", "HMAC_SHA1_128"],
                            ),
                            encryption_algorithm=dict(
                                type="str",
                                choices=[
                                    "AES_256_GCM",
                                    "AES_192_GCM",
                                    "AES_128_GCM",
                                    "AES_256_CBC",
                                    "AES_192_CBC",
                                    "AES_128_CBC",
                                ],
                            ),
                            lifetime_in_seconds=dict(type="int"),
                            is_pfs_enabled=dict(type="bool"),
                            pfs_dh_group=dict(
                                type="str",
                                choices=[
                                    "GROUP2",
                                    "GROUP5",
                                    "GROUP14",
                                    "GROUP19",
                                    "GROUP20",
                                    "GROUP24",
                                ],
                            ),
                        ),
                    ),
                    dpd_config=dict(
                        type="dict",
                        options=dict(
                            dpd_mode=dict(
                                type="str",
                                choices=["INITIATE_AND_RESPOND", "RESPOND_ONLY"],
                            ),
                            dpd_timeout_in_sec=dict(type="int"),
                        ),
                    ),
                    encryption_domain_config=dict(
                        type="dict",
                        options=dict(
                            oracle_traffic_selector=dict(type="list", elements="str"),
                            cpe_traffic_selector=dict(type="list", elements="str"),
                        ),
                    ),
                ),
            ),
            defined_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            cpe_local_identifier=dict(type="str"),
            cpe_local_identifier_type=dict(
                type="str", choices=["IP_ADDRESS", "HOSTNAME"]
            ),
            static_routes=dict(type="list", elements="str"),
            ipsc_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="ip_sec_connection",
        service_client_class=VirtualNetworkClient,
        namespace="core",
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
