#!/bin/bash

ROOT=$(pwd)
source ./src/download_proteomic.sh
cd $ROOT
source ./src/download_transcriptomic.sh
