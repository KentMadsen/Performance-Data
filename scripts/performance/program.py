import application

import sys


def main(argv):
    app = application.Application()

    app.initialise()
    app.execute()
    app.completion()

    return 0


# if main script, execute main
if __name__ == '__main__':
    main(sys.argv[1:])
