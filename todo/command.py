import os
import sys
import argparse

from todo.todo import Todo


def parse_args(args):
    parser = argparse.ArgumentParser()
    action_parser = parser.add_subparsers(title='actions', dest='action')

    action_parser.add_parser('list')

    add_action_parser = action_parser.add_parser('add')
    add_action_parser.add_argument('task_description')

    del_action_parser = action_parser.add_parser('del')
    del_action_parser.add_argument('task_idx', type=int)

    return parser.parse_args(args)


def main():
    args = parse_args(sys.argv[1:])

    data_path = os.path.expanduser('~')
    task_manager = Todo(data_path + '/.todo.json')

    if args.action == 'add':
        task_manager.create(args.task_description)
    elif args.action == 'del':
        try:
            task_manager.delete(args.task_idx)
        except IndexError:
            print('No task with that index')
    else:
        tasks = task_manager.list()
        if not tasks:
            print('To-do list is empty')
        else:
            print('To-do:')
            for idx, task in enumerate(tasks):
                print('[{}] {}'.format(idx, task))

    task_manager.save()


if __name__ == '__main__':
    main()
