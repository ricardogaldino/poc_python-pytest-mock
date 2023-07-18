from src.adapters.my_adapter import MyAdapter
from src.use_cases.my_use_case import MyUseCase


class Main:
    def __init__(self) -> None:
        self.my_adapter = MyAdapter()
        self.my_use_case = MyUseCase(self.my_adapter)

    def execute(self):
        self.my_use_case.execute()
