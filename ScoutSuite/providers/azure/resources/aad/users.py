from ScoutSuite.providers.azure.resources.base import AzureResources


class Users(AzureResources):
    async def fetch_all(self):
        for raw_user in await self.facade.aad.get_users():
            id, user = await self._parse_user(raw_user)
            self[id] = user

    async def fetch_additional_users(self, user_list):
        """
        Alternative method which only fetches defined users
        :param user_list: a list of the users to fetch and parse
        """
        for user in user_list:
            raw_user = await self.facade.aad.get_user(user)
            if raw_user:
                id, user = await self._parse_user(raw_user)
                self[id] = user

    async def _parse_user(self, raw_user):
        user_dict = {
            'id': raw_user.object_id,
            'additional_properties': raw_user.additional_properties,
            'deletion_timestamp': raw_user.deletion_timestamp,
            'object_type': raw_user.object_type,
            'immutable_id': raw_user.immutable_id,
            'usage_location': raw_user.usage_location,
            'given_name': raw_user.given_name,
            'surname': raw_user.surname,
            'account_enabled': raw_user.account_enabled,
            'display_name': raw_user.display_name,
            'name': raw_user.user_principal_name,
            'mail_nickname': raw_user.mail_nickname,
            'mail': raw_user.mail,
            'sign_in_names': raw_user.sign_in_names,
            'user_type': raw_user.user_type,
        }

        user_dict['groups'] = await self.facade.aad.get_user_groups(user_dict['id'])
        user_dict['roles'] = []  # this will be filled in `finalize()`

        return user_dict['id'], user_dict
