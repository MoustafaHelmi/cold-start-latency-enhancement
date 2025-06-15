"""
faas_sim.py: Simulates the execution of test cases in a FaaSLight-style environment.
Uses predictive pre-warming and checkpointing optimizations and compares against baseline.
"""
import json
from splitter import split_tasks
from executor import run_tasks
from optimizations import predictive_pre_warm, lightweight_checkpoint
from testcases import TEST_CASES
from logger_config import logger

def run_simulation(chunk_size=20):
    """
    Splits test cases into chunks, then runs baseline and optimized simulations.
    """
    # Split tasks into chunk files
    logger.info("Splitting tasks into smaller chunks...")
    chunk_files = split_tasks(TEST_CASES, chunk_size=chunk_size)
    chunk_files.sort()
    total_baseline_time = 0.0
    total_optimized_time = 0.0

    for chunk_file in chunk_files:
        logger.info(f"Processing chunk file: {chunk_file}")
        # Load chunk of tasks
        with open(chunk_file, 'r') as f:
            tasks = json.load(f)

        # Baseline run (with simulated cold starts)
        logger.info("Starting baseline run (cold starts simulated)...")
        baseline_metrics = run_tasks(tasks, simulate_cold=True)
        total_baseline_time += baseline_metrics["total_time"]

        # Apply optimizations: predictive pre-warming and checkpointing
        logger.info("Applying predictive pre-warming...")
        predictive_pre_warm(tasks)
        logger.info("Applying lightweight checkpointing...")
        lightweight_checkpoint(tasks)

        # Optimized run (cold starts avoided)
        logger.info("Starting optimized run (post-warming)...")
        optimized_metrics = run_tasks(tasks, simulate_cold=False)
        total_optimized_time += optimized_metrics["total_time"]

        logger.info(f"Chunk {chunk_file} - Baseline time: {baseline_metrics['total_time']:.3f}s, "
                    f"Optimized time: {optimized_metrics['total_time']:.3f}s")

    logger.info("Simulation complete.")
    logger.info(f"Total baseline runtime: {total_baseline_time:.3f}s")
    logger.info(f"Total optimized runtime: {total_optimized_time:.3f}s")
    improvement = (total_baseline_time - total_optimized_time) / total_baseline_time * 100 if total_baseline_time > 0 else 0
    logger.info(f"Total runtime improvement: {improvement:.2f}%")
    return {
        "baseline_total": total_baseline_time,
        "optimized_total": total_optimized_time,
        "improvement_percent": improvement
    }

def main():
    """
    Main entry point to run the FaaS simulation and print a summary report.
    """
    logger.info("Starting main simulation...")
    metrics = run_simulation()
    baseline = metrics["baseline_total"]
    optimized = metrics["optimized_total"]
    improvement = metrics["improvement_percent"]

    print("\n=== Runtime Summary ===")
    print(f"{'':<20}{'Baseline':>15}{'Optimized':>15}{'Improvement':>15}")
    print(f"{'Total runtime':<20}{baseline:15.3f}{optimized:15.3f}{improvement:15.2f}%")

if __name__ == "__main__":
    main()

