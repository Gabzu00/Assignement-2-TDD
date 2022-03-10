import unittest
import unittest.mock
from PIG import Main

class TestMainClass(unittest.TestCase):
    
    @unittest.mock.patch('builtins.print')
    def test_Main(self, mock_print):

        test = Main.startMain.main()
        res = Main.startMain.main()

        args, _ = mock_print.call_args
        print(args)

        self.assertTrue(res, test)