import tempfile


class TmpDir:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = tempfile.mkdtemp()
        return cls._instance
