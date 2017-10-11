
"""
C(n, r) = C(n - 1, r - 1) + C(n - 1, r)

C(0, 0) => 1

C(1, 0) => 1
C(1, 1) => 1

C(2, 0) => 1
C(2, 1) => C(1, 0) + C(1, 1) => 1 + 1 => 2
C(2, 2) => 1

C(3, 0) => 1
C(3, 1) => C(3 - 1, 1 - 1) + C(3 - 1, 1) => C(2, 0) + C(2, 1) => 1 + 2 => 3
C(3, 2) => C(3 - 1, 2 - 1) + C(3 - 1, 2) => C(2, 1) + C(2, 2) => 2 + 1 => 3
C(3, 3) => 1

# Consider pascal(0) => [1]
# Consider pascal(1) => [1] + [1] => [1,1]
# Consider pascal(2) => [1,2] + [1] => [1,2,1]
# Consider pascal(3) => [1,3,3] + [1] => [1,3,3,1]

n == 0 => [1] => (1 + x)^0 => 1
n == 1 => [1,1] => (1 + x)^1 => 1 + 1x
n == 2 => [1,2,1] => (1 + x)^2 => 1 + 2x + 1x^2
n == 3 => [1,3,3,1] => (1 + x)^3
                      => (1 + x)(1 + x)(1 + x)
                      => (1 + 2x + 1x^2)(1 + x)
                      => 1 + 2x + x^2 + x + 2x^2 + 1x^3
                      => 1 + 3x + 3x^2 + 1x^3


"""

def pascal(n):
  if n == 0:
    return [1]
  else:
    pascals_list = [1]
    pascals_sub_list = pascal(n-1)

    for r in range(n - 1):
      pascals_list.append(pascals_sub_list[r] + pascals_sub_list[r+1])

    return pascals_list + [1]

print(pascal(4))
