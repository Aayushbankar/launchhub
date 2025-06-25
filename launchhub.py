#!/usr/bin/env python3

import argparse
import sys
from utils.generator import generate_html_project
from utils.tracker import init_db, log_project, list_projects




def main():
    init_db()
    

    parser = argparse.ArgumentParser(
        description="LaunchHub – Project Scaffolding Engine"
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # init command
    init_parser = subparsers.add_parser('init', help='Initialize a new project')
    init_parser.add_argument('stack', type=str, help='Stack type (html, flask, cli)')
    
    # list command (placeholder)
    list_parser = subparsers.add_parser('list', help='List past projects (coming soon)')
    
    # help command
    help_parser = subparsers.add_parser('help', help='Show usage info')
    
    args = parser.parse_args()

    if args.command == "init":
        stack = args.stack.lower()
        if stack == "html":
            project_name = input("Enter project name: ").strip()
            output_dir = generate_html_project(project_name)  # ✅ MODIFY to return path
            if output_dir:  # only log if success
                log_project(project_name, stack, output_dir)
        else:
            print(f"[!] Stack '{stack}' is not supported in this version.")

    elif args.command == "list":
        # print("[LaunchHub] List function not implemented yet.")
        list_projects()

    elif args.command == "help" or args.command is None:
        parser.print_help()
    else:
        print("[LaunchHub] Invalid command.")
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    
    main()
