import unittest
from utils.template_engine import parse_and_replace_tokens
from pathlib import Path
import tempfile

class TestTemplateEngine(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.temp_file_path = Path(self.temp_dir.name) / "test.html"
        self.test_content = "<h1>{{project_name}}</h1>\n<p>by {{author}}</p>"

        with open(self.temp_file_path, "w") as f:
            f.write(self.test_content)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_token_replacement(self):
        context = {
            "project_name": "LaunchHub",
            "author": "Aayush"
        }

        result = parse_and_replace_tokens(self.temp_file_path, context)

        with open(self.temp_file_path, "r") as f:
            output = f.read()

        self.assertIn("LaunchHub", output)
        self.assertIn("Aayush", output)
        self.assertNotIn("{{", output)  # Make sure no placeholders remain
        self.assertEqual(result["project_name"], "LaunchHub")
        self.assertEqual(result["author"], "Aayush")

    def test_missing_token_prompt(self):
        # This test requires mocking `input()`
        # Add later with `unittest.mock`
        pass

if __name__ == "__main__":
    unittest.main()
