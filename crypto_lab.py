from collections import Counter
file = open("cipher_text.txt","r")
p = file.readline()
n = 2
p_terms = [p[i:i + n] for i in range(0, len(p), n)]
print "The plain text has " + str(len(p)) + " characters and " + str(len(p_terms)) + " terms"

for i in xrange(2, 11):
    j = 1
    c_terms = {}
    count_terms = {}
    unique_terms = {}
    for k in xrange(1, i+1):
        c_terms.setdefault(k, [])
        count_terms.setdefault(k, Counter())
        unique_terms.setdefault(k, [])
    for p_hexa in p_terms:
        c_terms[j].append(p_hexa)
        if (j == i):
            j = 1
        else:
            j += 1
    print "Key="+str(i)
    for k in xrange(1, i+1):
        count_terms[k].update(c_terms[k])
        unique_terms[k] = set(c_terms[k])

        print "Terms " + str(k) + " has " + str(len(unique_terms[k])) + " elements"
