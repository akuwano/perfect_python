with open('test.txt') as f:
    search = input()
    count = 0
    for line in f:
        print(line)
        if line.indexof(search) > -1:
            count += 1
    print(count)

