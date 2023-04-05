print(sum([ord(cur) - (96 if cur.islower() else 38) for line in [row.strip() for row in open('input1.txt').readlines()]
      for cur in {a for a in line[:len(line)//2] if a in line[len(line)//2:]}]))
