import unittest

import todo.command


class TestCommand(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_list(self):
        args = todo.command.parse_args(['list'])
        self.assertEquals('list', args.action)

        args = todo.command.parse_args(['add', 'Find data'])
        self.assertEquals('add', args.action)
        self.assertEquals('Find data', args.task_description)

        args = todo.command.parse_args(['del', '0'])
        self.assertEquals('del', args.action)
        self.assertEquals(0, args.task_idx)


if __name__ == '__main__':
    unittest.main()
