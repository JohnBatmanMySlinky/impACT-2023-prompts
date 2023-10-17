import random

def mix(PERCENT_CLEAN, clean, messy):
    final = [] 
    for i in range(len(messy)):
        if random.random() < PERCENT_CLEAN:
            final.append(clean[i])
        else:
            final.append(messy[i])
    return final


if __name__ == "__main__":
    with open("one.txt", "r") as f:
        raw = [x.strip().lower() for x in f.readlines()]
        messy = raw[:100]
        clean = raw[100:]

    assert len(messy) == len(clean)

    random.seed(10)

    PERCENT_CLEAN = .8


    final = mix(PERCENT_CLEAN=PERCENT_CLEAN, clean=clean, messy=messy)

    print(final)