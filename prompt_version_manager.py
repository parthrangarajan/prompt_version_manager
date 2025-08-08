import json
import os
from datetime import datetime

class PromptVersionManager:
    def __init__(self, json_file='prompt_version_manager.json'):
        self.json_file = json_file
        self._prompt = None
        self._output = None
        self.history = self._load_history()

    def _load_history(self):
        if os.path.isfile(self.json_file):
            with open(self.json_file, 'r', encoding='utf-8') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return []
        return []

    def _save_history(self):
        with open(self.json_file, 'w', encoding='utf-8') as f:
            json.dump(self.history, f, indent=4)

    @property
    def prompt(self):
        return self._prompt

    @prompt.setter
    def prompt(self, new_prompt):
        self._prompt = new_prompt
        record = {
            "prompt": new_prompt,
            "time": datetime.utcnow().isoformat() + "Z",
            "output": self._output
        }
        self.history.append(record)
        self._save_history()

    @property
    def output(self):
        return self._output

    @output.setter
    def output(self, new_output):
        self._output = new_output
        # Update the last saved record's output if exists
        if self.history:
            self.history[-1]["output"] = new_output
            self._save_history()
