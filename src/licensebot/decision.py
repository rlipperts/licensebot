from pathlib import Path

from anytree import AnyNode
from anytree.importer import JsonImporter


class Decision:
    """Guide through a decision making proccess using a tree."""

    node_history: list[AnyNode]

    def __init__(self, tree_root: AnyNode) -> None:
        self.node_history = [tree_root]

    @classmethod
    def load(cls, path: Path) -> "Decision":
        """Load the decision tree from a file."""
        importer = JsonImporter()
        with path.open() as file:
            tree_root = importer.read(file)
        return cls(tree_root)

    def state(self) -> AnyNode:
        """Return the current state of the decision making process."""
        return self.node_history[-1]

    def next(self, answer: str) -> None:
        """Move to the next state in the decision making process."""
        current_node = self.node_history[-1]
        if current_node.is_leaf:
            msg = "Cannot traverse further, already at a decision node."
            raise ValueError(msg)
        children = {child.branch: child for child in current_node.children}
        if answer not in children:
            msg = f"Invalid answer: {answer}"
            raise ValueError(msg)
        self.node_history.append(children[answer])
