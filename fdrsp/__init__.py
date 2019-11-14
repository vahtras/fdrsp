import tempfile


class TmpDir:
    """
    A class following the Singleton pattern to yield
    a unique temporary directory instance on each call
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = tempfile.mkdtemp()
        return cls._instance
