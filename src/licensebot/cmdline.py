# ruff: noqa: T201
from colored import fg, style, stylize

from licensebot.decision import Decision

h1: str = f"{style('bold')}{style('underline')}"
h2: str = f"{style('bold')}"
body: str = f"{fg('dark_gray')}"


def run_cli(decision_tree: Decision) -> None:
    """Run the CLI for the decision tree."""
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
