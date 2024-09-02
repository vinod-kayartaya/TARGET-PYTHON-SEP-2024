if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7,8,9,10]

    even_nums = []
    for a_num in nums:
        if a_num % 2 == 0:
            even_nums.append(a_num)

    odd_nums = [x for x in nums if x % 2 == 1]
    double_of_nums = [2*x for x in nums]

    print(f'{even_nums = }')
    print(f'{odd_nums = }')
    print(f'{double_of_nums = }')
