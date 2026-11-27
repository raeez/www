"""Check specialized PBW state windows, associated-graded translation pivots and the quartic sign."""

from collections import defaultdict, Counter
from hashlib import sha256
from itertools import permutations
from math import factorial
from pathlib import Path
import json

WB = Path("/tmp/astra62-programme-rebuild-20261118/constructions/w-bockstein")


def ghost_windows():
    negative_and_zero = [(0, 0, 0)]
    positive = defaultdict(list)
    positive[0] = [(0, 0)]
    for spin in (2, 3, 4):
        for r in range(10 + spin):
            energy = 1 - spin + r
            bit = 1 << ((spin - 2) * 21 + r)
            if energy <= 0:
                negative_and_zero += [(e + energy, q + 1, mask | bit) for e, q, mask in negative_and_zero]
            else:
                for weight in range(10, energy - 1, -1):
                    positive[weight].extend((q + 1, mask | bit) for q, mask in positive[weight - energy])
    return negative_and_zero, positive


def load_native_basis():
    states = {}
    with (WB / "input-neg/basis.tbl").open() as data:
        for line in data:
            degree, count = map(int, line.split())
            states[degree] = {tuple(map(int, data.readline().split())) for _ in range(count)}
            assert len(states[degree]) == count
    return states


def make_state_spaces():
    matter = json.loads((WB / "input-neg/matter-labels.json").read_text())
    negative, positive = ghost_windows()
    by_energy = defaultdict(list)
    variables = {}
    index = {}
    for i, word in enumerate(matter):
        by_energy[-sum(n for _, n in word)].append(i)
        variables[i] = tuple(sorted(6 * (-n - species - 2) + species for species, n in word))
        index[variables[i]] = i
    tables = {-1: defaultdict(set), 0: defaultdict(set)}
    for weight in tables:
        for e, q, mask in negative:
            for matter_energy, mids in by_energy.items():
                for qp, positive_mask in positive.get(weight - e - matter_energy, ()):
                    for mid in mids:
                        tables[weight][q + qp].add((mid, mask | positive_mask))
    original = load_native_basis()
    assert all(tables[0][q] == original.get(q, set()) for q in set(tables[0]) | set(original))
    return tables, variables, index


def translation_pivots(tables, variables, index):
    pivots = set()
    maximum_jet_order = 0
    max_coefficient = 0
    for q, states in tables[-1].items():
        for mid, mask in states:
            mvars = variables[mid]
            gvars = []
            remaining = mask
            while remaining:
                low = remaining & -remaining
                bit = low.bit_length() - 1
                species, r = divmod(bit, 21)
                gvars.append(6 * r + 3 + species)
                remaining -= low
            # Highest jet first, largest species breaks ties. The derivative
            # of that occurrence is the only variable in its new jet order.
            chosen = max((*mvars, *gvars))
            r, species = divmod(chosen, 6)
            maximum_jet_order = max(maximum_jet_order, r)
            if species < 3:
                updated = list(mvars)
                updated.remove(chosen)
                updated.append(chosen + 6)
                target = (index[tuple(sorted(updated))], mask)
                coefficient = (r + 1) * mvars.count(chosen)
            else:
                bit = 21 * (species - 3) + r
                target = (mid, mask ^ (1 << bit) ^ (1 << (bit + 1)))
                coefficient = r + 1  # Exterior reordering is a unit sign.
            assert coefficient > 0 and target in tables[0][q] and target not in pivots
            pivots.add(target)
            max_coefficient = max(max_coefficient, coefficient)
    assert len(pivots) == sum(map(len, tables[-1].values()))
    return len(pivots), maximum_jet_order, max_coefficient


def symmetrization():
    # Label the three copies separately to keep all six contributions.
    labels = ("a1", "a2", "a3", "u")
    suspended_degrees = (2, 2, 2, 7)
    by_position = Counter()
    for p in permutations(range(4)):
        exponent = sum(suspended_degrees[i] * suspended_degrees[j]
                       for k, i in enumerate(p) for j in p[k + 1:] if i > j)
        by_position[p.index(3)] += (-1) ** exponent
    assert list(sorted(by_position.values())) == [6] * 4
    assert by_position[3] == factorial(3)
    return dict(sorted(by_position.items()))


def main():
    tables, variables, index = make_state_spaces()
    assert (WB / "input-neg/basis.tbl").read_bytes() == (WB / "input-pos/basis.tbl").read_bytes()
    assert (WB / "input-neg/matter-labels.json").read_bytes() == (WB / "input-pos/matter-labels.json").read_bytes()
    pivots, maximum_jet, max_coefficient = translation_pivots(tables, variables, index)
    source_dims = [len(tables[-1][q]) for q in range(17)]
    exact_ranks = []
    for n in source_dims:
        exact_ranks.append(n - (exact_ranks[-1] if exact_ranks else 0))
    assert min(exact_ranks) >= 0 and exact_ranks[-1] == 0
    square = json.loads((WB / "product-3-3.json").read_text())
    assert len(square) == 11033 and all((2 * v) % 1000003 for _, v in square)
    print(json.dumps({"native_fibre": "tau=-3/2; state PBW basis independent of special nonzero tau",
                      "weight_zero_exact_match_to_native_basis": True,
                      "weight_zero_dimensions": [len(tables[0][q]) for q in range(17)],
                      "weight_minus_one_dimensions": source_dims,
                      "weight_minus_one_ranks_implied_by_native_acyclicity": exact_ranks,
                      "distinct_associated_graded_target_pivots_of_translation": pivots,
                      "max_source_jet_order": maximum_jet, "max_absolute_pivot_coefficient": max_coefficient,
                      "separate_plus_fibre_nonzero_marked_cochain_square_entries": len(square),
                      "suspended_shuffle_coefficients_by_position_of_u": symmetrization(),
                      "native_normal_form_only_position": 3, "native_shuffle_obstruction": "6*gamma*az",
                      "both_signed_basis_tables_byte_identical": True,
                      "basis_source_sha256": sha256((WB / "input-neg/basis.tbl").read_bytes()).hexdigest()},
                     indent=2))


if __name__ == "__main__":
    main()
