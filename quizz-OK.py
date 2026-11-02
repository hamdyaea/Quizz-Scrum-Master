#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
"""Five-question historical Scrum quiz with Tkinter."""
from __future__ import annotations
from dataclasses import dataclass
import tkinter as tk
from tkinter import ttk

@dataclass(frozen=True)
class Question:
    prompt: str
    options: tuple[str, ...]
    correct: int

QUESTIONS = (
    Question("When is a Sprint over?", ("When all tasks are completed.", "When all Product Backlog items are done.", "When the time-box expires."), 2),
    Question("What is the main reason for the Scrum Master to be at the Daily Scrum?", ("Ensure everyone answers three questions.", "The Scrum Master need not attend but ensures the Daily Scrum takes place.", "Track Sprint Backlog changes and burndown."), 1),
    Question("The product increment must be released to production at the end of every Sprint.", ("True", "False"), 1),
    Question("When might a Sprint be cancelled?", ("When tasks cannot be finished.", "When sales has a new opportunity.", "When the Sprint Goal becomes obsolete."), 2),
    Question("Which statement best describes a Product Owner's responsibility?", ("Maximizing product value.", "Managing project commitments.", "Directing the Development Team."), 0),
)

def score(answers: dict[int, int], questions=QUESTIONS) -> tuple[int, int]:
    return sum(answers.get(i) == q.correct for i, q in enumerate(questions)), len(questions)

class Quiz(ttk.Frame):
    def __init__(self, root: tk.Tk):
        super().__init__(root, padding=20)
        self.pack(fill="both", expand=True)
        self.index = 0
        self.answers: dict[int, int] = {}
        self.choice = tk.IntVar(value=-1)
        self.question = tk.StringVar()
        self.progress = tk.StringVar()
        ttk.Label(self, textvariable=self.question, wraplength=650, font=("sans", 13)).pack(anchor="w", pady=12)
        self.buttons = ttk.Frame(self)
        self.buttons.pack(fill="x")
        ttk.Label(self, textvariable=self.progress).pack(pady=12)
        nav = ttk.Frame(self)
        nav.pack()
        ttk.Button(nav, text="Previous", command=lambda: self.navigate(-1)).pack(side="left", padx=8)
        ttk.Button(nav, text="Next", command=lambda: self.navigate(1)).pack(side="left", padx=8)
        ttk.Button(nav, text="Finish", command=self.finish).pack(side="left", padx=8)
        self.show()

    def show(self) -> None:
        question = QUESTIONS[self.index]
        self.question.set(question.prompt)
        self.progress.set(f"Question {self.index + 1} of {len(QUESTIONS)}")
        self.choice.set(self.answers.get(self.index, -1))
        for widget in self.buttons.winfo_children():
            widget.destroy()
        for index, option in enumerate(question.options):
            ttk.Radiobutton(self.buttons, text=option, variable=self.choice, value=index, command=self.remember).pack(anchor="w", pady=5)

    def remember(self) -> None:
        self.answers[self.index] = self.choice.get()

    def navigate(self, offset: int) -> None:
        self.index = max(0, min(len(QUESTIONS) - 1, self.index + offset))
        self.show()

    def finish(self) -> None:
        points, total = score(self.answers)
        self.question.set(f"Result: {points}/{total} correct")
        self.progress.set("Questions are based on historical Scrum training materials.")
        for widget in self.buttons.winfo_children():
            widget.destroy()
        ttk.Button(self.buttons, text="Restart", command=self.restart).pack(pady=12)

    def restart(self) -> None:
        self.answers.clear()
        self.index = 0
        self.show()

def main() -> None:
    root = tk.Tk()
    root.title("Scrum Master Quiz")
    root.geometry("760x400")
    Quiz(root)
    root.mainloop()

if __name__ == "__main__":
    main()
