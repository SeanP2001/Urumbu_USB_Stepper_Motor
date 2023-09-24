#!/bin/bash
# Load inventory and use it to look for missing symbols
# Author: Krisjanis Rijnieks
# Created: 2022-04-27

# The location of the library can change. Supply it from outside.
if [[ ! ${1} ]]; then
  echo "Please specify KiCad library file and optional whitelist file."
  echo "Usage: ./inventory.sh ../fab.kicad_sym ./whitelist.txt"
  exit 1
fi

# Check if file exists
if [[ ! -f ${1} ]]; then
  echo "Library file does not exist."
  echo "Make sure the path to the library file is correct."
  exit 1
fi

if [[ ${2} && ! -f ${2} ]]; then
  echo "Provided whitelist file node not exist."
  echo "Make sure the path to the whitelist file is correct."
  exit 1
fi

LIBRARY_FILE=${1}
WHITELIST_FILE=${2}
INVENTORY_URL="http://inventory.fabcloud.io/data/inv.json"
SOURCE="Digi-Key"

# Whitelist. All the tools and materials from Digi-Key go here.
readarray -t WHITELIST < ${WHITELIST_FILE}
WHITELIST=${WHITELIST[@]}

# Colored output
RED='\033[0;31m'
GREEN='\033[0;32m'
RESET='\033[0m'

# Error counting
ERRORS=0

echo "This script looks for parts that are not in the KiCad fab library yet. In order to add parts, make sure that the manufacturer number of the part is added to the keywords section of the library symbol."

# Read keywords from all KiCad fab library symbols
KEYWORD_LINES=$(cat ${LIBRARY_FILE} | grep --extended-regexp --only-matching -U 'property "ki_keywords" "([^"]*)"')
KEYWORDS=""
IFS=$'\n'
for LINE in ${KEYWORD_LINES}; do
   WORDS=$(echo ${LINE} | sed -En 's/property "ki_keywords" "([^"]*)"/\1/p')
   KEYWORDS="${KEYWORDS} ${WORDS}"
done

# Extract items matching source
# JQ is used here.
# RT*M: https://stedolan.github.io/jq/manual/
# Play: https://jqplay.org/
echo "Loading fab inventory..."
ITEMS=$(curl -s ${INVENTORY_URL} | jq -r '.topics[] | .sources."Digi-Key".categories[]? | .[] | .item')
echo "Looking for matches in the library..."
for ITEM in ${ITEMS}; do
  # TODO: Look for item in whitelist
  if [[ ${WHITELIST} == *"${ITEM}"* ]]; then
    echo "${ITEM} found in whitelist"
    continue
  fi

  # Look for item in KiCad symbol library
  if [[ ${KEYWORDS} == *"${ITEM}"* ]]; then
    echo -e "${GREEN}${ITEM} found${RESET}"
  else
    echo -e "${RED}${ITEM} not found${RESET}"
    ERRORS=$(expr $ERRORS + 1)
  fi
done

if [ ${ERRORS} -eq 0 ]; then
  echo -e "${GREEN}SUCCESS: All parts can be found!${RESET}"
  exit 0
else
  echo -e "${RED}ERROR(${ERRORS}): Some parts could not be found.${RESET}"
  exit 1
fi
