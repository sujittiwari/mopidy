from __future__ import unicode_literals

import os

import mopidy
from mopidy import ext
from mopidy.utils import config


class Extension(ext.Extension):

    dist_name = 'Mopidy-MPD'
    ext_name = 'mpd'
    version = mopidy.__version__

    def get_default_config(self):
        conf_file = os.path.join(os.path.dirname(__file__), 'ext.conf')
        return open(conf_file).read()

    def get_config_schema(self):
        schema = config.ExtensionConfigSchema()
        schema['hostname'] = config.Hostname()
        schema['port'] = config.Port()
        schema['password'] = config.String(optional=True, secret=True)
        schema['max_connections'] = config.Integer(minimum=1)
        schema['connection_timeout'] = config.Integer(minimum=1)
        return schema

    def validate_environment(self):
        pass

    def get_frontend_classes(self):
        from .actor import MpdFrontend
        return [MpdFrontend]
