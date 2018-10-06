@staticmethod
def L(strip, pos):
  arr = []
  arr[0] = (64 * pos + 0)
  arr[1] = (64 * pos + 15)
  arr[2] = (64 * pos + 16)
  arr[3] = (64 * pos + 31)
  arr[4] = (64 * pos + 32)
  arr[5] = (64 * pos + 47)
  arr[6] = (64 * pos + 48)
  arr[7] = (64 * pos + 57)
  arr[8] = (64 * pos + 58)
  arr[9] = (64 * pos + 59)
  arr[10] = (64 * pos + 60)
  arr[11] = (64 * pos + 61)
  arr[12] = (64 * pos + 62)
  arr[13] = (64 * pos + 63)
  return arr
