#!/bin/bash

countToTwenty() {
  count=1
  
  while [ $count -le 20 ]
  do
    echo "Count: $count"
    $((count++))
  done
}

countToTwenty
