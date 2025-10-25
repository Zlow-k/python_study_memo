# -*- coding: utf-8 -*-
"""
unittest と subTest() の使用例
- 例として、与えられた文字列が回文かどうかを判定する関数 is_palindrome() を実装
- 同一関数に対して複数入力をテーブル駆動で検証するために subTest() を活用
"""

import re
import unittest


def is_palindrome(s: str) -> bool:
    """回文判定関数
    - 大文字小文字は無視
    - 記号・空白は無視（英数字のみを対象）
    - None や非文字列は TypeError を送出
    """
    if not isinstance(s, str):
        raise TypeError("s must be str")

    # 英数字のみを抽出し、大小を無視して比較
    filtered = re.sub(r"[^0-9A-Za-z]", "", s).lower()
    return filtered == filtered[::-1]


class TestIsPalindrome(unittest.TestCase):
    """is_palindrome() のユニットテスト"""

    @classmethod
    def setUpClass(cls):
        # クラス全体で共有したい準備があればここで実施
        # （今回特に必須な準備はないが、雛形として記載）
        pass

    def test_palindrome_true_cases(self):
        """回文であると期待されるケースを subTest で一括検証"""
        # テーブル駆動（入力と期待値の組を列挙）
        cases = [
            ("", True),                        # 空文字
            ("a", True),                       # 1文字
            ("abba", True),                    # 偶数長
            ("abcba", True),                   # 奇数長
            ("A man, a plan, a canal: Panama", True),  # 記号・空白・大小混在
            ("No 'x' in Nixon", True),
            ("1234321", True),                 # 数字のみ
        ]

        for s, expected in cases:
            with self.subTest():
                self.assertEqual(is_palindrome(s), expected)

    def test_palindrome_false_cases(self):
        """回文でないと期待されるケースを subTest で一括検証"""
        cases = [
            ("ab", False),
            ("abca", False),
            ("hello", False),
            ("12345", False),
            ("Python", True),  # 大文字小文字を無視しても回文でない
        ]
        for s, expected in cases:
            with self.subTest():
                self.assertEqual(is_palindrome(s), expected)

    def test_type_error(self):
        """非文字列が渡された場合は TypeError を送出すること"""
        cases = [None, 123, 3.14, ["a", "b"], {"s": "abba"}]
        for bad in cases:
            with self.subTest():
                with self.assertRaises(TypeError):
                    is_palindrome(bad)


if __name__ == "__main__":
    # コマンドラインから実行された場合にテストを走らせる
    unittest.main()
