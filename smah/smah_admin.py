from smah.database import Database, Migration
import argparse
from rich.traceback import Traceback
from rich.prompt import Prompt
import smah.console
from smah.console import std_console, err_console


class DeferredHelpFormatter(argparse.HelpFormatter):
    def __init__(self, prog):
        super().__init__(prog, max_help_position=40, width=80)

    def format_help(self):
        print(f"HELP {self._prog}")
        if '-h' in self._prog.split():
            return '..'
        return super().format_help()

def handle_prompt_component(parser, args, remaining):
    if getattr(args, 'action_parser', None) is not None:
        action_parser = args.action_parser
    else:
        action_parser = parser

    if getattr(args, 'show_help:action', False):
        show_help(parser=action_parser, args=args)
    elif getattr(args, 'show_help:prompt', False):
        show_help(parser=action_parser, args=args)
    elif getattr(args, 'show_help:base', False):
        show_help(parser=parser, args=args)
    return args

def handle_script_component(parser, args, remaining):
    if getattr(args, 'action_parser', None) is not None:
        action_parser = args.action_parser
    else:
        action_parser = parser

    if getattr(args, 'show_help:action', False):
        show_help(parser=action_parser, args=args)
    elif getattr(args, 'show_help:script', False):
        show_help(parser=action_parser, args=args)
    elif getattr(args, 'show_help:base', False):
        show_help(parser=parser, args=args)

    return args



def parse_prompt_component(parser, subparser, parent_parser):
    s_prompt = subparser.add_parser(
        name="prompt",
        help="Manage Stored Prompts.",
        formatter_class=DeferredHelpFormatter,
        exit_on_error=False,
        add_help=False
    )
    s_prompt.set_defaults(with_component="Prompt")
    s_prompt.add_argument('-h', '--help',  dest="show_help:prompt", action='store_true', help='Show this help message and exit')

    s_prompt_s = s_prompt.add_subparsers(
        title="Manage Prompt",
        description="Prompt Component Command Option",
        dest="command",
        help="Prompt Component Command To Run",
        metavar="<command>",
        required=False,
    )



    parse_edit_component(parser=s_prompt, subparser=s_prompt_s, parent_parser=parent_parser)
    parse_new_component(parser=s_prompt, subparser=s_prompt_s, parent_parser=parent_parser)
    parse_clone_component(parser=s_prompt, subparser=s_prompt_s, parent_parser=parent_parser)
    parse_browse_component(parser=s_prompt, subparser=s_prompt_s, parent_parser=parent_parser)
    parse_search_component(parser=s_prompt, subparser=s_prompt_s, parent_parser=parent_parser)
    return s_prompt


def parse_script_component(parser, subparser, parent_parser):
    s_command = subparser.add_parser(
        name="script",
        help="Manage Stored Scripts.",
        formatter_class=DeferredHelpFormatter,
        exit_on_error=False,
        add_help=False
    )
    s_command.set_defaults(with_component="Script")
    s_command.add_argument('-h', '--help',  dest="show_help:script", action='store_true', help='Show this help message and exit')

    s_command_s = s_command.add_subparsers(
        title="Manage Script",
        description="Script Component Command Option",
        dest="command" ,
        help="Script Component Command To Run",
        metavar="<command>",
        required=False
    )

    parse_edit_component(parser=s_command, subparser=s_command_s, parent_parser=parent_parser)
    parse_new_component(parser=s_command, subparser=s_command_s, parent_parser=parent_parser)
    parse_clone_component(parser=s_command, subparser=s_command_s, parent_parser=parent_parser)
    parse_browse_component(parser=s_command, subparser=s_command_s, parent_parser=parent_parser)
    parse_search_component(parser=s_command, subparser=s_command_s, parent_parser=parent_parser)
    return s_command

