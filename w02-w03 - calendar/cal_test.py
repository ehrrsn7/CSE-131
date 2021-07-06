
import cal
import pytest

def test_is_leap_year():
    assert cal.is_leap_year(1992) == True
    assert cal.is_leap_year(2000) == True
    assert cal.is_leap_year(1900) == False

def test_days_in_month():
    assert cal.get_days_in_month(1753, 1)   == 31
    assert cal.get_days_in_month(1753, 3)   == 31
    assert cal.get_days_in_month(1753, 5)   == 31
    assert cal.get_days_in_month(1753, 7)   == 31
    assert cal.get_days_in_month(1753, 8)   == 31
    assert cal.get_days_in_month(1753, 10)  == 31
    assert cal.get_days_in_month(1753, 12)  == 31

    assert cal.get_days_in_month(1753, 4)   == 30
    assert cal.get_days_in_month(1753, 6)   == 30
    assert cal.get_days_in_month(1753, 9)   == 30
    assert cal.get_days_in_month(1753, 11)  == 30

    assert cal.get_days_in_month(2020, 2)   == 29
    assert cal.get_days_in_month(1753, 2)   == 28

def test_calculate_offset():
    assert cal.calculate_offset(2021, 1) == 5
    assert cal.calculate_offset(2017, 3) == 3
    assert cal.calculate_offset(1990, 12) == 6
    assert cal.calculate_offset(1984, 10) == 1

pytest.main(["-v", "--tb=no", "cal_test.py"])
