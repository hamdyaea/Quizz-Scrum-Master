# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
import importlib.util
from pathlib import Path
import sys
import unittest

spec = importlib.util.spec_from_file_location("scrumquiz", Path(__file__).resolve().parents[1] / "quizz-OK.py")
quiz = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = quiz
spec.loader.exec_module(quiz)

class QuizTests(unittest.TestCase):
    def test_questions(self):
        self.assertEqual(len(quiz.QUESTIONS), 5)
        for question in quiz.QUESTIONS:
            self.assertTrue(0 <= question.correct < len(question.options))
    def test_full_score(self):
        answers = {i: q.correct for i, q in enumerate(quiz.QUESTIONS)}
        self.assertEqual(quiz.score(answers), (5, 5))
    def test_empty_score(self):
        self.assertEqual(quiz.score({}), (0, 5))

if __name__ == "__main__":
    unittest.main()
