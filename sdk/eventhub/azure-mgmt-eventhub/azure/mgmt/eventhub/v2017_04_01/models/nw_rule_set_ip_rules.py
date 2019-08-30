# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class NWRuleSetIpRules(Model):
    """Description of NetWorkRuleSet - IpRules resource.

    :param ip_mask: IP Mask
    :type ip_mask: str
    :param action: The IP Filter Action. Possible values include: 'Allow'.
     Default value: "Allow" .
    :type action: str or
     ~azure.mgmt.eventhub.v2017_04_01.models.NetworkRuleIPAction
    """

    _attribute_map = {
        'ip_mask': {'key': 'ipMask', 'type': 'str'},
        'action': {'key': 'action', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(NWRuleSetIpRules, self).__init__(**kwargs)
        self.ip_mask = kwargs.get('ip_mask', None)
        self.action = kwargs.get('action', "Allow")