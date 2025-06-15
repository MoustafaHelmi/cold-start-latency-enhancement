# cold-start-latency-enhancement

Enhancing Performance and Efficiency of Serverless Computing (cold-start) paper implimentation
----------------------------------------------------------

Overview
--------
This project implements a hybrid methodology for evaluating and optimizing cold start latency in serverless (Function-as-a-Service) environments. It integrates techniques from two foundational frameworks:

1. **FaaSLight** – Application-level cold start optimization via static analysis and code transformation.
2. **GeoFF** – Federated function deployment with function pre-warming and data pre-fetching for geo-distributed environments.

The result is a unified simulation and optimization framework that can be used to benchmark and enhance cold start performance across diverse workloads and configurations.

Getting Started
---------------
### Prerequisites
- Python 3.8+
- Recommended: virtualenv or conda for isolated environments

### Installation
1. Clone this repository:
git clone https://github.com/mostafa/cold-start-latency-enhancement.git
cd cold-start-latency-enhancement


2. (Optional) Create a virtual environment:
python3 -m venv venv
source venv/bin/activate

3. Install dependencies:
pip install -r requirements.txt


### Running the Simulation
To start the simulation and evaluation pipeline:
python faas_sim.py

Methodology
-----------
The simulation follows eight sequential phases:

1. **Task Generation**  
   Synthetic tasks are generated and categorized as CPU-bound, memory-bound, or I/O-bound.

2. **Task Splitting**  
   Each task is decomposed into smaller, stateless components for better parallelism and control.

3. **Cold Start Simulation**  
   Initial task executions simulate cold starts (e.g., by triggering inactive functions).

4. **Performance Measurement**  
   Metrics captured include:
   - Total Runtime
   - Compute Time
   - Cold Overhead Time

5. **Optimization Phase**  
   - *Pre-warming* (GeoFF): Keeps functions ready-to-run to avoid cold starts.
   - *Lightweight Checkpointing*: Partial state snapshots to accelerate future invocations.
   - *Code Pruning* (FaaSLight): Static analysis removes non-essential code paths, reducing the cold start footprint.

6. **Second Execution**  
   Re-executes tasks without simulating cold starts to evaluate performance post-optimization.

7. **Comparative Analysis**  
   Quantifies performance improvements using:
   - Baseline vs Optimized Total Time
   - Improvement Percentage

8. **Logging & Monitoring**  
   Detailed logs are maintained to ensure reproducibility and support debugging.

Background References
---------------------
- **FaaSLight**: A framework for mitigating cold start latency via static analysis and code reduction.  
- **GeoFF**: A geo-distributed orchestration framework leveraging pre-warming and data pre-fetching.

For detailed gap analysis and foundational background, see the paper or the `/docs/` directory (if available).

Outputs
-------
After execution, results will be available in the `/results/` folder. These include:
- Raw logs of task execution
- Performance metrics (pre- and post-optimization)
- Summary analysis report

Citation
--------
[1] FaaSLight: General Application-Level Cold-Start Latency Optimization for Function-as-a-Service in Serverless Computing.”  2023. Xuanzhe Liu, Jinfeng Wen, Zhenpeng Chen, Ding Li, Junkai Chen, Yi Liu, Haoyu Wang, Xin Jin. 

[2]	“GeoFF: Federated Serverless Workflows with Data Pre-Fetching” 2024.Valentin Carl, Trever Schirmer, Tobias Pfandzelter, David Bermbach.
