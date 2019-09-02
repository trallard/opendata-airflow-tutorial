from airflow.operators.email_operator import EmailOperator
from datetime import timedelta, datetime

email_task = EmailOperator(
    to="some@email.com",
    task_id="email_task",
    subject="Templated Subject: start_date {{ ds }}",
    params={"content1": "random"},
    html_content="Templated Content: content1 - {{ params.content1 }}  task_key - {{ task_instance_key_str }} test_mode - {{ test_mode }} task_owner - {{ task.owner}} hostname - {{ ti.hostname }}",
    dag=dag,
)

#  run

airflow test dag_name email_task <today date>


# Adding params

# You can pass `params` dict to DAG object
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(2),
}

dag = DAG(
    dag_id='airflow_tutorial_2',
    default_args=default_args,
    schedule_interval=None,
    params={
        "param1": "value1",
        "param2": "value2"
    }
)

bash = BashOperator(
    task_id='bash',
    bash_command='echo {{ params.param1 }}', # Output: value1
    dag=dag
)


# accessing sensitive data in connections
# install pip install apache-airflow[crypto]

from airflow.hooks.base_hook import BaseHook
slack_token = BaseHook.get_connection('slack').password


#  accesing variables
from airflow.models import Variable

# Common (Not-so-nice way)
# 3 DB connections when the file is parsed
var1 = Variable.get("var1")
var2 = Variable.get("var2")
var3 = Variable.get("var3")

# Recommended Way
# Just 1 Database call
dag_config = Variable.get("dag1_config", deserialize_json=True)
dag_config["var1"]
dag_config["var2"]
dag_config["var3"]

# You can directly use it Templated arguments {{ var.json.my_var.path }}
bash_task = BashOperator(
    task_id="bash_task",
    bash_command='{{ var.json.dag1_config.var1 }} ',
    dag=dag,
)

# macros reference

# https://airflow.apache.org/macros.html

{
      'dag': task.dag,
      'ds': ds,
      'next_ds': next_ds,
      'next_ds_nodash': next_ds_nodash,
      'prev_ds': prev_ds,
      'prev_ds_nodash': prev_ds_nodash,
      'ds_nodash': ds_nodash,
      'ts': ts,
      'ts_nodash': ts_nodash,
      'ts_nodash_with_tz': ts_nodash_with_tz,
      'yesterday_ds': yesterday_ds,
      'yesterday_ds_nodash': yesterday_ds_nodash,
      'tomorrow_ds': tomorrow_ds,
      'tomorrow_ds_nodash': tomorrow_ds_nodash,
      'END_DATE': ds,
      'end_date': ds,
      'dag_run': dag_run,
      'run_id': run_id,
      'execution_date': self.execution_date,
      'prev_execution_date': prev_execution_date,
      'next_execution_date': next_execution_date,
      'latest_date': ds,
      'macros': macros,
      'params': params,
      'tables': tables,
      'task': task,
      'task_instance': self,
      'ti': self,
      'task_instance_key_str': ti_key_str,
      'conf': configuration,
      'test_mode': self.test_mode,
      'var': {
          'value': VariableAccessor(),
          'json': VariableJsonAccessor()
      },
      'inlets': task.inlets,
      'outlets': task.outlets,
}

# dynamic dags

# Using DummyOperator
a = []
for i in range(0,10):
    a.append(DummyOperator(
        task_id='Component'+str(i),
        dag=dag))
    if i != 0: 
        a[i-1] >> a[i]

# From a List
sample_list = ["val1", "val2", "val3"]
tasks_list = []
for index, value in enumerate(sample_list):
    tasks_list.append(DummyOperator(
        task_id='Component'+str(index),
        dag=dag))
    if index != 0: 
        tasks_list[index-1] >> tasks_list[index]

# database

airflow initdb # first time only

airflow upgradedb # apply missing migrations