#!/bin/bash

set -e
set -x

source "$PWD"/script/hash_setup.sh

$CMD_BASE -f "$FILE_INPUT"
$CMD_BASE -a "$ASCII_INPUT"
$CMD_BASE -x "$HEX_INPUT"

function hash_runner {
    for hash in "${HASHES[@]}"
    do
        echo "Using hash $hash"

        tail "$FILE_INPUT" | $CMD_BASE --hash-type "$hash"
        $CMD_BASE -f "$FILE_INPUT" --hash-type "$hash"
        $CMD_BASE -a "$ASCII_INPUT" --hash-type "$hash"
        $CMD_BASE -x "$HEX_INPUT" --hash-type "$hash"

        # tail "$FILE_INPUT" | $CMD_BASE -r --hash-type "$hash"
        $CMD_BASE -rf "$FILE_INPUT" --hash-type "$hash"
        $CMD_BASE -ra "$ASCII_INPUT" --hash-type "$hash"
        $CMD_BASE -rx "$HEX_INPUT" --hash-type "$hash"

        if [[ -v "FILE_VERIFY[$hash]" ]] ; then
            $CMD_BASE -f "$FILE_INPUT" --hash-type "$hash" --verify "${FILE_VERIFY[$hash]}"
            tail "$FILE_INPUT" | $CMD_BASE --hash-type "$hash" --verify "${FILE_VERIFY[$hash]}"
        fi

        if [[ -v "ASCII_VERIFY[$hash]" ]] ; then
            $CMD_BASE -a "$ASCII_INPUT" --hash-type "$hash" --verify "${ASCII_VERIFY[$hash]}"
        fi
    done
}

hash_runner
