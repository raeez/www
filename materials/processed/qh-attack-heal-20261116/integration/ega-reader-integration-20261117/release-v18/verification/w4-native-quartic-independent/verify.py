"""Independent finite checks on native PBW weight -1, graded precomposition and L4."""
from collections import Counter
from functools import cache
from itertools import combinations, permutations
import json


# Species 0,1,2 are the independent matter fields of spins 2,3,4.
# Species 3,4,5 are the odd ghosts gamma_2,gamma_3,gamma_4.
starting_weight = (2, 3, 4, -1, -2, -3)
negative_sum = sum(sum(range(1, -w + 1)) for w in starting_weight if w < 0)
assert negative_sum == 10
letters = [(jet, species)
           for species, w in enumerate(starting_weight)
           for jet in range(negative_sum - w + 1)]


def weight(letter):
    jet, species = letter
    return jet + starting_weight[species]


def odd(letter):
    return letter[1] >= 3


nonpositive = [g for g in letters if weight(g) <= 0]
positive = sorted((g for g in letters if weight(g) > 0), key=weight)
assert all(odd(g) for g in nonpositive)


@cache
def positive_words(n, start=0):
    if n == 0:
        return ((),)
    words = []
    for index in range(start, len(positive)):
        g = positive[index]
        if weight(g) > n:
            break
        for rest in positive_words(n - weight(g), index + int(odd(g))):
            words.append((g,) + rest)
    return tuple(words)


def states(w):
    for size in range(len(nonpositive) + 1):
        for lower in combinations(nonpositive, size):
            remaining = w - sum(weight(g) for g in lower)
            if remaining < 0:
                continue
            for upper in positive_words(remaining):
                yield tuple(sorted(lower + upper))


target = set(states(0))
src_count = Counter()
tgt_count = Counter(sum(map(odd,w)) for w in target)
pivots = set()
for w in states(-1):
    src_count[sum(map(odd,w))] += 1
    jet, species = w[-1]
    # In the associated graded, act on a highest jet of the chosen species.
    # The new variable didn't occur, so even multiplicities remain nonzero
    # in char 0 and odd variables remain distinct. Lower-jet terms are lower
    # triangular in maximum jet. A pivot can be uniquely reduced to its input.
    pivot = tuple(sorted(w[:-1] + ((jet + 1, species),)))
    assert pivot in target and pivot not in pivots
    pivots.add(pivot)
assert max(tgt_count) == 15
assert tgt_count[8] == 24451 and tgt_count[9] == 23109
assert tgt_count[11] == 8878 and tgt_count[12] == 3408 and tgt_count[15] == 9
assert len(pivots) == sum(src_count.values())


def parity(u):
    return (-1) ** (u % 2)


# Sign standardizing Q f=f d_P to the usual Hom differential.
def standard_sign(m):
    return parity(m * (m + 1) // 2)


for m in range(16):
    assert standard_sign(m + 1) == parity(m + 1) * standard_sign(m)
    for u in range(-4, 9):
        # Composition of natural transformations and opposite product.
        for v in range(-4, 9):
            assert parity(v*m+u*(m+v)) == parity(u*v+(u+v)*m)
        # The two terms involving df cancel in [d,R(u)]. The remaining
        # term has exactly the standard sign of R(du).
        assert parity(u*m) == parity(u+u*(m+1))
        assert parity(u*m+m) == parity((u+1)*m)


# In the symmetrization map S^4(sH) -> T^4(sH), sa is even and su odd.
# Explicitly label repeated inputs to preserve all permutation multiplicities.
inputs = ('a1', 'a2', 'a3', 'u')
word_count = Counter()
for word in permutations(range(4)):
    koszul = parity(sum(
        int(i == 3) * int(j == 3)
        for p, i in enumerate(word) for j in word[p+1:] if i > j))
    key = ''.join('u' if inputs[i] == 'u' else 'a' for i in word)
    word_count[key] += koszul
assert word_count == {'aaau': 6, 'aaua': 6, 'auaa': 6, 'uaaa': 6}

print(json.dumps({
    "native_basis": "tensor of universal W4 even jets and the three odd ghost jet families",
    "PBW_minimum_total_negative_ghost_weight": -negative_sum,
    "finite_dimensions_by_ghost_number": {
        str(n): {"weight_minus_one":src_count[n], "weight_zero":tgt_count[n]}
        for n in range(16)},
    "translation_distinct_nonzero_highest_jet_pivots":len(pivots),
    "weight_zero_states":len(target),
    "precomposition": "standardization, product and differential identities checked in all stated degrees",
    "symmetric_word_coefficients":dict(word_count),
    "quartic_symmetric_bracket_on_normal_form": "6 gamma s(az)",
}, indent=2))
