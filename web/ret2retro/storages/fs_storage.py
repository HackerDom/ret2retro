import os
from ret2retro.storages.base import BaseStorage


class FsStorage(BaseStorage):
    def __init__(self, path, *args, **kwargs):
        super(FsStorage, self).__init__(*args, **kwargs)
        self.path = path

    def _get_file_name(self, filename):
        return os.path.join(self.path, filename)

    def get_resource(self, name):
        try:
            with open(self._get_file_name(name), 'rb') as f:
                return f.read()
        except FileNotFoundError:
            return

    def add_resource(self, name, data):
        with open(self._get_file_name(name), 'wb') as f:
            f.write(data)
