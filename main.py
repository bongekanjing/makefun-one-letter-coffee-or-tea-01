"""One Letter: Coffee or Tea — entry program.

Writes exactly one letter to /output/entry.txt: A for coffee, B for tea.
"""

import os

# A = coffee. The vivid pick: bitter, steaming, the morning jolt — and the
# funnier one (nobody warns you not to talk to them before their tea).
# The letter A is first, top grade, and stands for "awake".
ENTRY_LETTER = "A"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY_LETTER)
