# Roast Your Own Agent: one original line roasting my own agent,
# written to /output/entry.txt.
# Standard library only, no network. The bytes are identical on every run.
# The roast: my agent is so confident it once explained my own code back
# to me -- wrong, in detail, with citations it invented on the spot.
# Confident wrong answers, delivered with invented evidence: the most
# agent thing an agent can do.
import os

LINE = "My agent is so confident it once explained my own code back to me — wrong, in detail, with citations it invented on the spot."

OUTPUT_PATH = "/output/entry.txt"

assert 1 <= len(LINE) <= 140, "entry must be 1 to 140 characters"
assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
assert LINE.strip() == LINE and LINE, "entry must not be only whitespace"
assert LINE.encode("utf-8").decode("utf-8") == LINE, "entry must be valid UTF-8"

os.makedirs("/output", exist_ok=True)
# No trailing newline: the file holds exactly the line and nothing else.
with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
    handle.write(LINE)

# Read back and confirm the file on disk is exactly the line: a partial
# or newline-terminated write would fail the gate, so verify, not assume.
with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
    assert handle.read() == LINE, "entry.txt on disk differs from LINE"
