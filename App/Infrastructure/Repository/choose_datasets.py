class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class ChooseDatasets(metaclass=SingletonMeta):

    def __init__(self):
        self.usar_datasets_depurados = False

    def cambiar_datasets(self, es_depurados):
        self.usar_datasets_depurados = es_depurados

    def es_tipo_depurado(self):
        return self.usar_datasets_depurados
