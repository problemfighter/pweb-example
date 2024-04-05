from pweb import PWebAppConfig
from pweb_auth import AuthBase
from pweb_basic.common.app_ssr_ui_helper import AppSSRUIHelper
from pweb_form_rest import PWebSSRUIHelper
from pweb_ssr import SSRTemplateAssets


class Config(PWebAppConfig):
    APP_NAME = "PWeb Example"
    PORT: int = 1212

    SWAGGER_TITLE: str = "Swagger Example App"
    SSR_UI_HELPER: PWebSSRUIHelper = AppSSRUIHelper()

    DEFAULT_TEMPLATE_ASSETS: SSRTemplateAssets = SSRTemplateAssets(
        name="example",
        import_name=__name__,
        template_folder="../template-assets/templates",
        static_folder="../template-assets/assets",
        static_url_path="app-assets"
    )

    TOTAL_ITEM_PER_PAGE: int = 5
    TABLE_ITEM_PER_PAGE_OPTIONS: str = [5, 10, 25, 50, 100, 200, 500]
    SYSTEM_AUTH_BASE: AuthBase = AuthBase.EMAIL
    ENABLE_REGISTRATION: bool = True
    IS_ENABLE_AUTH: bool = True
