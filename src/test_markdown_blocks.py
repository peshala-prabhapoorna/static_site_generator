import unittest

from markdown_blocks import markdown_to_blocks


class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside it.

* This is a list item
* This is another list item
"""

        self.assertEqual(
            markdown_to_blocks(markdown),
            [
                "# This is a heading",
                (
                    "This is a paragraph of text. It has some **bold** and"
                    " *italic* words inside it."
                ),
                "* This is a list item\n* This is another list item",
            ],
        )

    def test_markdown_to_blocks_new_lines(self):
        markdown = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""

        self.assertEqual(
            markdown_to_blocks(markdown),
            [
                "This is **bolded** paragraph",
                (
                    "This is another paragraph with *italic* text and `code`"
                    " here\nThis is the same paragraph on a new line"
                ),
                "* This is a list\n* with items",
            ],
        )