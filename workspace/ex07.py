import sys
from myutils import to_float


def main():
    args = sys.argv[1:]
    nums = [to_float(arg) for arg in args]
    nums = [n for n in nums if n is not None]

    print(f'{sum(nums) = }')


if __name__ == '__main__':
    main()
