import re

def solution(myStr):
    result = re.split('[abc]', myStr)
    result = [s for s in result if s] 
    return result if result else ["EMPTY"]