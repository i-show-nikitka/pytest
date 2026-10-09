import pytest
from calculator import calculate_commission

class TestCalculateCommission:
    @pytest.mark.parametrize("amount, expected", [
        (100, 50.0),
        (1000, 50.0),
        (1001, 100.0),
        (20000, 100.0),
        (20001, 400.01),
        (40000, 600.0), 
        (50000, 500.0)])
    def test_commission_calculation(self, amount, expected):
        assert calculate_commission(amount) == pytest.approx(expected)
  
    @pytest.mark.parametrize("invalid_amount", [99, 50001, -1, 0])
    def test_commission_invalid_amount_raises_value_error(self, invalid_amount):
        with pytest.raises(ValueError):
            calculate_commission(invalid_amount)


    @pytest.mark.parametrize("invalid_type", ["abc", None, 100.5])
    def test_commission_invalid_type_raises_type_error(self, invalid_type):
        with pytest.raises(TypeError):
            calculate_commission(invalid_type) 
            
class TestNewRule:
    """Тесты для нового правила: сумма > 40000 - комиссия 500"""
    
    @pytest.mark.parametrize("amount, expected", [
        (40001, 500.0),   
        (45000, 500.0),   
        (49999, 500.0),  
    ])
    def test_commission_over_40000_is_fixed(self, amount, expected):
        assert calculate_commission(amount) == pytest.approx(expected)