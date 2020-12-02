# 字符串判断统计

def judge_element(str):
    low_element = 0
    up_element = 0
    digit_element = 0
    other_element = 0
    for element in str:
        if 'a' <= element <= 'z':
            low_element += 1
            return (,)
        elif 'A' <= element <= 'Z':
            up_element += 1
        elif '0' <= element <= '9':
            digit_element += 1
        else:
            other_element += 1



str="wdxwechucuwuiy27177e3189&*((7"