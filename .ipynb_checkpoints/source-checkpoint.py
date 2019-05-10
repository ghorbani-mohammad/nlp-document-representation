import io

lines = [line.rstrip('\n') for line in open('Data/HAM-Test.txt', encoding="utf8")]

for line in lines[0:10]:
    print(line)
