
### Sinter Operator For Airflow


#### Pre-requisites

To use the SinterOperator, you must have a Sinter API Key. To receive your
api key, please contact Sinter support.

#### Usage

1. Install this module into the environment where Airflow is running
2. Create a task that invokes the SinterOperator

```python
from sinter_operator import SinterOperator

SINTER_API_KEY = "..."

# Your Sinter Account ID
ACCOUNT_ID = 123

# Your Sinter Project ID
PROJECT_ID = 456

# The name of the job to run in Sinter
JOB_NAME = "Run"

t1 = SinterOperator(
    task_id='run_sinter',
    token=SINTER_API_KEY,
    account_id=ACCOUNT_ID,
    project_id=PROJECT_ID,
    job_name=JOB_NAME,
    retries=0,
    dag=dag)
```
