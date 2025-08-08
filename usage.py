from prompt_version_manager import PromptVersionManager

pvm = PromptVersionManager()

# Set a new prompt (this automatically saves the prompt with timestamp)
pvm.prompt = "Write a poem about AI."

# Optionally add the output to the last saved prompt
pvm.output = "AI is amazing, it learns and grows."
