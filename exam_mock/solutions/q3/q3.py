def top5_bigram_frequency(filename):
    bigram = {}
    for line in open(filename):
        words = line.lower().strip().split()
        for i in range(len(words)-1):
            b = words[i] + " " + words[i+1]
            bigram[b] = bigram.get(b, 0) + 1

    bigram = dict(sorted(bigram.items(), key=lambda x:x[1], reverse=True)[:5])
    return bigram

