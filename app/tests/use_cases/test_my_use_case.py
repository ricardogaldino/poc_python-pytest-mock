from src.adapters.my_adapter import MyAdapter
from src.use_cases.my_use_case import MyUseCase


def test_my_usecase(mocker):
    # arrange
    expected_result = "Xpto"

    mock_my_adapter = mocker.Mock(spec=MyAdapter)
    mock_my_adapter.get.return_value = expected_result

    my_use_case = MyUseCase(mock_my_adapter)

    # act
    result = my_use_case.execute()

    # assert
    assert result == expected_result
