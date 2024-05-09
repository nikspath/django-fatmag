
def calculate_average(cnt,total_cnt):
    if total_cnt == 0:
        return '100.00'
    if cnt == 0:
        return '00.00'
    rate = float(cnt) / float(total_cnt)
    rate_percentage = float(rate) * 100
    return round(rate_percentage,2)


