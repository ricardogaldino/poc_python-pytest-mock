from src.adapters.my_adapter import MyAdapter


class MyUseCase:
    def __init__(self, my_adapter: MyAdapter):
        self.my_adapter = my_adapter

    def execute(self):
        return self.my_adapter.get()
