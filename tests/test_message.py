import unittest
import message

class MessageTest(unittest.TestCase):
    def test_normal(self):
        assert message.transName('オリーサ') == '英語：Orisa    韓国語：오리사'
    
    def test_except(self):
        assert message.transName('存在しない名前だよ') == '存在しないキャラ名だよ😱'