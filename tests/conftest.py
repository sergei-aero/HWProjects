import pytest

def test_pytest_import():
    """Проверка что pytest импортируется корректно"""
    assert True

def test_module_import():
    """Проверка что модули импортируются корректно"""
    try:
        from masks import get_mask_card_number, get_mask_account
        assert True
    except ImportError:
        pytest.fail("Не удалось импортировать модули")
