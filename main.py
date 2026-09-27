from future import annotations

import logging
from dataclasses import dataclass
from typing import Callable

LOGGER = logging.getLogger(name)

@dataclass(frozen=True)
class AutomationTask:
  """Represents a named automation task."""

name: str
action: Callable[[], None]

def run_tasks(tasks: list[AutomationTask]) -> int:
  """Execute each task, logging progress and returning the count run."""
  if not tasks:
    LOGGER.warning("No tasks to run")
    return 0

completed = 0
for task in tasks:
  LOGGER.info("Running task: %s", task.name)
  try:
    task.action()
    completed += 1
  except Exception: # noqa: BLE001 - log and continue
  LOGGER.exception("Task failed: %s", task.name)
  return completed

def main() -> int:
  """Application entry point."""
  logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

tasks = [
  AutomationTask(name="greet", action=lambda: print("Automation running")),
]

completed = run_tasks(tasks)
print(f"Completed {completed} task(s).")
return 0

if name == "main":
  raise SystemExit(main())
  
