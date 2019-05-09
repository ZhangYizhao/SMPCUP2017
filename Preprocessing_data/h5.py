import pandas as pd



i = 1
blogs = pd.read_csv('final4w.csv', header=None, sep=',',
                    encoding='utf-8')
result = []
while (i <371):
    line = blogs.ix[i]
    try:
        list = eval(line.values[2])
        str = list[0]+ ' ' +list[1] + ' ' + list[2]
        result.append(str)
        i = i + 1
    except:
        continue
    print(i)

pd.DataFrame(result).to_csv('look.txt', index=None, header=None, encoding='utf-8')


