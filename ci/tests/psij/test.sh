#!/bin/bash

# https://github.com/ExaWorks/SDK/blob/master/docs/source/tutorials/psij.ipynb

BASE_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]:-$0}"; )" &> /dev/null && pwd 2> /dev/null; )"

while getopts "o:" OPTION; do
    case $OPTION in
        o) OUTPUT_DIR="$OPTARG" ;;
        *) exit 1               ;;
    esac
done

mkdir -p $OUTPUT_DIR; cd $OUTPUT_DIR

# Prepare MPI Hello World example
cat <<EOF >hello.c
#include <stdio.h>
#include <mpi.h>

void main(int argc, char **argv) {
    int rank;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    
    printf("Hello from rank %d\n", rank);
    
    MPI_Finalize();
}
EOF

mpicc hello.c -o hello

python3 $BASE_DIR/test.py > $OUTPUT_DIR/psij_output.log 2>&1
exitcode=$?

test "$exitcode" = 0 && echo "Success!"
exit $exitcode
