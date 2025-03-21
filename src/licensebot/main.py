# ruff: noqa: D103
import argparse
from pathlib import Path

from licensebot.cmdline import run_cli
from licensebot.decision import Decision


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="LicenseBot - A tool to guide through a decision tree.",
    )
    parser.add_argument(
        "--tree-file",
        type=Path,
        default="data/tree.json",
        help="Path to the decision tree file.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose output.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    # load the tree
    decision_tree = Decision.load(args.tree_file)
    # perform the decision process
    run_cli(decision_tree)


if __name__ == "__main__":
    main()
