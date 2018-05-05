
def tinh_bmi(chieu_cao, can_nang):
    bmi = can_nang / (chieu_cao * chieu_cao)
    return bmi

def ket_luan(bmi):
    kl = ''
    if bmi < 18.5:
        kl = 'Bạn gầy'
    elif bmi < 25:
        kl = 'Bạn bình thường'
    else:
        kl = 'Bạn thừa cân'
    return kl
