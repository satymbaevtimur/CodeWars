package kata

func SetAlarm(employed, vacation bool) bool {
  if employed && !vacation {
    return true
  } else {
    return false
  }
}
