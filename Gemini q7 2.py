def merge_sorted(a: list[int], b: list[int]) -> list[int]:
    result = []
    i, j = 0, 0
    
    # 双指针合并，确保 O(n) 时间复杂度且不修改原列表
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
            
    # 追加剩余元素
    result.extend(a[i:])
    result.extend(b[j:])
    return result

