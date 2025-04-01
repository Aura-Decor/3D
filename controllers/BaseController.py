import os

class BaseController:
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.dirname(__file__))