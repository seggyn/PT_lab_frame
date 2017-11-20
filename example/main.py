from utility.settings import *

# GETTING SIZE OF SET
n = 20
#n = int(input('ENTER SET SIZE\n'))
# CREATE SIMPLE CHOICE
sc = SimpleChoice(data.input, n)
# OUTPUT`S GENERATION
tpl.insert({
    'GeneralSet': data.input,
    'SimpleChoice': sc.choice,
    'SimpleVarRow': sc.table,

    'sAvarage': sc.avarage,
    'sDispersion': sc.dispersion,
    'sSDeviation': sc.standardDeviation,
    'sMode': sc.mode,
    'sMedian': sc.median
})


# WRITE GRAPHICS CODE THERE OR ENDURE IT TO CLASS AND CALL

print(plt.hist(sc.setX, bins=2, weights=sc.setN, histtype='step'))
plt.title("Графік вибірки")
plt.xlabel("Проста вибірка")
plt.ylabel("Частота")
fig = plt.gcf()
fig.savefig('results/hist.png')