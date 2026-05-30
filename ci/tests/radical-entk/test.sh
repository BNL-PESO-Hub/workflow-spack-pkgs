#!/bin/bash

if python3 -c "import radical.entk" 2>/dev/null; then
    entk_version="$(python3 -c "import radical.entk; print(radical.entk.__version__)")"
    if [[ -z $entk_version ]]; then
        echo "RADICAL-EnTK version unknown"
        exit 1
    fi
else
    echo "RADICAL-EnTK not installed"
    exit 1
fi

while getopts "o:" OPTION; do
    case $OPTION in
        o) OUTPUT_DIR="$OPTARG" ;;
        *) exit 1               ;;
    esac
done

base_url="https://raw.githubusercontent.com/radical-cybertools/radical.entk/v$entk_version/examples"
wget -q "$base_url/user_guide/get_started.py"
chmod +x get_started.py

radical-stack
RADICAL_REPORT_ANIME=FALSE ./get_started.py
exitcode=$?

# collect session sandboxes as tarballs
session_id=$(find . -maxdepth 1 -name "re.session*" -type d -exec basename {} "re.session" \;)
tar -czf session_client.tar.gz `find $session_id -type d -print`
session_agent_sbox="$HOME/radical.pilot.sandbox/$session_id"
if [ -d "$session_agent_sbox" ]; then
  tar -P -czf session_agent.tar.gz $session_agent_sbox
fi
mkdir -p $OUTPUT_DIR
mv session_*.tar.gz $OUTPUT_DIR/
echo "sessionID: $session_id"

test "$exitcode" = 0 && echo "Success!"
exit $exitcode
