package kata

func GetGrade(a,b,c int) rune {
  if average := (a + b + c) / 3; average >= 90 && average <= 100 {
    return 'A'
  } else if average < 90 && average >= 80 {
    return 'B'
  } else if average < 80 && average >= 70 {
    return 'C'
  } else if average < 70 && average >= 60 {
    return 'D'
  } else {
    return 'F'
  }
}
