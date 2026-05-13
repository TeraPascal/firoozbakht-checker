import datetime
import pandas as pd

while True:
    print("\n\n.\n..\n...\n..\n.\n")

    def txtreader(file):
        data = pd.read_csv(f"{file}.txt", header = None, sep = " ")
        data = data.values.tolist()[0]
        if not data[len(data)-1] > 1:
            del data[len(data)-1]
        return data

    limit = int(input('maximum number of the fact check range :\n  >  '))
    print()

    primes = txtreader(f"primesuntil{limit}")
    for n in range(len(primes)):
        try:
            p0 = primes[n]
            p1 = primes[n+1]
            n = n+1
            print(datetime.datetime.now(),f" - solving for prime numbers {p0} and {p1} ..")
            if p1 ** (1/(n+1)) < p0 ** (1/n):
                print(" > True. \n")
            else :
                print(f" > Firoozbakht rule is not valid for prime numbers {p0} and {p1} ")
                break
        except:
            print(" > end of the prime numbers in the given range")


    print(f"\n\nFiroozbakht rule has fact checked until number {limit}")    
    print("done.")
