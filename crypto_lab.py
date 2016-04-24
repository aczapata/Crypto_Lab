from collections import Counter
file = open("cipher_text.txt", "r")
p = file.readline()
n = 2
p_terms = [p[i:i + n] for i in range(0, len(p), n)]
print "The plain text has " + str(len(p)) + " characters and " + str(len(p_terms)) + " terms"
IC_EN = 0.067
common_ocurrences = ['20','65','61','69','74', '68', '6f', '53', '4e', '72']
candidates = []
for i in xrange(2, 11):
    j = 1
    c_terms = {}
    count_terms = {}
    unique_terms = {}
    for k in xrange(1, i + 1):
        c_terms.setdefault(k, [])
        count_terms.setdefault(k, Counter())
        unique_terms.setdefault(k, [])
    for p_hexa in p_terms:
        c_terms[j].append(p_hexa)
        if (j == i):
            j = 1
        else:
            j += 1
    print "Key=" + str(i)
    for k in xrange(1, i + 1):
        count_terms[k].update(c_terms[k])
        unique_terms[k] = set(c_terms[k])
        # print "Tabla de Frecuencias"
        # for term,n in count_terms[k].most_common(len(count_terms[k])):
        # print term + " p= " + str(n)
        IC = 0.0
        sw = True
        for i_c in count_terms[k]:
                IC += count_terms[k][i_c] * (count_terms[k][i_c] - 1.0)
        n = sum(count_terms[k].values())
        IC = IC / (float(n) * float(n - 1))
        if abs(IC - IC_EN) > 0.015:
            sw = False
        print "Terms " + str(k) + " N = " + str(len(unique_terms[k])) + " IC = " + str(IC)
    if sw is True:
        print "Key " + str(i) + " is a candidate!"
        candidates.append(i)

i = candidates[0]
print "Key=" + str(i)
for k in xrange(1, i + 1):
    print "Tabla de Frecuencias"
    terms_k= []
    counter_k=Counter()
    for term, n in count_terms[k].most_common(10):
        for value in common_ocurrences:
            c_bin = hex(int(term, 16) ^ int(value, 16))[2:].zfill(2)
            terms_k.append(c_bin)
        print term + " p= " + str(n)
    counter_k.update(terms_k)
    print counter_k