fajr_h=4
fajr_m=18
maghreb_h=18
maghreb_m=7
total_h=(fajr_h-maghreb_h)
total_m=(fajr_m-maghreb_m)
if total_m<0 and total_h>=0:
    time5=(total_m+60)
    time6=(total_h-1)
    mid5=(time5/2)
    mid6=(time6/2)
    x6=(mid6+maghreb_h)
    y5=(mid5+maghreb_m)
    print("midnight time is:"+str(x6)+(":")+str(y5))
elif total_h<0 and total_m>=0:
    time7=(total_h+24)
    time8=(total_m)
    mid7=(time7/2)
    mid8=(time8/2)
    x7=(mid7+maghreb_h)
    y8=(mid8+maghreb_m)
else:
    time3=(total_h)
    time4=(total_m)
    mid3=(time3/2)
    mid4=(time4/2)
    x3=(mid3+maghreb_h)
    y4=(mid4+maghreb_m)
    print("midnight time is:"+str(x3)+(":")+str(y4))