# pytestサンプル
## 環境構築
Windows10 + Python3.9 + Gitbash
```
cd python-pytest-sample

python -V
 > Python 3.9.5

python -m venv venv

source venv/Scripts/Activate
```

## ディレクトリ構成
```
srcs [IntelliJ Sources Root]
  - file_transfer
    - xxx.py
test
  - file_transfer
    - test_xxx.py
  - conftest.py
 requirements.txt
 setup.py
```

## Lint、Formatter
* https://github.com/Y-Suzaki/python-advanced-sample

## pytest実行
1. setup.pyに、srcs以下のパスを通す。
   * これがないと、IDE（IntelliJ）上ではパスが通っているように見えるが、pytest実行時にModuleNotFoundErrorになる。
2. 全テスト実行 コマンド
    ```
    pytest -v --capture=no
    ```
3. 任意のテストのみ実行 コマンド
    ```
    pytest -v --capture=no tests/file_transfer/test_file_
    transfer.py::test_get_ip
    ```
4. 任意のテスト名を含むテストのみ実行 コマンド
    ```
    pytest -v --capture=no -k "_print_"
    ```
5. 任意のmarkerを含むテストのみ実行 コマンド
```
# カレントディレクトリにpytest.iniがないと読み込まれなかった。
cd tests
pytest -v --capture=no -m run_print
```

# 参考URL
* https://httpbin.org/
    * 通信系の疎通確認に使えるお便利サイト