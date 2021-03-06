#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
module: oci_loadbalancer_load_balancer_facts
short_description: Fetches details about one or multiple LoadBalancer resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple LoadBalancer resources in Oracle Cloud Infrastructure
    - Lists all load balancers in the specified compartment.
    - If I(load_balancer_id) is specified, the details of a single LoadBalancer will be returned.
version_added: "2.5"
options:
    load_balancer_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the load balancer to retrieve.
            - Required to get a specific load_balancer.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment containing the load balancers to list.
            - Required to list multiple load_balancers.
        type: str
    detail:
        description:
            - The level of detail to return for each result. Can be `full` or `simple`.
            - "Example: `full`"
        type: str
    sort_by:
        description:
            - The field to sort by.  You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending.
              Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.
        type: str
        choices:
            - "ASC"
            - "DESC"
    display_name:
        description:
            - A filter to return only resources that match the given display name exactly.
            - "Example: `example_load_balancer`"
        type: str
        aliases: ["name"]
    lifecycle_state:
        description:
            - A filter to return only resources that match the given lifecycle state.
            - "Example: `SUCCEEDED`"
        type: str
        choices:
            - "CREATING"
            - "FAILED"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List load_balancers
  oci_loadbalancer_load_balancer_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific load_balancer
  oci_loadbalancer_load_balancer_facts:
    load_balancer_id: ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
