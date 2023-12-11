from go_tree_sitter.go_parser import GoParser

# TODO
class TestCaseGenerator:
    def __init__(self, llm, seed_path):
        self.MAX_INPUT_TOKEN_LEN = 512

        self.llm = llm
        self.parser = GoParser()

        self.seed_path = seed_path

        self.input_text_list = []

    def _get_input_text(self):
        while len(self.input_text_list) != 0:
            yield self.input_text_list[0]

    def generate(self):
        return self.llm.generate(self._get_input_text())
