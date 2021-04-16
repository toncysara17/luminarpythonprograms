#       *
#     *    *
#   *   *   *
# *   *   *   *
k = (2 * 4) - 2
for p in range(0, 4):
   for n in range(0, k):
      print(end=" ")
   k = k - 1
   for n in range(0, p + 1):
      print("*", end=' ')
   print(" ")