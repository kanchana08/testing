#!/bin/bash
SESSION_NAME="my_session"
SCRIPT_PATH="hlo.py"
if screen -list | grep -q "$SESSION_NAME";then
        echo "Attaching to existing screen session: $SESSION_NAME"
        screen -r "$SESSION_NAME"
else
        echo "creating and starting a new session: $SESSION_NAME"
        screen -S "$SESSION_NAME" -d -m
        screen -S "$SESSION_NAME" -X stuff "python3 $SCRIPT_PATH$(echo -ne '\015')"
        screen -r "$SESSION_NAME"
fi
