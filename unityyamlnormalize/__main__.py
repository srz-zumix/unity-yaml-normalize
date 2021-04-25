from unityparser import UnityDocument
from argparse import ArgumentParser
from . import __version__ as VERSION


class UnityYaml:

    def __init__(self):
        pass

    def normalize(self, input, output):
        doc = UnityDocument.load_yaml(input)
        for entry in doc.entries:
            entry.__dict__ = dict(sorted(entry.__dict__.items()))
        doc.dump_yaml(output)


class CLI:
    """CLI class"""

    def __init__(self):
        self.setup()

    def command_help(self, args):
        print(self.parser.parse_args([args.subcommand[0], '--help']))

    def command_run(self, args):
        unity_yaml = UnityYaml()
        unity_yaml.normalize(args.input[0], args.output)

    # command line option
    def setup(self):
        self.parser = ArgumentParser()
        self.parser.add_argument(
            '-v',
            '--version',
            action='version',
            version=u'%(prog)s version ' + VERSION
        )
        # self.parser.add_argument(
        #     '-i',
        #     '--input',
        #     required=True,
        #     help='input file path'
        # )
        self.parser.add_argument(
            '-o',
            '--output',
            help='output file path'
        )
        self.parser.add_argument(
            'input',
            metavar='INPUT',
            nargs=1,
            help='input file'
        )
        self.parser.set_defaults(handler=self.command_run)

    def parse_command_line(self, argv):
        args = self.parser.parse_args(argv)
        return args

    def print_help(self):
        self.parser.print_help()

    def execute(self):
        self.execute_with_args()

    def execute_with_args(self, args=None):
        args = self.parse_command_line(args)
        if hasattr(args, 'handler'):
            args.handler(args)
        else:
            self.print_help()


def main():
    cli = CLI()
    cli.execute()


if __name__ == '__main__':
    main()
