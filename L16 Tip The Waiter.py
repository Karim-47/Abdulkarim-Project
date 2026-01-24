def totalbill(billamount,tip_perc):
    result = round(billamount*(1+ 0.01*tip_perc),2)
    return result

bill = 100
tip = 5
bill = totalbill(bill,tip)
print(bill)