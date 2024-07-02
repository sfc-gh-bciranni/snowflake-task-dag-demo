# run_all_dags.sh
#!/bin/bash

# Set PYTHONPATH to the project root
export PYTHONPATH=$(pwd)

# Loop through each Python file in the dags directory
for file in dags/*.py; do
  echo "Running DAG file: $file"
  python $file
done