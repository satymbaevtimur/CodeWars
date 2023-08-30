package kata

func century(year int) int {
  century := year / 100
  
  if year % 100 != 0 {
    century++
  }
  
  return century
}
