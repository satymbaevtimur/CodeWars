package kata

import (
  "unicode"
  "strings"
)

func ToAlternatingCase(str string) string {
  var result string
  
  for _, runeValue := range str {
    if unicode.IsUpper(runeValue) {
      result += strings.ToLower(string(runeValue))
    } else if unicode.IsLower(runeValue) {
      result += strings.ToUpper(string(runeValue))
    } else {
      result += string(runeValue)
    }
  }
  
  return result
}
