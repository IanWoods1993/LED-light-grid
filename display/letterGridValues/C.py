@staticmethod
def C(strip, pos):
  arr = []
  arr[0] = (64 * pos + 1)
  arr[1] = (64 * pos + 2)
  arr[2] = (64 * pos + 3)
  arr[3] = (64 * pos + 4)
  arr[4] = (64 * pos + 5)
  arr[5] = (64 * pos + 9)
  arr[6] = (64 * pos + 15)
  arr[7] = (64 * pos + 16)
  arr[8] = (64 * pos + 31)
  arr[9] = (64 * pos + 32)
  arr[10] = (64 * pos + 47)
  arr[11] = (64 * pos + 48)
  arr[12] = (64 * pos + 54)
  arr[13] = (64 * pos + 58)
  arr[14] = (64 * pos + 59)
  arr[15] = (64 * pos + 60)
  arr[16] = (64 * pos + 61)
  arr[17] = (64 * pos + 62)
  return arr