def parse_edit_component(parser, subparser, parent_parser):
    component = parser.get_default("with_component")
    s = subparser.add_parser(
        name="edit",
        help=f"Edit a {component}",
        formatter_class=DeferredHelpFormatter,
        exit_on_error=False,
        add_help=False,
    )
    s.add_argument('-h', '--help',  dest="show_help:action", action='store_true', help='Show this help message and exit')
    s.add_argument(
        "-name",
        type=str,
        help=f"{component} to edit ",
    )
    s.set_defaults(action_parser=s)
    return s


def parse_new_component(parser, subparser, parent_parser):
    component = parser.get_default("with_component")
    s = subparser.add_parser(
        "new",
        help=f"New {component}",
        formatter_class=DeferredHelpFormatter,
        exit_on_error=False,
        add_help=False
    )
    s.add_argument('-h', '--help',  dest="show_help:action", action='store_true', help='Show this help message and exit')
    s.add_argument(
        "-name",
        type=str,
        help=f"{component} Name",
    )
    s.set_defaults(action_parser=s)
    return s

def parse_clone_component(parser, subparser, parent_parser):
    component = parser.get_default("with_component")
    s = subparser.add_parser(
        "clone",
        help=f"Clone {component}",
        formatter_class=DeferredHelpFormatter,
        exit_on_error=False,
        add_help=False
    )
    s.add_argument('-h', '--help',  dest="show_help:action", action='store_true', help='Show this help message and exit')
    s.add_argument(
        "-name",
        type=str,
        help=f"{component} To Clone"
    )
    s.add_argument(
        "-as",
        type=str,
        help="Clone Prompt Name"
    )
    s.set_defaults(action_parser=s)
    return s

def parse_search_component(parser, subparser, parent_parser):
    component = parser.get_default("with_component")
    s = subparser.add_parser(
        name="search",
        help=f"Search {component}s",
        formatter_class=DeferredHelpFormatter,
        exit_on_error=False,
        add_help=False
    )
    s.add_argument('-h', '--help',  dest="show_help:action", action='store_true', help='Show this help message and exit')
    s.set_defaults(action_parser=s)
    return s

def parse_browse_component(parser, subparser, parent_parser):
    component = parser.get_default("with_component")
    s = subparser.add_parser(
        name="browse",
        help=f"Browse {component}s",
        formatter_class=DeferredHelpFormatter,
        exit_on_error=False,
        add_help=False
    )
    s.add_argument('-h', '--help',  dest="show_help:action", action='store_true', help='Show this help message and exit')
    s.set_defaults(action_parser=s)
    return s


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="SMAH Admin Tool",
        epilog="Use to manage your smah database, saved prompts, command line methods and more.",
        formatter_class=DeferredHelpFormatter,
        exit_on_error=False,
        add_help=False
    )
    parser.add_argument('-h', '--help',  dest="show_help:base", action='store_true', help='Show this help message and exit')

    # Create subparsers for each command (migrate, rollback, status)
    subparser = parser.add_subparsers(
        dest="component",
        title="Admin Component",
        description="SMASH Component to Administer",
        help="Admin Component to Manage.",
        metavar="<component>",
        required=False
    )

    prompt_parser = parse_prompt_component(parser=parser, subparser=subparser, parent_parser=parser)
    script_parser = parse_script_component(parser=parser, subparser=subparser, parent_parser=parser)

    try:
        args, remaining = parser.parse_known_args()

        if args.component == 'prompt':
            args = handle_prompt_component(parser=prompt_parser, args=args, remaining=remaining)
        elif args.component == 'script':
            args = handle_script_component(parser=script_parser, args=args, remaining=remaining)
        else:
            show_help(parser=parser, args=args)
            exit(1)
    except argparse.ArgumentError as e:
        err_console.print_exception(show_locals=True, max_frames=10)
        print("--------------------------\n\n")
        parser.print_help()
        print("")
        exit(1)
    except Exception as e:
        err_console.print_exception(show_locals=True, max_frames=10)
        print("--------------------------\n\n")
        parser.print_help()
        print("")
        exit(1)


def show_help(parser, args):
    parser.print_help()
    exit(0)

def main():
    args = parse_arguments()
    # database = Database(args)
    print(args)



if __name__ == "__main__":
    main()