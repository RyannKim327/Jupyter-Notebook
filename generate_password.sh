#!/bin/bash

jupyter notebook password

new_pass=$(cat ~/.jupyter/jupyter_notebook_config.json | jq -r '.NotebookApp.password')

echo "Add a Replit Secret called NOTEBOOK_PASSWORD with the following contents:"
echo "${new_pass}"

