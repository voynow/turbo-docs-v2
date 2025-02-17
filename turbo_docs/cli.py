import argparse
import asyncio

from turbo_docs import readme


def main() -> None:
    """Entry point for the turbo-docs CLI."""
    parser = argparse.ArgumentParser(description="Generate documentation for your project")
    parser.add_argument("--readme", action="store_true", help="Generate README.md file")

    args = parser.parse_args()

    if args.readme:
        asyncio.run(readme.generate())
    else:
        print("No command specified. Use --help for usage information.")


if __name__ == "__main__":
    main()
