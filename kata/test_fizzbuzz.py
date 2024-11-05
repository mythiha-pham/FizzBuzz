import pytest
from fizzbuzz import fizzbuzz

def load_expected_outputs(filename):
    expected_outputs = {}
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

@pytest.mark.parametrize("stage, filename", [
    (1, 'testdata/fizzbuzz_stage1.txt'),
    (2, 'testdata/fizzbuzz_stage2.txt')
])

def test_fizzbuzz(stage, filename):
    expected_outputs = load_expected_outputs(filename)
    
    for number, expected_output in enumerate(expected_outputs, start=1):
        assert fizzbuzz(number, stage) == expected_output