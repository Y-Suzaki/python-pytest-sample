from file_transfer_sub.file_transfer import print_out as print_out_sub
from file_transfer.file_transfer import print_out, get_ip


def test_print_1():
    print_out_sub('Hello Pytest World 1.')
    assert True


def test_print_2():
    print_out('Hello Pytest World 2.')
    assert True


def test_get_ip():
    ip: dict = get_ip()
    print(f'{ip=}')
    assert ip.get('origin', None) is not None
