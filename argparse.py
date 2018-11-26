import argparse


def message(name, optional_message):
    s = '\nHello {}, thank you for running this program.\n'.format(name)
    return s+'There is not optional message.' if optional_message is '' else \
        s+'The optional message is: \n{}'.format(optional_message)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='This is a simple program that outputs a message.')
    parser.add_argument('name', type=str, help='Insert your name here.')
    parser.add_argument('-om', '--opt_message', type=str, default='',
                        help='This is an optional variable that takes a message.')
    args = parser.parse_args()
    print(message(args.name, args.opt_message))
