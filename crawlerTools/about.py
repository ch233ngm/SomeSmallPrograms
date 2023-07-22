from simple import get_data
# 在simple.py的基础上扩充一些可能会用到的函数

# 是否为中文
def is_Chinese(string):
    if '\u4e00' <= string <= '\u9fff':
        return True
    return False

def print_align(string, max_len, _type='L', pad=' '):
    '''
    中英文混合字符串对齐函数
    string： 需要对齐的字符串
    max_len： 对齐长度
    _type： 对齐方式 L左、R右、其他居中
    pad： 填充字符
    '''
    str_len = len(string)       # 原始长度
    for i in str(string):
        if is_Chinese(i):       # 判断是否中文 中文长度 +1
            str_len += 1        # 
    pad_len = max_len - str_len # 计算需要填充的长度
    if _type == 'L':
        _left = 0
        _right = pad_len
    elif _type == 'R':
        _left = pad_len
        _right = 0
    else:
        _left = pad_len // 2
        _right = pad_len - _left
    return pad * _left + string + pad * _right

# 对于多页数据可以这样
def get_more_data(next_page_button, page_count):
    # 使用xpath helper获取下一页按钮，next_page_button = driver.find_element(By.PATH, "")
    for i in range(page_count-1):
        next_page_button.click()
        get_data() 
