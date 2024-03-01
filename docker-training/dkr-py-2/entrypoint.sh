#!/bin/bash

# Your script logic here
python app.py "$@"

# Start a long-running process (e.g., shell) to keep the container running
exec /bin/bash

