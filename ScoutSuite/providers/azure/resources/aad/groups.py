from ScoutSuite.providers.azure.resources.base import AzureResources


class Groups(AzureResources):
    async def fetch_all(self):
        for raw_group in await self.facade.aad.get_groups():
            id, group = await self._parse_group(raw_group)
            self[id] = group

    async def _parse_group(self, raw_group):

        group_dict = {
            'id': raw_group.object_id,
            'name': raw_group.display_name,
            'additional_properties': raw_group.additional_properties,
            'deletion_timestamp': raw_group.deletion_timestamp,
            'object_type': raw_group.object_type,
            'mail_enabled': raw_group.mail_enabled,
            'mail_nickname': raw_group.mail_nickname,
            'security_enabled': raw_group.security_enabled,
            'mail': raw_group.mail,
            'users': [],
            'roles': [],
        }


        return group_dict['id'], group_dict

