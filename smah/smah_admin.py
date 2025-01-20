from smah.database import Database, Migration
import argparse
from rich.traceback import Traceback
from rich.prompt import Prompt
import smah.console
from smah.console import std_console, err_console


"""
import argparse
from smah.console import std_console, err_console

class DeferredHelpFormatter(argparse.HelpFormatter):
    def __init__(self, prog):
        super().__init__(prog, max_help_position=40, width=80)

    def format_help(self):
        if '-h' in self._prog.split():
            return ''
        return super().format_help()

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="SMAH Admin Tool",
        epilog="Use to manage your smah database, saved prompts, command line methods and more.",
        formatter_class=DeferredHelpFormatter,
        add_help=False
    )

    parser.add_argument('-h', '--help', action='store_true', help='Show this help message and exit')

    subparser = parser.add_subparsers(
        dest="component",
        title="Admin Component",
        description="SMASH Component to Administer",
        help="Admin Component to Manage.",
        metavar="<component>",
        required=True
    )

    parse_prompt_component(parser=parser, subparser=subparser)
    parse_script_component(parser=parser, subparser=subparser)

    args, remaining = parser.parse_known_args()

    if args.help:
        parser.print_help()
        exit(0)

    if args.component == 'prompt':
        handle_prompt_component(args, remaining)
    elif args.component == 'script':
        handle_script_component(args, remaining)

    return args

def handle_prompt_component(args, remaining):
    prompt_parser = argparse.ArgumentParser(add_help=False, formatter_class=DeferredHelpFormatter)
    prompt_subparser = prompt_parser.add_subparsers(dest="command", required=True)

    parse_edit_component(parser=prompt_parser, subparser=prompt_subparser)
    parse_new_component(parser=prompt_parser, subparser=prompt_subparser)
    parse_clone_component(parser=prompt_parser, subparser=prompt_subparser)
    parse_browse_component(parser=prompt_parser, subparser=prompt_subparser)
    parse_search_component(parser=prompt_parser, subparser=prompt_subparser)

    prompt_args, _ = prompt_parser.parse_known_args(remaining)

    if '-h' in remaining or '--help' in remaining:
        prompt_parser.print_help()
        exit(0)

def handle_script_component(args, remaining):
    script_parser = argparse.ArgumentParser(add_help=False, formatter_class=DeferredHelpFormatter)
    script_subparser = script_parser.add_subparsers(dest="command", required=True)

    parse_edit_component(parser=script_parser, subparser=script_subparser)
    parse_new_component(parser=script_parser, subparser=script_subparser)
    parse_clone_component(parser=script_parser, subparser=script_subparser)
    parse_browse_component(parser=script_parser, subparser=script_subparser)
    parse_search_component(parser=script_parser, subparser=script_subparser)

    script_args, _ = script_parser.parse_known_args(remaining)

    if '-h' in remaining or '--help' in remaining:
        script_parser.print_help()
        exit(0)

# ... (rest of your code remains the same)

def main():
    args = parse_arguments()
    print(args)

if __name__ == "__main__":
    main()
"""



def parse_prompt_component(parser, subparser):
    s_prompt = subparser.add_parser(
        name="prompt",
        help="Manage Stored Prompts.",
    )
    s_prompt.set_defaults(with_component="Prompt")

    s_prompt_s = s_prompt.add_subparsers(
        title="Manage Prompt",
        description="Prompt Component Command Option",
        dest="command",
        help="Prompt Component Command To Run",
        metavar="<command>",
        required=True
    )

    parse_edit_component(parser=s_prompt, subparser=s_prompt_s)
    parse_new_component(parser=s_prompt, subparser=s_prompt_s)
    parse_clone_component(parser=s_prompt, subparser=s_prompt_s)
    parse_browse_component(parser=s_prompt, subparser=s_prompt_s)
    parse_search_component(parser=s_prompt, subparser=s_prompt_s)
    return s_prompt


def parse_script_component(parser, subparser):
    s_command = subparser.add_parser(
        name="script",
        help="Manage Stored Scripts.",
    )
    s_command.set_defaults(with_component="Script")
    s_command_s = s_command.add_subparsers(
        title="Manage Script",
        description="Script Component Command Option",
        dest="command",
        help="Script Component Command To Run",
        metavar="<command>",
        required=True
    )

    parse_edit_component(parser=s_command, subparser=s_command_s)
    parse_new_component(parser=s_command, subparser=s_command_s)
    parse_clone_component(parser=s_command, subparser=s_command_s)
    parse_browse_component(parser=s_command, subparser=s_command_s)
    parse_search_component(parser=s_command, subparser=s_command_s)
    return s_command




def parse_edit_component(parser, subparser):
    component = parser.get_default("with_component")
    s_edit = subparser.add_parser(
        name="edit",
        help=f"Edit a {component}"
    )
    s_edit.add_argument(
        dest="name",
        type=str,
        help=f"{component} to edit ",
    )

def parse_new_component(parser, subparser):
    component = parser.get_default("with_component")

    s_new = subparser.add_parser(
        "new",
        help=f"New {component}"
    )
    s_new.add_argument(
        dest="name",
        type=str,
        help=f"{component} Name"
    )

def parse_clone_component(parser, subparser):
    component = parser.get_default("with_component")
    s_clone = subparser.add_parser(
        "clone",
        help=f"Clone {component}"
    )
    s_clone.add_argument(
        dest="name",
        type=str,
        help=f"{component} To Clone"
    )
    s_clone.add_argument(
        dest="as",
        type=str,
        help="Clone Prompt Name"
    )

def parse_search_component(parser, subparser):
    component = parser.get_default("with_component")
    subparser.add_parser("search",help=f"Search {component}s")

def parse_browse_component(parser, subparser):
    component = parser.get_default("with_component")
    subparser.add_parser("browse",help=f"Browse {component}s")



def parse_arguments():

    closing_options = argparse.ArgumentParser(add_help=False)
    closing_options.add_argument("--database", type=str, help="Path to the database file")

    parser = argparse.ArgumentParser(
        description="SMAH Admin Tool",
        epilog="Use to mange your smah database, saved prompts, command line methods and more.",
        exit_on_error=False,
        add_help=False
    )
    parser.add_argument('-h', '--help', action='store_true', help='Show this help message and exit')

    # Create subparsers for each command (migrate, rollback, status)
    subparser = parser.add_subparsers(
        dest="component",
        title="Admin Component",
        description="SMASH Component to Administer",
        help="Admin Component to Manage.",
        metavar="<component>",
        required=True
    )

    parse_prompt_component(parser=parser, subparser=subparser)
    parse_script_component(parser=parser, subparser=subparser)


    #parser.add_argument("-h", action="help")
    #parser.add_argument("--database", type=str, help="Path to the database file")
    #t = subparser.add_parser(name="h")
    #t.add_argument('--database', nargs='?', type=argparse.FileType('rw'))
    #tt = t.add_subparsers(name="-h", dest="command")
    #tt.add_parser(a)
    #tt.add_parser(b)
    #t.add_subparsers(name="-h")



    try:
        args,r = parser.parse_known_args()
        print(r)

        if args.component is None:
            raise Exception("component Required")
        return args
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

def main():
    args = parse_arguments()
    # database = Database(args)
    print(args)



if __name__ == "__main__":
    main()