from hexlet_pytest.example import reverse


def test_reverse():
    assert reverse('Hexlet') == 'telxeH'


def test_reverse_for_empty_string():
    assert reverse('') == ''

def test_extra():
    input_file = 'test_data/input_data.txt'
    output_file = 'test_data/output_data.txt'
    with open(input_file) as f:
        input = f.read()
    with open(output_file) as f:
        output = f.read()
    print(input)
    print(reverse(input))
    print(output)
    assert reverse(input) == output
