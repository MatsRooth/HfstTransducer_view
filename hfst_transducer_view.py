# Author: Mats Rooth
# Codebase Generation: ChatGPT (via iterative design loop)

import hfst
from collections import defaultdict
from graphviz import Digraph

def _display_symbol(symbol):
    replacements = {
        hfst.EPSILON: "ε",
        hfst.IDENTITY: "?",
        hfst.UNKNOWN: "?",
        "@0@": "ε",
    }
    return replacements.get(symbol, symbol)


def _hfst_transducer_view(self, *, show_weights=False, format="svg"):
    """
    Return a Graphviz representation of this HfstTransducer.

    Parallel transitions between the same pair of states are combined
    into one arrow with space-separated labels.
    """
    basic = hfst.HfstBasicTransducer(self)

    graph = Digraph(format=format)
    graph.attr(rankdir="LR")

    # Default appearance for states.
    graph.attr(
        "node",
        shape="circle",
        style="filled",
        fillcolor="yellow",
    )

    # Add states.
    for state in basic.states():
        if basic.is_final_state(state):
            graph.node(
                str(state),
                shape="doublecircle",
                style="filled",
                fillcolor="yellow",
            )
        else:
            graph.node(str(state))

    # Collect parallel transitions.
    edge_labels = defaultdict(list)

    for source in basic.states():
        for transition in basic.transitions(source):
            target = transition.get_target_state()

            input_symbol = _display_symbol(
                transition.get_input_symbol()
            )
            output_symbol = _display_symbol(
                transition.get_output_symbol()
            )

            if input_symbol == output_symbol:
                rendered = input_symbol
            else:
                rendered = f"{input_symbol}:{output_symbol}"

            if show_weights:
                weight = transition.get_weight()
                if weight != 0:
                    rendered += f" / {weight:g}"

            edge_labels[(source, target)].append(
                (input_symbol, output_symbol, rendered)
        )

    # Draw one arrow for each source-target pair.
    for (source, target), entries in edge_labels.items():
        entries.sort(key=lambda x: (x[0], x[1]))
        label = " ".join(rendered for _, _, rendered in entries)

        graph.edge(
            str(source),
            str(target),
            label=label,
            )
    

    return graph


def install():
    if getattr(hfst.HfstTransducer, "view", None) is not _hfst_transducer_view:
        hfst.HfstTransducer.view = _hfst_transducer_view
