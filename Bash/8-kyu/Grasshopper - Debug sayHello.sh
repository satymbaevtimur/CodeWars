#!/bin/bash 

say_hello() { 
  name="$1"
  echo "Hello, $name"
}

say_hello "$1"
