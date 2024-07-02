# run_changed_dags.sh
#!/bin/bash

# Set PYTHONPATH to the project root
export PYTHONPATH=$(pwd)

# Get the list of changed files
changed_files=$(git diff --name-only HEAD^ HEAD)

# Loop through each changed file
for file in $changed_files; do
  # Check if the file is a Python file in the dags directory
  if [[ $file == dags/*.py ]]; then
    echo "Running changed file: $file"
    python $file
  fi
done
