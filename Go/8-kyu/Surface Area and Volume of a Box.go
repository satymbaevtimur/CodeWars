package kata

func GetSize(w,h,d int) [2]int {
  volume := w * h * d
  area := 2 * (w * h + h * d + d * w)
  
  return [2]int{area, volume}
}
