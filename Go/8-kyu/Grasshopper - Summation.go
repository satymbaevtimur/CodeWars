package kata

func Summation(n int) int {
  var result int
  
  for i := n; i > 0; i-- {
    result += i
  }
  
  return result
}
