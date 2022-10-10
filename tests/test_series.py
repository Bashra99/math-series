from math_series.series import *
import pytest
def test_fibonacci():
    assert fibonacci(0)==0
    assert fibonacci(1)==1
    assert fibonacci(2)==1
    assert fibonacci(3)==2
    assert fibonacci(4)==3
    assert fibonacci(5)==5
    assert fibonacci(6)==8
    assert fibonacci(7)==13
    assert fibonacci(8)==21
    assert fibonacci(9)==34
    assert fibonacci(10)==55

def test_lucas():
    assert lucas(0)==2
    assert lucas(1)==1
    assert lucas(2)==3
    assert lucas(3)==4
    assert lucas(4)==7
    assert lucas(5)==11
    assert lucas(6)==18
    assert lucas(7)==29
    assert lucas(8)==47
    assert lucas(9)==76
    assert lucas(10)==123


def test_sum_series():
    assert sum_series(0)==0
    assert sum_series(1)==1
    assert sum_series(2)==1
    assert sum_series(3)==2
    assert sum_series(4)==3
    assert sum_series(5)==5
    assert sum_series(6)==8
    assert sum_series(7)==13
    assert sum_series(8)==21
    assert sum_series(9)==34
    assert sum_series(10)==55



