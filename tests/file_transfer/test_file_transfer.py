import pytest
from file_transfer_sub.file_transfer import print_out as print_out_sub

from file_transfer.file_transfer import get_ip, print_out


def test_print_1():
    """
    Tests:
        test_print_1のテスト。
    Expects:
        Print1が標準出力されること。
    """
    print_out_sub('Hello Pytest World 1.')
    assert True


# @pytest.mark.run_print
# def test_print_2():
#     """
#     Tests:
#         test_print_2のテスト。
#     Expects:
#         Print1が標準出力されること。
#     """
#     print_out('Hello Pytest World 2.')
#     assert True
#
#
# def test_get_ip():
#     """
#     Tests:
#         test_get_ipのテスト。
#     Expects:
#         自身のIPアドレスが出力されること。
#     """
#     ip: dict = get_ip()
#     print(f'{ip=}')
#     assert ip.get('origin', None) is not None
