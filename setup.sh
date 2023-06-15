#!/bin/bash

if conda env list | grep "conlab_screening";
then
  echo "conlab_screening already exists ... "
  echo "updating requirements only"
  conda activate conlab_screening
  conda env update -f requirements/environment.yml --prune
else
  echo "creating conlab_screening environment ..."
  conda env create -f requirements/environment.yml
  conda activate conlab_screening
fi

