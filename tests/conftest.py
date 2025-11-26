import pytest


def test_pytest_import():
    """Проверка что pytest импортируется корректно"""
    assert True


# def test_module_import():
#        from masks import get_mask_card_number, get_mask_account
#        assert True
#    except ImportError:
#        pytest.fail("Не удалось импортировать модули")


@pytest.fixture
def common_transaction_data():
    """Общая фикстура с транзакциями для нескольких тестовых модулей"""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-01-15T10:30:00.000000", "amount": 1000},
        {"id": 2, "state": "PENDING", "date": "2024-01-10T14:45:00.000000", "amount": 2000},
        {"id": 3, "state": "EXECUTED", "date": "2024-01-20T09:15:00.000000", "amount": 3000},
    ]
