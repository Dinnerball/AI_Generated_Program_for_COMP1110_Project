def second_largest(numbers: list[int]) -> int | None:
    # 使用 set 去重获取独特值，不影响原列表
    unique_numbers = list(set(numbers))
    if len(unique_numbers) < 2:
        return None
    # 排序后提取倒数第二个元素
    unique_numbers.sort()
    return unique_numbers[-2]

