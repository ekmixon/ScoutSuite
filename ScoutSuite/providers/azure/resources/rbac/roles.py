from ScoutSuite.providers.azure.facade.base import AzureFacade
from ScoutSuite.providers.azure.resources.base import AzureResources


class Roles(AzureResources):

    def __init__(self, facade: AzureFacade, subscription_id: str):
        super().__init__(facade)
        self.subscription_id = subscription_id

    async def fetch_all(self):
        for raw_role in await self.facade.rbac.get_roles(self.subscription_id):
            id, role = self._parse_role(raw_role)
            self[id] = role

    def _parse_role(self, raw_role):
        role_dict = {
            'id': raw_role.name,
            'name': raw_role.role_name,
            'type': raw_role.type,
            'description': raw_role.description,
            'role_type': raw_role.role_type,
            'permissions': raw_role.permissions,
            'assignable_scopes': raw_role.assignable_scopes,
            'additional_properties': raw_role.additional_properties,
            'assignments_count': 0,
            'assignments': {'users': [], 'groups': [], 'service_principals': []},
        }

        return role_dict['id'], role_dict
