from collections import Counter


def xor_hexa(term, value):
    c_bin = int(str(term), 16) ^ int(value, 16)
    c_bin = hex(c_bin)
    #c_bin = hex(int(c_bin, 16) % int("0x80", 16))
    # print str(term)+ " XOR "+ str(value) +" = "+ str(c_bin)
    if c_bin in non_ascii_values_hex:
        #print str(term)+ " True XOR "+ str(value) +" = "+ str(c_bin)
        return True
    else:
        #print str(term)+ " False XOR "+ str(value) +" = "+ str(c_bin)
        return False

def xor_hexa2(term, value):
    c_bin = int(str(term), 16) ^ int(value, 16)
    c_bin = hex(c_bin)
    # c_bin = hex(int(c_bin, 16) % int("0x80", 16))
    # print str(term)+ " XOR "+ str(value) +" = "+ str(c_bin)
    return c_bin

file = open("cipher_text.txt", "r")
p = file.readline()
n = 2
p_terms = [p[i:i + n] for i in range(0, len(p), n)]
print "The plain text has " + str(len(p)) + " characters and " + str(len(p_terms)) + " terms"
IC_EN = 0.067
common_ocurrences = ['20','65','61','69','74', '68', '6f', '53', '4e', '72']
candidates = []
candidate_terms = {}
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
        IC = 0.0
        sw = True
        for i_c in count_terms[k]:
                IC += count_terms[k][i_c] * (count_terms[k][i_c] - 1.0)
        n = sum(count_terms[k].values())
        IC = IC / (float(n) * float(n - 1))
        if abs(IC - IC_EN) > 0.010:
            sw = False
        print "Terms " + str(k) + " N = " + str(len(unique_terms[k])) + " IC = " + str(IC)
    if sw is True:
        print "Key " + str(i) + " is a candidate!"
        candidates.append(i)
        candidate_terms = c_terms
        break

key = candidates[0]
print "Key=" + str(key)
for t, cesar_set in candidate_terms.iteritems():

        ascii_values = list(xrange(256))
        non_ascii_values = list(xrange(32))
        ascii_values_hex = [hex(i) for i in ascii_values]
        non_ascii_values_hex = [hex(i) for i in non_ascii_values]
        non_ascii_values_hex.append("0x7f")
        non_ascii_values_hex.append("0x7c")
        # print ascii_values_hex
        # print non_ascii_values_hex
        for term in set(cesar_set):
            ascii_values_hex = [value for value in ascii_values_hex if not xor_hexa(term, value)]
        print "Values:"+ str(len(ascii_values_hex))
        ascii_values_str = [ chr(int(i,16)) for i in ascii_values_hex]
        #print ascii_values_str

        for key in ascii_values_hex[:200]:
            s = ""
            terms_key = []
            count_keys = Counter()
            for term in cesar_set:
                c_bin = xor_hexa2(term, key)
                terms_key.append(chr(int(c_bin,16)))
                #terms_key.append(c_bin)
            count_keys.update(terms_key)
            #print "Key " +(chr(int(key,16))) + "- " +str(key)
            #print count_keys
            #list_count = list(count_keys)
            #print list_count
            for y, f in count_keys.most_common(1):
                if y == " " or y == "e" or y == "a":
                    s = s+chr(int(key,16))
                    print chr(int(key,16)) + " " +str(key)+" is a Posible candidate with " + y
