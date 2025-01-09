import time

tiend = 0
sek = 0
min = 0

try:
    while True:
        if sek >= 59 and tiend >= 9:
            min += 1
            sek = 0
            tiend = 0
        elif tiend >= 9:
            sek += 1
            tiend = 0
        else:
            time.sleep(1/10)
            tiend += 1
        print(f"{min} | {sek} | {tiend}")
except KeyboardInterrupt:
    print(f"Endelig tid: {min} | {sek} | {tiend}")
