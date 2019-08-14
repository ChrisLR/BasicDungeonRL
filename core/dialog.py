class DialogTree(object):
    """
    This object holds DialogNodes each of them possibly branching to other nodes
    """
    def __init__(self, dialog_id, root_nodes):
        self.dialog_id = dialog_id
        self.root_nodes = root_nodes
        self._nodes = {}
        self._prepare_options(self.root_nodes)

    def get_options(self, talker, progress_id=None):
        if progress_id is None:
            return self.root_nodes

        current_node = self._nodes.get(progress_id)
        child_nodes = [
            child for child in current_node.children
            if child.requirements is None
            or all(requirement(talker) for requirement in child.requirements)]

        return child_nodes

    def select(self, node):
        if node.on_select:
            node.on_select()
        return node.key

    def _prepare_options(self, nodes, path=None):
        if nodes is None:
            return

        for i, node in enumerate(nodes):
            key = "%s_%s" % (path, i) if path else str(i)
            self._nodes[key] = node
            node.key = key
            self._prepare_options(node.children, key)


class DialogNode(object):
    def __init__(self, ask_text, reply_text, children=None, requirements=None, on_select=None):
        self.ask_text = ask_text
        self.reply_text = reply_text
        self.children = children
        self.requirements = requirements
        self.on_select = on_select
        self.key = None
