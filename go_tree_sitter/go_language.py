from tree_sitter import Language


class GoLanguage:
    PATH = "C:\\Users\\11152\\PycharmProjects\\test_platform\\resources\\build\\my-languages.so"

    language = Language(PATH, "go")

    @staticmethod
    def use_query(query, node):
        return GoLanguage.language.query(query).captures(node)
