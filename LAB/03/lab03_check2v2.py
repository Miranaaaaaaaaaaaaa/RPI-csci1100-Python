def skew(time1,time2,time3,time4,time5):
    avg = (time1+time2+time3+time4+time5)/5
    var = (time1-avg)**2 + (time2-avg)**2 + (time3-avg)**2 + (time4-avg)**2 + (time5-avg)**2
    var /= 5
    skew = (time1-avg)**3 + (time2-avg)**3 + (time3-avg)**3 + (time4-avg)**3 + (time5-avg)**3
    skew /= 5
    skew = skew/var**3**0.5    
    return skew

def sentence(name,time1,time2,time3,time4,time5):
    mini = min(time1,time2,time3,time4,time5)
    maxi = max(time1,time2,time3,time4,time5)
    avgi = ((time1+time2+time3+time4+time5)-(mini+maxi))/3
    print('{0} stats-- min: {1}, max: {2}, avg: {3}'.format(name, mini,maxi,round(avgi,1)))

    
name_1 = "Stan"
## The following are Stan's 5 latest running times for 3 miles

time1_1 = 34
time2_1 = 34
time3_1 = 35
time4_1 = 31
time5_1 = 29

name_2 = "Kyle"
## The following are Kyle's 5 latest running times for 3 miles

time1_2 = 30
time2_2 = 31
time3_2 = 29
time4_2 = 29
time5_2 = 28

name_3 = "Cartman"
## The following are Cartman's 5 latest running times for 3 miles
time1_3 = 36
time2_3 = 31
time3_3 = 32
time4_3 = 33
time5_3 = 33

name_4 = "Kenny"
## The following are Kenny's 5 latest running times for 3 miles
time1_4 = 33
time2_4 = 32
time3_4 = 34
time4_4 = 31
time5_4 = 35

name_5 = "Bebe"
## The following are Bebe's 5 latest running times for 3 miles
time1_5 = 27
time2_5 = 29
time3_5 = 29
time4_5 = 28
time5_5 = 30

skew_1 = skew(34, 34, 35, 31, 29)
skew_2 = skew(30, 31, 29, 29, 28)
skew_3 = skew(36, 31, 32, 33, 33)
skew_4 = skew(33, 32, 34, 31, 35)
skew_5 = skew(27, 29, 29, 28, 30)

name1 = name_1 + "'s"
name2 = name_2 + "'s"
name3 = name_3 + "'s"
name4 = name_4 + "'s"
name5 = name_5 + "'s"

print ("{0}'s running times have a skew of {1:.2f}".format(name_1,skew_1))
print ("{0}'s running times have a skew of {1:.2f}".format(name_2,skew_2))
print ("{0}'s running times have a skew of {1:.2f}".format(name_3,skew_3))
print ("{0}'s running times have a skew of {1:.2f}".format(name_4,skew_4))
print ("{0}'s running times have a skew of {1:.2f}".format(name_5,skew_5))

print('')

sentence(name1,34, 34, 35, 31, 29)
sentence(name2,30, 31, 29, 29, 28)
sentence(name3,36, 31, 32, 33, 33)
sentence(name4,33, 32, 34, 31, 35)
sentence(name5,27, 29, 29, 28, 30)

'''
print('{0} stats-- min: {1}, max: {2}, avg: {3:.1f}'.format(name1, mini(34, 34, 35, 31, 29),maxi(34, 34, 35, 31, 29),avgi(34, 34, 35, 31, 29)))
print('{0} stats-- min: {1}, max: {2}, avg: {3:.1f}'.format(name2, mini(30, 31, 29, 29, 28),maxi(30, 31, 29, 29, 28),avgi(30, 31, 29, 29, 28)))
print('{0} stats-- min: {1}, max: {2}, avg: {3:.1f}'.format(name3, mini(36, 31, 32, 33, 33),maxi(36, 31, 32, 33, 33),avgi(36, 31, 32, 33, 33)))
print('{0} stats-- min: {1}, max: {2}, avg: {3:.1f}'.format(name4, mini(33, 32, 34, 31, 35),maxi(33, 32, 34, 31, 35),avgi(33, 32, 34, 31, 35)))
print('{0} stats-- min: {1}, max: {2}, avg: {3:.1f}'.format(name5, mini(33, 32, 34, 31, 35),maxi(27, 29, 29, 28, 30),avgi(27, 29, 29, 28, 30)))

'''
'''
# Process results for the first person
avg = (time1_1+time2_1+time3_1+time4_1+time5_1)/5
var = (time1_1-avg)**2 + (time2_1-avg)**2 + (time3_1-avg)**2 + (time4_1-avg)**2 + (time5_1-avg)**2
var /= 5
skew = (time1_1-avg)**3 + (time2_1-avg)**3 + (time3_1-avg)**3 + (time4_1-avg)**3 + (time5_1-avg)**3
skew /= 5
skew = skew/var**3**0.5
print ("{0}'s running times have a skew of {1:.2f}".format(name_1,skew))


## Process for the second person
avg = (time1_2+time2_2+time3_2+time4_2+time5_2)/5
var = (time1_2-avg)**2 + (time2_2-avg)**2 + (time3_2-avg)**2 + (time4_2-avg)**2 + (time5_2-avg)**2
var /= 5
skew = (time1_2-avg)**3 + (time2_2-avg)**3 + (time3_2-avg)**3 + (time4_2-avg)**3 + (time5_2-avg)**3
skew /= 5
skew = skew/var**3**0.5
print ("{0}'s running times have a skew of {1:.2f}".format(name_2,skew))

## Process for the third person
avg = (time1_3+time2_3+time3_3+time4_3+time5_3)/5
var = (time1_3-avg)**2 + (time2_3-avg)**2 + (time3_3-avg)**2 + (time4_3-avg)**2 + (time5_3-avg)**2
var /= 5
skew = (time1_3-avg)**3 + (time2_3-avg)**3 + (time3_3-avg)**3 + (time4_3-avg)**3 + (time5_3-avg)**3
skew /= 5
skew = skew/var**3**0.5
print ("{0}'s running times have a skew of {1:.2f}".format(name_3,skew))


## Process for the fourth person
avg = (time1_4+time2_4+time3_4+time4_4+time5_4)/5
var = (time1_4-avg)**2 + (time2_4-avg)**2 + (time3_4-avg)**2 + (time4_4-avg)**2 + (time5_4-avg)**2
var /= 5
skew = (time1_4-avg)**3 + (time2_4-avg)**3 + (time3_4-avg)**3 + (time4_4-avg)**3 + (time5_4-avg)**3
skew /= 5
skew = skew/var**3**0.5
print ("{0}'s running times have a skew of {1:.2f}".format(name_4,skew))


## Process for the fifth person
avg = (time1_5+time2_5+time3_5+time4_5+time5_5)/5
var = (time1_5-avg)**2 + (time2_5-avg)**2 + (time3_5-avg)**2 + (time4_5-avg)**2 + (time5_5-avg)**2
var /= 5
skew = (time1_5-avg)**3 + (time2_5-avg)**3 + (time3_5-avg)**3 + (time4_5-avg)**3 + (time5_5-avg)**3
skew /= 5
skew = skew/var**3**0.5
print ("{0}'s running times have a skew of {1:.2f}".format(name_5,skew))
'''
