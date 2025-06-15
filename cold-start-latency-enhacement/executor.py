"""
executor.py: Executes test cases and measures runtime, isolating cold start latency.
"""
import time
import os
from logger_config import logger

# Define simulated cold start overhead time (seconds)
COLD_START_OVERHEAD = 1.0  # e.g., 1 second overhead for code loading at cold start

def run_tasks(tasks, simulate_cold=True):
    """
    Execute a list of tasks and measure runtimes.
    If simulate_cold is True, simulates cold start overhead on first invocation of each function.
    Returns a dict of metrics including total time, compute time, and cold start overhead.
    """
    seen_funcs = set()
    total_compute_time = 0.0
    cold_overhead_time = 0.0

    start_total = time.perf_counter()
    for task in tasks:
        func_id = task.get("func")
        task_type = task.get("type")
        param = task.get("param")
        task_id = task.get("id", -1)

        logger.debug(f"Executing task ID {task_id}: func={func_id}, type={task_type}")

        # Simulate cold start overhead for the first invocation of each function
        if simulate_cold and func_id not in seen_funcs:
            logger.debug(f"Cold start for function {func_id} (task {task_id})")
            overhead_start = time.perf_counter()
            time.sleep(COLD_START_OVERHEAD)  # simulate code loading time
            overhead_end = time.perf_counter()
            overhead_duration = overhead_end - overhead_start
            cold_overhead_time += overhead_duration
            seen_funcs.add(func_id)
            logger.debug(f"Cold start overhead for {func_id}: {overhead_duration:.3f}s")

        # Execute the actual task workload
        task_start = time.perf_counter()
        if task_type == "cpu":
            # CPU-bound task: perform many operations
            result = sum(i * i for i in range(param))
        elif task_type == "memory":
            # Memory-bound task: allocate and sum a large list
            data = [i for i in range(param)]
            result = sum(data)
        elif task_type == "io":
            # IO-bound task: write and read a file of given size (in MB)
            filename = f"temp_io_task_{task_id}.bin"
            data = b'0' * (param * 1024 * 1024)
            with open(filename, "wb") as f:
                f.write(data)
            with open(filename, "rb") as f:
                _ = f.read()
            # Clean up temporary file
            try:
                os.remove(filename)
            except OSError:
                logger.warning(f"Could not remove temp file {filename}")
            result = None
        else:
            logger.warning(f"Unknown task type: {task_type}")
            result = None
        task_end = time.perf_counter()

        task_time = task_end - task_start
        total_compute_time += task_time
        logger.debug(f"Task {task_id} completed in {task_time:.3f}s")

    end_total = time.perf_counter()
    total_time = end_total - start_total

    metrics = {
        "total_time": total_time,
        "compute_time": total_compute_time,
        "cold_overhead": cold_overhead_time
    }
    logger.info(f"Run completed: total_time={total_time:.3f}s, compute_time={total_compute_time:.3f}s, cold_overhead={cold_overhead_time:.3f}s")
    return metrics

