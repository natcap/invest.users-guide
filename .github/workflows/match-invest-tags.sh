#!/bin/bash
#
# Match tags from InVEST.
#
# Loops through all known tags in InVEST and checks to see if the
# tag is present in the UG git repo.  If it isn't present, we'll
# create it based on what's in the target rev's Makefile.

for InVEST_TAG in `git -C invest-src tag -l`
do
    if [[ `git -C . tag -l $InVEST_TAG` == $InVEST_TAG ]]
    then
        echo "Already present in user's guide:" $InVEST_TAG
    else
        git -C invest-src checkout $InVEST_TAG
        UG_REV=$(grep ^GIT_UG_REPO_REV invest-src/Makefile | awk -F ' ' '{ print $3 }')
        echo "Adding tag $InVEST_TAG for userguide rev $UG_REV (from InVEST Makefile)"
        git -C . tag $InVEST_TAG $UG_REV
    fi
done