load_balancers:
    description:
        - List of LoadBalancer resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the load balancer.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment containing the load balancer.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        display_name:
            description:
                - A user-friendly name. It does not have to be unique, and it is changeable.
                - "Example: `example_load_balancer`"
            returned: on success
            type: string
            sample: example_load_balancer
        lifecycle_state:
            description:
                - The current state of the load balancer.
            returned: on success
            type: string
            sample: CREATING
        time_created:
            description:
                - The date and time the load balancer was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        ip_addresses:
            description:
                - An array of IP addresses.
            returned: on success
            type: complex
            contains:
                ip_address:
                    description:
                        - An IP address.
                        - "Example: `192.168.0.3`"
                    returned: on success
                    type: string
                    sample: 192.168.0.3
                is_public:
                    description:
                        - Whether the IP address is public or private.
                        - "If \\"true\\", the IP address is public and accessible from the internet."
                        - "If \\"false\\", the IP address is private and accessible only from within the associated VCN."
                    returned: on success
                    type: bool
                    sample: true
        shape_name:
            description:
                - A template that determines the total pre-provisioned bandwidth (ingress plus egress).
                  To get a list of available shapes, use the L(ListShapes,https://docs.cloud.oracle.com/#/en/loadbalancer/20170115/LoadBalancerShape/ListShapes)
                  operation.
                - "Example: `100Mbps`"
            returned: on success
            type: string
            sample: 100Mbps
        is_private:
            description:
                - Whether the load balancer has a VCN-local (private) IP address.
                - "If \\"true\\", the service assigns a private IP address to the load balancer."
                - "If \\"false\\", the service assigns a public IP address to the load balancer."
                - A public load balancer is accessible from the internet, depending on your VCN's
                  L(security list rules,https://docs.cloud.oracle.com/Content/Network/Concepts/securitylists.htm). For more information about public and
                  private load balancers, see L(How Load Balancing Works,https://docs.cloud.oracle.com/Content/Balance/Concepts/balanceoverview.htm#how-load-
                  balancing-works).
                - "Example: `true`"
            returned: on success
            type: bool
            sample: true
        subnet_ids:
            description:
                - An array of subnet L(OCIDs,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            returned: on success
            type: list
            sample: []
        listeners:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - A friendly name for the listener. It must be unique and it cannot be changed.
                        - "Example: `example_listener`"
                    returned: on success
                    type: string
                    sample: example_listener
                default_backend_set_name:
                    description:
                        - The name of the associated backend set.
                        - "Example: `example_backend_set`"
                    returned: on success
                    type: string
                    sample: example_backend_set
                port:
                    description:
                        - The communication port for the listener.
                        - "Example: `80`"
                    returned: on success
                    type: int
                    sample: 0
                protocol:
                    description:
                        - The protocol on which the listener accepts connection requests.
                          To get a list of valid protocols, use the
                          L(ListProtocols,https://docs.cloud.oracle.com/#/en/loadbalancer/20170115/LoadBalancerProtocol/ListProtocols)
                          operation.
                        - "Example: `HTTP`"
                    returned: on success
                    type: string
                    sample: HTTP
                hostname_names:
                    description:
                        - An array of hostname resource names.
                    returned: on success
                    type: list
                    sample: []
                path_route_set_name:
                    description:
                        - The name of the set of path-based routing rules,
                          L(PathRouteSet,https://docs.cloud.oracle.com/#/en/loadbalancer/20170115/PathRouteSet/),
                          applied to this listener's traffic.
                        - "Example: `example_path_route_set`"
                    returned: on success
                    type: string
                    sample: example_path_route_set
                ssl_configuration:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        certificate_name:
                            description:
                                - A friendly name for the certificate bundle. It must be unique and it cannot be changed.
                                  Valid certificate bundle names include only alphanumeric characters, dashes, and underscores.
                                  Certificate bundle names cannot contain spaces. Avoid entering confidential information.
                                - "Example: `example_certificate_bundle`"
                            returned: on success
                            type: string
                            sample: example_certificate_bundle
                        verify_peer_certificate:
                            description:
                                - Whether the load balancer listener should verify peer certificates.
                                - "Example: `true`"
                            returned: on success
                            type: bool
                            sample: true
                        verify_depth:
                            description:
                                - The maximum depth for peer certificate chain verification.
                                - "Example: `3`"
                            returned: on success
                            type: int
                            sample: 3
                connection_configuration:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        idle_timeout:
                            description:
                                - The maximum idle time, in seconds, allowed between two successive receive or two successive send operations
                                  between the client and backend servers. A send operation does not reset the timer for receive operations. A
                                  receive operation does not reset the timer for send operations.
                                - For more information, see L(Connection
                                  Configuration,https://docs.cloud.oracle.com/Content/Balance/Reference/connectionreuse.htm#ConnectionConfiguration).
                                - "Example: `1200`"
                            returned: on success
                            type: int
                            sample: 1200
                rule_set_names:
                    description:
                        - The names of the L(rule sets,https://docs.cloud.oracle.com/#/en/loadbalancer/20170115/RuleSet/) to apply to the listener.
                        - "Example: [\\"example_rule_set\\"]"
                    returned: on success
                    type: list
                    sample: []
        hostnames:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - A friendly name for the hostname resource. It must be unique and it cannot be changed. Avoid entering confidential
                          information.
                        - "Example: `example_hostname_001`"
                    returned: on success
                    type: string
                    sample: example_hostname_001
                hostname:
                    description:
                        - A virtual hostname. For more information about virtual hostname string construction, see
                          L(Managing Request Routing,https://docs.cloud.oracle.com/Content/Balance/Tasks/managingrequest.htm#routing).
                        - "Example: `app.example.com`"
                    returned: on success
                    type: string
                    sample: app.example.com
        certificates:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                certificate_name:
                    description:
                        - A friendly name for the certificate bundle. It must be unique and it cannot be changed.
                          Valid certificate bundle names include only alphanumeric characters, dashes, and underscores.
                          Certificate bundle names cannot contain spaces. Avoid entering confidential information.
                        - "Example: `example_certificate_bundle`"
                    returned: on success
                    type: string
                    sample: example_certificate_bundle
                public_certificate:
                    description:
                        - The public certificate, in PEM format, that you received from your SSL certificate provider.
                        - "Example:"
                        -     -----BEGIN CERTIFICATE-----
                              MIIC2jCCAkMCAg38MA0GCSqGSIb3DQEBBQUAMIGbMQswCQYDVQQGEwJKUDEOMAwG
                              A1UECBMFVG9reW8xEDAOBgNVBAcTB0NodW8ta3UxETAPBgNVBAoTCEZyYW5rNERE
                              MRgwFgYDVQQLEw9XZWJDZXJ0IFN1cHBvcnQxGDAWBgNVBAMTD0ZyYW5rNEREIFdl
                              YiBDQTEjMCEGCSqGSIb3DQEJARYUc3VwcG9ydEBmcmFuazRkZC5jb20wHhcNMTIw
                              ...
                              -----END CERTIFICATE-----
                    returned: on success
                    type: string
                    sample: public_certificate_example
                ca_certificate:
                    description:
                        - The Certificate Authority certificate, or any interim certificate, that you received from your SSL certificate provider.
                        - "Example:"
                        -     -----BEGIN CERTIFICATE-----
                              MIIEczCCA1ugAwIBAgIBADANBgkqhkiG9w0BAQQFAD..AkGA1UEBhMCR0Ix
                              EzARBgNVBAgTClNvbWUtU3RhdGUxFDASBgNVBAoTC0..0EgTHRkMTcwNQYD
                              VQQLEy5DbGFzcyAxIFB1YmxpYyBQcmltYXJ5IENlcn..XRpb24gQXV0aG9y
                              aXR5MRQwEgYDVQQDEwtCZXN0IENBIEx0ZDAeFw0wMD..TUwMTZaFw0wMTAy
                              ...
                              -----END CERTIFICATE-----
                    returned: on success
                    type: string
                    sample: ca_certificate_example
        backend_sets:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - A friendly name for the backend set. It must be unique and it cannot be changed.
                        - Valid backend set names include only alphanumeric characters, dashes, and underscores. Backend set names cannot
                          contain spaces. Avoid entering confidential information.
                        - "Example: `example_backend_set`"
                    returned: on success
                    type: string
                    sample: example_backend_set
                policy:
                    description:
                        - The load balancer policy for the backend set. To get a list of available policies, use the
                          L(ListPolicies,https://docs.cloud.oracle.com/#/en/loadbalancer/20170115/LoadBalancerPolicy/ListPolicies) operation.
                        - "Example: `LEAST_CONNECTIONS`"
                    returned: on success
                    type: string
                    sample: LEAST_CONNECTIONS
                backends:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - A read-only field showing the IP address and port that uniquely identify this backend server in the backend set.
                                - "Example: `10.0.0.3:8080`"
                            returned: on success
                            type: string
                            sample: 10.0.0.3:8080
                        ip_address:
                            description:
                                - The IP address of the backend server.
                                - "Example: `10.0.0.3`"
                            returned: on success
                            type: string
                            sample: 10.0.0.3
                        port:
                            description:
                                - The communication port for the backend server.
                                - "Example: `8080`"
                            returned: on success
                            type: int
                            sample: 8080
                        weight:
                            description:
                                - The load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger
                                  proportion of incoming traffic. For example, a server weighted '3' receives 3 times the number of new connections
                                  as a server weighted '1'.
                                  For more information on load balancing policies, see
                                  L(How Load Balancing Policies Work,https://docs.cloud.oracle.com/Content/Balance/Reference/lbpolicies.htm).
                                - "Example: `3`"
                            returned: on success
                            type: int
                            sample: 3
                        drain:
                            description:
                                - "Whether the load balancer should drain this server. Servers marked \\"drain\\" receive no new
                                  incoming traffic."
                                - "Example: `false`"
                            returned: on success
                            type: bool
                            sample: false
                        backup:
                            description:
                                - "Whether the load balancer should treat this server as a backup unit. If `true`, the load balancer forwards no ingress
                                  traffic to this backend server unless all other backend servers not marked as \\"backup\\" fail the health check policy."
                                - "**Note:** You cannot add a backend server marked as `backup` to a backend set that uses the IP Hash policy."
                                - "Example: `false`"
                            returned: on success
                            type: bool
                            sample: false
                        offline:
                            description:
                                - Whether the load balancer should treat this server as offline. Offline servers receive no incoming
                                  traffic.
                                - "Example: `false`"
                            returned: on success
                            type: bool
                            sample: false
                health_checker:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        protocol:
                            description:
                                - The protocol the health check must use; either HTTP or TCP.
                                - "Example: `HTTP`"
                            returned: on success
                            type: string
                            sample: HTTP
                        url_path:
                            description:
                                - The path against which to run the health check.
                                - "Example: `/healthcheck`"
                            returned: on success
                            type: string
                            sample: /healthcheck
                        port:
                            description:
                                - The backend server port against which to run the health check. If the port is not specified, the load balancer uses the
                                  port information from the `Backend` object.
                                - "Example: `8080`"
                            returned: on success
                            type: int
                            sample: 0
                        return_code:
                            description:
                                - "The status code a healthy backend server should return. If you configure the health check policy to use the HTTP protocol,
                                  you can use common HTTP status codes such as \\"200\\"."
                                - "Example: `200`"
                            returned: on success
                            type: int
                            sample: 0
                        retries:
                            description:
                                - "The number of retries to attempt before a backend server is considered \\"unhealthy\\". This number also applies
                                  when recovering a server to the \\"healthy\\" state. Defaults to 3."
                                - "Example: `3`"
                            returned: on success
                            type: int
                            sample: 3
                        timeout_in_millis:
                            description:
                                - The maximum time, in milliseconds, to wait for a reply to a health check. A health check is successful only if a reply
                                  returns within this timeout period. Defaults to 3000 (3 seconds).
                                - "Example: `3000`"
                            returned: on success
                            type: int
                            sample: 3000
                        interval_in_millis:
                            description:
                                - The interval between health checks, in milliseconds. The default is 10000 (10 seconds).
                                - "Example: `10000`"
                            returned: on success
                            type: int
                            sample: 10000
                        response_body_regex:
                            description:
                                - A regular expression for parsing the response body from the backend server.
                                - "Example: `^((?!false).|\\\\s)*$`"
                            returned: on success
                            type: string
                            sample: ^((?!false).|\\s)*$
                ssl_configuration:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        certificate_name:
                            description:
                                - A friendly name for the certificate bundle. It must be unique and it cannot be changed.
                                  Valid certificate bundle names include only alphanumeric characters, dashes, and underscores.
                                  Certificate bundle names cannot contain spaces. Avoid entering confidential information.
                                - "Example: `example_certificate_bundle`"
                            returned: on success
                            type: string
                            sample: example_certificate_bundle
                        verify_peer_certificate:
                            description:
                                - Whether the load balancer listener should verify peer certificates.
                                - "Example: `true`"
                            returned: on success
                            type: bool
                            sample: true
                        verify_depth:
                            description:
                                - The maximum depth for peer certificate chain verification.
                                - "Example: `3`"
                            returned: on success
                            type: int
                            sample: 3
                session_persistence_configuration:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        cookie_name:
                            description:
                                - "The name of the cookie used to detect a session initiated by the backend server. Use '*' to specify
                                  that any cookie set by the backend causes the session to persist."
                                - "Example: `example_cookie`"
                            returned: on success
                            type: string
                            sample: example_cookie
                        disable_fallback:
                            description:
                                - Whether the load balancer is prevented from directing traffic from a persistent session client to
                                  a different backend server if the original server is unavailable. Defaults to false.
                                - "Example: `false`"
                            returned: on success
                            type: bool
                            sample: false
        path_route_sets:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The unique name for this set of path route rules. Avoid entering confidential information.
                        - "Example: `example_path_route_set`"
                    returned: on success
                    type: string
                    sample: example_path_route_set
                path_routes:
                    description:
                        - The set of path route rules.
                    returned: on success
                    type: complex
                    contains:
                        path:
                            description:
                                - The path string to match against the incoming URI path.
                                - "*  Path strings are case-insensitive."
                                - "*  Asterisk (*) wildcards are not supported."
                                - "*  Regular expressions are not supported."
                                - "Example: `/example/video/123`"
                            returned: on success
                            type: string
                            sample: /example/video/123
                        path_match_type:
                            description:
                                - The type of matching to apply to incoming URIs.
                            returned: on success
                            type: complex
                            contains:
                                match_type:
                                    description:
                                        - Specifies how the load balancing service compares a
                                          L(PathRoute,https://docs.cloud.oracle.com/#/en/loadbalancer/20170115/requests/PathRoute)
                                          object's `path` string against the incoming URI.
                                        - "*  **EXACT_MATCH** - Looks for a `path` string that exactly matches the incoming URI path."
                                        - "*  **FORCE_LONGEST_PREFIX_MATCH** - Looks for the `path` string with the best, longest match of the beginning
                                             portion of the incoming URI path."
                                        - "*  **PREFIX_MATCH** - Looks for a `path` string that matches the beginning portion of the incoming URI path."
                                        - "*  **SUFFIX_MATCH** - Looks for a `path` string that matches the ending portion of the incoming URI path."
                                        - For a full description of how the system handles `matchType` in a path route set containing multiple rules, see
                                          L(Managing Request Routing,https://docs.cloud.oracle.com/Content/Balance/Tasks/managingrequest.htm).
                                    returned: on success
                                    type: string
                                    sample: EXACT_MATCH
                        backend_set_name:
                            description:
                                - The name of the target backend set for requests where the incoming URI matches the specified path.
                                - "Example: `example_backend_set`"
                            returned: on success
                            type: string
                            sample: example_backend_set
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        rule_sets:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The name for this set of rules. It must be unique and it cannot be changed. Avoid entering
                          confidential information.
                        - "Example: `example_rule_set`"
                    returned: on success
                    type: string
                    sample: example_rule_set
                items:
                    description:
                        - An array of rules that compose the rule set.
                    returned: on success
                    type: complex
                    contains:
                        action:
                            description:
                                - ""
                            returned: on success
                            type: string
                            sample: ADD_HTTP_REQUEST_HEADER
                        header:
                            description:
                                - A header name that conforms to RFC 7230.
                                - "Example: `example_header_name`"
                            returned: on success
                            type: string
                            sample: example_header_name
                        value:
                            description:
                                - A header value that conforms to RFC 7230.
                                - "Example: `example_value`"
                            returned: on success
                            type: string
                            sample: example_value
                        prefix:
                            description:
                                - A string to prepend to the header value. The resulting header value must conform to RFC 7230.
                                - "Example: `example_prefix_value`"
                            returned: on success
                            type: string
                            sample: example_prefix_value
                        suffix:
                            description:
                                - A string to append to the header value. The resulting header value must conform to RFC 7230.
                                - "Example: `example_suffix_value`"
                            returned: on success
                            type: string
                            sample: example_suffix_value
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "example_load_balancer",
        "lifecycle_state": "CREATING",
        "time_created": "2016-08-25T21:10:29.600Z",
        "ip_addresses": [{
            "ip_address": "192.168.0.3",
            "is_public": true
        }],
        "shape_name": "100Mbps",
        "is_private": true,
        "subnet_ids": [],
        "listeners": {
            "name": "example_listener",
            "default_backend_set_name": "example_backend_set",
            "port": 0,
            "protocol": "HTTP",
            "hostname_names": [],
            "path_route_set_name": "example_path_route_set",
            "ssl_configuration": {
                "certificate_name": "example_certificate_bundle",
                "verify_peer_certificate": true,
                "verify_depth": 3
            },
            "connection_configuration": {
                "idle_timeout": 1200
            },
            "rule_set_names": []
        },
        "hostnames": {
            "name": "example_hostname_001",
            "hostname": "app.example.com"
        },
        "certificates": {
            "certificate_name": "example_certificate_bundle",
            "public_certificate": "public_certificate_example",
            "ca_certificate": "ca_certificate_example"
        },
        "backend_sets": {
            "name": "example_backend_set",
            "policy": "LEAST_CONNECTIONS",
            "backends": [{
                "name": "10.0.0.3:8080",
                "ip_address": "10.0.0.3",
                "port": 8080,
                "weight": 3,
                "drain": false,
                "backup": false,
                "offline": false
            }],
            "health_checker": {
                "protocol": "HTTP",
                "url_path": "/healthcheck",
                "port": 0,
                "return_code": 0,
                "retries": 3,
                "timeout_in_millis": 3000,
                "interval_in_millis": 10000,
                "response_body_regex": "^((?!false).|\\\\s)*$"
            },
            "ssl_configuration": {
                "certificate_name": "example_certificate_bundle",
                "verify_peer_certificate": true,
                "verify_depth": 3
            },
            "session_persistence_configuration": {
                "cookie_name": "example_cookie",
                "disable_fallback": false
            }
        },
        "path_route_sets": {
            "name": "example_path_route_set",
            "path_routes": [{
                "path": "/example/video/123",
                "path_match_type": {
                    "match_type": "EXACT_MATCH"
                },
                "backend_set_name": "example_backend_set"
            }]
        },
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "rule_sets": {
            "name": "example_rule_set",
            "items": [{
                "action": "ADD_HTTP_REQUEST_HEADER",
                "header": "example_header_name",
                "value": "example_value",
                "prefix": "example_prefix_value",
                "suffix": "example_suffix_value"
            }]
        }
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.load_balancer import LoadBalancerClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class LoadBalancerFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "load_balancer_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_load_balancer,
            load_balancer_id=self.module.params.get("load_balancer_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "detail",
            "sort_by",
            "sort_order",
            "display_name",
            "lifecycle_state",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_load_balancers,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


LoadBalancerFactsHelperCustom = get_custom_class("LoadBalancerFactsHelperCustom")


class ResourceFactsHelper(LoadBalancerFactsHelperCustom, LoadBalancerFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            load_balancer_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            detail=dict(type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            display_name=dict(aliases=["name"], type="str"),
            lifecycle_state=dict(
                type="str",
                choices=["CREATING", "FAILED", "ACTIVE", "DELETING", "DELETED"],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="load_balancer",
        service_client_class=LoadBalancerClient,
        namespace="load_balancer",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(load_balancers=result)


if __name__ == "__main__":
    main()
