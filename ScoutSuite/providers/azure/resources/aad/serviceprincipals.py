from ScoutSuite.providers.azure.resources.base import AzureResources


class ServicePrincipals(AzureResources):
    async def fetch_all(self):
        for raw_service_principal in await self.facade.aad.get_service_principals():
            id, service_principal = await self._parse_service_principal(raw_service_principal)
            # exclude built-in service principals
            if service_principal['publisher_name'] != 'Microsoft Services':
                self[id] = service_principal

    async def _parse_service_principal(self, raw_service_principal):
        service_principal_dict = {
            'id': raw_service_principal.object_id,
            'name': raw_service_principal.display_name,
            'additional_properties': raw_service_principal.additional_properties,
            'deletion_timestamp': raw_service_principal.deletion_timestamp,
            'object_type': raw_service_principal.object_type,
            'account_enabled': raw_service_principal.account_enabled,
            'alternative_names': raw_service_principal.alternative_names,
            'app_name': raw_service_principal.app_display_name,
            'app_id': raw_service_principal.app_id,
            'app_owner_tenant_id': raw_service_principal.app_owner_tenant_id,
            'app_role_assignment_required': raw_service_principal.app_role_assignment_required,
            'app_roles': raw_service_principal.app_roles,
            'error_url': raw_service_principal.error_url,
            'homepage': raw_service_principal.homepage,
            'key_credentials': raw_service_principal.key_credentials,
            'logout_url': raw_service_principal.logout_url,
            'oauth2_permissions': raw_service_principal.oauth2_permissions,
            'password_credentials': raw_service_principal.password_credentials,
            'preferred_token_signing_key_thumbprint': raw_service_principal.preferred_token_signing_key_thumbprint,
            'publisher_name': raw_service_principal.publisher_name,
            'reply_urls': raw_service_principal.reply_urls,
            'saml_metadata_url': raw_service_principal.saml_metadata_url,
            'service_principal_names': raw_service_principal.service_principal_names,
            'service_principal_type': raw_service_principal.service_principal_type,
            'tags': raw_service_principal.tags,
            'roles': [],
        }

        return service_principal_dict['id'], service_principal_dict

