import os
import unittest

import todo.todo


class TestTodo(unittest.TestCase):

    def setUp(self):
        self.test_file = 'todo-test.json'

    def tearDown(self):
        try:
            os.remove(self.test_file)
        except OSError:
            pass

    def test_main(self):
        todo_manager = todo.todo.Todo(self.test_file)

        self.assertListEqual([], todo_manager.list())

        todo_manager.create('Find data')
        self.assertListEqual(['Find data'], todo_manager.list())

        todo_manager.create('Delete data')
        self.assertListEqual(['Find data', 'Delete data'], todo_manager.list())

        todo_manager.delete(1)
        self.assertListEqual(['Find data'], todo_manager.list())

        todo_manager.delete(0)
        self.assertListEqual([], todo_manager.list())


if __name__ == '__main__':
    unittest.main()
