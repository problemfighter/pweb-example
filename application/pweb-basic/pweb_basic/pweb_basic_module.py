import os

from pweb import PWebComponentRegister, PWebModuleDetails
from pweb_auth import PWebAuthRegistry
from pweb_basic.controller.basic_controller import basic_controller
from pweb_basic.controller.crud_controller import crud_controller
from pweb_basic.controller.exp_controller import ExpController
from pweb_basic.controller.file_holder_controller import file_holder_controller
from pweb_basic.controller.form_controller import form_controller
from pweb_basic.controller.form_raw_controller import form_raw_controller
from pweb_basic.controller.rest_api_controller import rest_api_controller
from pweb_basic.controller.saas_controller import saas_controller
from pweb_basic.controller.socket_controller import socket_controller
from pweb_basic.controller.ssr_controller import ssr_controller
from pweb_basic.controller.xyz_controller import xyz_controller
from pweb_extra.pws.pweb_socket import PWebSocket


class PWebBasicModule(PWebComponentRegister):

    def app_details(self) -> PWebModuleDetails:
        return PWebModuleDetails(system_name="pweb-basic")

    def run_on_cli_init(self, pweb_app, config):
        pass

    def run_on_start(self, pweb_app, config):
        print("run_on_start Environment : " + os.environ.get('env', 'Local'))
        print("run_on_start Environment : " + os.environ.get('abulkabul', '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'))
        print(os.environ)
        PWebAuthRegistry.add_start_with_url_in_skip("/pweb-socket")
        if pweb_app.is_app_loaded():
            print("Call Once during app load")
            PWebSocket.register(pweb_app=pweb_app)

    def register_model(self, pweb_db):
        pass

    def register_controller(self, pweb_app):
        pweb_app.register_blueprint(basic_controller)
        pweb_app.register_blueprint(crud_controller)
        pweb_app.register_blueprint(saas_controller)
        pweb_app.register_blueprint(rest_api_controller)
        pweb_app.register_blueprint(file_holder_controller)
        pweb_app.register_blueprint(form_controller)
        pweb_app.register_blueprint(ssr_controller)
        pweb_app.register_blueprint(form_raw_controller)
        pweb_app.register_blueprint(xyz_controller)
        pweb_app.register_blueprint(socket_controller)
        ExpController.init_controller(pweb_app)
