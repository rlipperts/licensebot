# ruff: noqa: T201, D103
import argparse
from pathlib import Path

from colored import fg, style, stylize

from licensebot.decision import Decision

"""Load the tree and guide through it in a question process."""

h1: str = f"{style('bold')}{style('underline')}"
h2: str = f"{style('bold')}"
body: str = f"{fg('dark_gray')}"


def main() -> None:
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
    args = parser.parse_args()

    if args.verbose:
        print(f"Loading tree from {args.tree_file}...")

    # load the tree
    decision_tree = Decision.load(args.tree_file)
    # perform the decision process
    state = decision_tree.state()
    while not state.is_leaf:
        print(stylize(state.title, h1))
        print(stylize(state.body, body))
        children = {child.branch: child for child in state.children}
        print(stylize("\nOptions:", h2))
        for branch, child in children.items():
            if child.is_leaf:
                print(f"\t{branch} ---> {stylize(child.title, fg('green'))}")
            else:
                print(f"\t{branch} ---> next question: {child.title}")
        answer = input("\nYour answer: ")
        print("\n\n")
        decision_tree.next(answer)
        state = decision_tree.state()
    print(stylize(f"Your License: {state.title}", h1))
    print(stylize(state.body, body))


if __name__ == "__main__":
    main()
