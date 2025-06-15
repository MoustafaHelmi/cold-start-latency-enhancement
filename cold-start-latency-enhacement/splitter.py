"""
splitter.py: Splits a large list of test cases into smaller files, preserving all scenarios.
"""
import json
import os
from testcases import TEST_CASES
from logger_config import logger

def split_tasks(tasks, chunk_size=20, output_dir="task_chunks"):
    """
    Split the list of tasks into multiple JSON files with a given chunk size.
    """
    os.makedirs(output_dir, exist_ok=True)
    chunks = []
    total = len(tasks)
    for i in range(0, total, chunk_size):
        chunk = tasks[i:i + chunk_size]
        filename = os.path.join(output_dir, f"tasks_chunk_{i // chunk_size}.json")
        with open(filename, "w") as f:
            json.dump(chunk, f, indent=2)
        chunks.append(filename)
        logger.info(f"Saved {len(chunk)} tasks to {filename}")
    return chunks

if __name__ == "__main__":
    # Example usage: split the TEST_CASES into chunks and print file list
    chunk_files = split_tasks(TEST_CASES)
    print(f"Created {len(chunk_files)} chunk files.")

