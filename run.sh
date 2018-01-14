#!/bin/bash

pushd `dirname $0` > /dev/null
SCRIPT_PATH=`pwd`
popd > /dev/null

BASE_PATH="$(dirname "${SCRIPT_PATH}")"

export PYTHONPATH="${SCRIPT_PATH}"
export CLISSON_ENV=Dev

python "${SCRIPT_PATH}/run.py" --app clisson --port 5000 "$@@"
