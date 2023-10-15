#!/bin/bash

removeChar() {
  name="$1"
  name="${name#?}"
  name="${name%?}"
  
  echo "$name"
}

removeChar $1
