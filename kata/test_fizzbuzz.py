from fizzbuzz import fizzbuzz

def load_expected_outputs(filename):
    expected_outputs = {}
    with open(filename, 'r') as file:
        for number in range(1, 101):
            expected_outputs[number] = file.readline().strip()  # Read each line for numbers 1 to 100
    return expected_outputs

def test_fizzbuzz():
    expected_outputs = load_expected_outputs('testdata/fizzbuzz_stage1.txt')
    
    for number in range(1, 101):
        assert fizzbuzz(number) == expected_outputs[number]
