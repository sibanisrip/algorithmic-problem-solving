class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def triangle(r, b, t):
            h = 1
            while True:
                if t == 0:
                    if r < h:
                        break
                    r -= h
                else:
                    if b < h:
                        break
                    b -= h
                h += 1
                t ^= 1
            return h - 1

        return max(triangle(red, blue, 0), triangle(red, blue, 1))
