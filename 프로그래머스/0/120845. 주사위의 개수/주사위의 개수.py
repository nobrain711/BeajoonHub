def solution(box, n):
    # 넓이 + 높이
    w=(box[0]//n)*(box[1]//n)
    h=(box[2]//n)
    return w*h