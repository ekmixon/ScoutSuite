import oss2
from aliyunsdkcore.client import AcsClient

from ScoutSuite.core.console import print_exception


def get_client(credentials, region=None):
    try:
        return AcsClient(
            credential=credentials.credentials,
            region_id=region or 'cn-hangzhou',
        )


    except Exception as e:
        print_exception(e)
        return None


def get_oss_client(credentials, region=None):
    try:
        auth = oss2.Auth(credentials.credentials.access_key_id, credentials.credentials.access_key_secret)
        return oss2.Service(
            auth,
            endpoint=f'oss-{region}.aliyuncs.com'
            if region
            else 'oss-cn-hangzhou.aliyuncs.com',
        )


    except Exception as e:
        print_exception(e)
        return None
