package kata

import (
  "strings"
)

func FakeBin(x string) string {
  var result strings.Builder
  
  for _, runeValue := range x {
    digit := int(runeValue - '0')
    
    if digit < 5 {
      result.WriteString("0")
    } else {
      result.WriteString("1")
    }
  }
  
  return result.String()
}
