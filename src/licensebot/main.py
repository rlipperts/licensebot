import argparse
from pathlib import Path

from anytree import AnyNode
from anytree.importer import JsonImporter

"""Load the tree and guide through it in a question process."""


def load_tree(path: Path) -> AnyNode:
    """Load the decision tree from a file."""
    importer = JsonImporter()
    with path.open() as file:
        return importer.read(file)


def decision_process(tree: AnyNode) -> AnyNode:
    next_node = tree
    while next_node.children:
        print(next_node.title)
        if hasattr(next_node, "question"):
            print(next_node.question)
        children = {child.answer: child for child in next_node.children}
        for child in children.values():
            print(f"{child.answer}: {child.title}")
        choice = input("Enter your choice: ").lower().strip()
        next_node = children[choice]
    print(f"Decision: {next_node.title}")
    return next_node


def main():
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

    # Placeholder for loading and processing the tree
    tree_root = load_tree(args.tree_file)
    decision_process(tree_root)


if __name__ == "__main__":
    main()
