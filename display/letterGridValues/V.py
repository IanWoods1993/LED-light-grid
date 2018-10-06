@staticmethod
def V(strip, pos):
  arr = []
  arr[0] = (64 * pos + 0)
  arr[1] = (64 * pos + 6)
  arr[2] = (64 * pos + 9)
  arr[3] = (64 * pos + 15)
  arr[4] = (64 * pos + 16)
  arr[5] = (64 * pos + 22)
  arr[6] = (64 * pos + 25)
  arr[7] = (64 * pos + 31)
  arr[8] = (64 * pos + 32)
  arr[9] = (64 * pos + 38)
  arr[10] = (64 * pos + 42)
  arr[11] = (64 * pos + 46)
  arr[12] = (64 * pos + 50)
  arr[13] = (64 * pos + 52)
  arr[14] = (64 * pos + 60)
  return arr
