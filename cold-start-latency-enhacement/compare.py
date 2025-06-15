"""
compare.py: Produces a side-by-side comparison of runtime before and after optimization.
"""
from faas_sim import run_simulation

def main():
    metrics = run_simulation()
    baseline = metrics["baseline_total"]
    optimized = metrics["optimized_total"]
    improvement = metrics["improvement_percent"]
    print("\n=== Runtime Comparison ===")
    print(f"{'':<20}{'Baseline':>15}{'Optimized':>15}{'Improvement':>15}")
    print(f"{'Total runtime':<20}{baseline:15.3f}{optimized:15.3f}{improvement:15.2f}%")

if __name__ == "__main__":
    main()

