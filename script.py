class Solution:
    def reverse(self, x: int) -> int:
        solution = int(str(abs(x))[::-1])
        return (-solution if x < 0 else solution) if solution.bit_length() < 32 else 0

def main():
    """Проверка алгоритма"""
    input = 153423646
    S = Solution()
    print(S.reverse(input))

if __name__ == "__main__":
    main()