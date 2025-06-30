import argparse

def main():
    parser = argparse.ArgumentParser(description="{{project_name}} CLI tool")
    parser.add_argument('--version', action='store_true', help='Show version')

    args = parser.parse_args()

    if args.version:
        print("{{project_name}} - v0.1.0")
    else:
        print("Welcome to {{project_name}} CLI!")

if __name__ == "__main__":
    main()
