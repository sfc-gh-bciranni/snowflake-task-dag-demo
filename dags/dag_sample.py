from datetime import timedelta

from snowflake.core import Root
from snowflake.core.task import StoredProcedureCall
from snowflake.core.task.dagv1 import DAG, DAGTask, DAGOperation
from snowflake.snowpark import Session
from snowflake.snowpark.functions import sum as sum_

from auth.snowflake_auth import authenticate
from sql.utils import load_sql

# Authenticate to Snowflake.
session = authenticate(local=True, connection_name="github_service_conn")
root = Root(session)


with DAG("my_dag", schedule=timedelta(days=1), warehouse=session.get_current_warehouse()) as dag:
  # Create a task that runs some SQL.
  dag_task1 = DAGTask(
    name="dag_sample_task_1",
    definition=load_sql(rel_path="my_dag/dag_sample_task_1.sql")
  )
  # Create a task that runs a Python function.
  dag_task2 = DAGTask(
    name='dag_sample_task_2',
    definition=load_sql(rel_path="my_dag/dag_sample_task_2.sql")
  )
  # Create another task
  dag_task3 = DAGTask(
    name='dag_sample_task_3',
    definition=load_sql(rel_path="my_dag/dag_sample_task_3.sql")
  )
# Shift right and left operators can specify task relationships.
dag_task1 >> dag_task2  # dag_task1 is a predecessor of dag_task2
schema = root.databases["github_demo"].schemas["github_schema"]
dag_op = DAGOperation(schema)
dag_op.deploy(dag, mode='orReplace')