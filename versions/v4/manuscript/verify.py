import argparse
from fractions import Fraction
import json
from math import comb
from pathlib import Path


def polynomial(*coefficients):
    result = list(map(Fraction, coefficients))
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return tuple(result)


def add(*values):
    size = max(map(len, values))
    return polynomial(*(sum((item[index] if index < len(item) else 0)
                            for item in values) for index in range(size)))


def scale(value, multiplier):
    return polynomial(*(coefficient * multiplier for coefficient in value))


def multiply(first, second):
    result = [Fraction(0)] * (len(first) + len(second) - 1)
    for first_index, first_coefficient in enumerate(first):
        for second_index, second_coefficient in enumerate(second):
            result[first_index + second_index] += first_coefficient * second_coefficient
    return polynomial(*result)


def shift(value, offset):
    result = polynomial(0)
    for degree, coefficient in enumerate(value):
        result = add(result, polynomial(*(coefficient * comb(degree, power)
                     * offset ** (degree - power) for power in range(degree + 1))))
    return result


def choose(upper, lower):
    return comb(upper, lower) if 0 <= lower <= upper else 0


def row(index):
    return [choose(index + 2, column + 1) + choose(index + 1, column)
            + choose(index + 1, column + 1) + choose(index, column) - 4
            for column in range(index + 1)]


def convolution(index):
    values = row(index)
    return sum(values[column] * values[index - column] for column in range(index + 1))


def closed(index):
    return (4 * comb(2 * index + 4, index + 2) + 4 * comb(2 * index + 2, index + 1)
            + comb(2 * index, index) - 72 * 2 ** index + 16 * index + 40)


def recurrence(values, index):
    return (2 * (index + 2) * values[index] - (17 * index + 23) * values[index - 1]
            + (47 * index + 36) * values[index - 2] - 2 * (22 * index + 17) * values[index - 3]
            + 4 * (20 - index) * values[index - 4] + 8 * (2 * index - 9) * values[index - 5]
            + 24 * (12 * index - 47))


def triangle(index, column):
    return (choose(index + 2, column + 1) + choose(index + 1, column)
            + choose(index + 1, column + 1) + choose(index, column) - 4)


def middle_recurrence(values, index):
    return (2 * (index + 1) * values[index] - (7 * index + 5) * values[index - 1]
            + 2 * (3 - 2 * index) * values[index - 2] + 12 * (1 - 3 * index))


def near_recurrence(values, index):
    return (-2 * (index + 3) * (139 * index - 175) * values[index]
            + (1279 * index ** 2 + 1334 * index - 1089) * values[index - 1]
            - 2 * (167 * index + 121) * (2 * index - 3) * values[index - 2]
            + 12 * (111 * index ** 2 + 456 * index + 229))


def half_recurrence(values, index):
    return (-(index + 2) * (3 * index - 20) * values[index]
            - (index + 1) * (3 * index - 11) * values[index - 1]
            + (33 * index ** 2 - 180 * index - 100) * values[index - 2]
            + (15 * index ** 2 - 56 * index + 1) * values[index - 3]
            + 2 * (-51 * index ** 2 + 313 * index - 208) * values[index - 4]
            - 12 * (index - 1) * (index - 4) * values[index - 5]
            + 8 * (9 * index - 11) * (index - 5) * values[index - 6]
            + 4 * (-24 * index ** 2 + 196 * index - 365))


def companion_symbolic_checks():
    def product(*factors):
        result = polynomial(1)
        for factor in factors:
            result = multiply(result, factor)
        return result

    near_terms = [
        scale(product(polynomial(0, 1), polynomial(-1, 2), polynomial(-175, 139),
                      polynomial(1, 14, 9)), -4),
        product(polynomial(-1, 1), polynomial(-4, -4, 9), polynomial(-1089, 1334, 1279)),
        scale(product(polynomial(-2, 1), polynomial(2, 1), polynomial(121, 167),
                      polynomial(9, -22, 9)), -1),
    ]
    even_terms = [
        scale(product(polynomial(-3, 1), polynomial(-1, 1), polynomial(-20, 3),
                      polynomial(10, 9)), -8),
        scale(product(polynomial(-3, 1), polynomial(-8, 9), polynomial(-100, -180, 33)), 2),
        scale(product(polynomial(0, 1), polynomial(-26, 9), polynomial(208, -313, 51)), -1),
        product(polynomial(0, 1), polynomial(-2, 1), polynomial(-44, 9), polynomial(-11, 9)),
    ]
    odd_terms = [
        scale(product(polynomial(-2, 1), polynomial(-11, 3), polynomial(1, 9)), -4),
        product(polynomial(-17, 9), polynomial(1, -56, 15)),
        scale(product(polynomial(-1, 1), polynomial(-1, 1), polynomial(-35, 9)), -3),
    ]
    for terms in [near_terms, even_terms, odd_terms]:
        assert add(*terms) == polynomial(0)
    half_coefficients = [
        scale(product(polynomial(2, 1), polynomial(-20, 3)), -1),
        scale(product(polynomial(1, 1), polynomial(-11, 3)), -1),
        polynomial(-100, -180, 33), polynomial(1, -56, 15),
        polynomial(-416, 626, -102),
        scale(product(polynomial(-1, 1), polynomial(-4, 1)), -12),
        scale(product(polynomial(-11, 9), polynomial(-5, 1)), 8),
    ]
    assert add(*(scale(value, Fraction(1, 2 ** offset))
                 for offset, value in enumerate(half_coefficients))) == polynomial(0)
    assert add(*(scale(value, (-1) ** offset)
                 for offset, value in enumerate(half_coefficients))) == polynomial(0)
    assert add(*(multiply(value, polynomial(2 * offset - 5, -2))
                 for offset, value in enumerate(half_coefficients))) == polynomial(1460, -784, 96)
    near_coefficients = [scale(product(polynomial(3, 1), polynomial(-175, 139)), -2),
                         polynomial(-1089, 1334, 1279),
                         scale(product(polynomial(121, 167), polynomial(-3, 2)), -2)]
    assert add(*near_coefficients) == polynomial(687, 1368, 333)
    middle_part = {offset: polynomial(0) for offset in [-2, -1, 0, 1]}
    residual_part = dict(middle_part)
    for offset, coefficient in [(0, polynomial(2, 2)), (-1, polynomial(-5, -7)),
                                (-2, polynomial(6, -4))]:
        middle_part[offset] = add(middle_part[offset], coefficient)
        middle_part[offset + 1] = add(middle_part[offset + 1], scale(coefficient, 2))
    for offset, weight in [(0, 4), (-1, 4), (-2, 1)]:
        residual_part[offset + 1] = add(residual_part[offset + 1],
                                              scale(polynomial(offset + 1, 1), weight))
        residual_part[offset] = add(residual_part[offset],
                                   scale(polynomial(-4 * offset - 2, -4), weight))
    assert middle_part == residual_part
    return {'A027171_A027175_central_residual_identity': True,
            'A027174_cleared_polynomial_identity': True,
            'A027174_constant_correction': True,
            'A027179_even_cleared_polynomial_identity': True,
            'A027179_odd_cleared_polynomial_identity': True,
            'A027179_exponential_annihilation': True,
            'A027179_alternating_annihilation': True,
            'A027179_affine_inhomogeneity': True}


def symbolic_checks():
    lower = {0: polynomial(-2, -4), 1: polynomial(-27, -7), 2: polynomial(8, 2)}
    target = {0: polynomial(8, 16), 1: polynomial(60, -4), 2: polynomial(-254, -44),
              3: polynomial(271, 47), 4: polynomial(-108, -17), 5: polynomial(14, 2)}
    weights = [-4, 8, -5, 1]
    expansion = {index: polynomial(0) for index in range(6)}
    for offset, weight in enumerate(weights):
        for index, coefficient in lower.items():
            expansion[index + offset] = add(expansion[index + offset], scale(shift(coefficient, offset), weight))
    assert expansion == target
    binomial_part = {index: polynomial(0) for index in range(5)}
    residual_part = {index: polynomial(0) for index in range(5)}
    for index, coefficient in lower.items():
        for offset, weight in enumerate([1, 4, 4]):
            binomial_part[index + offset] = add(binomial_part[index + offset], scale(coefficient, weight))
    for offset, weight in enumerate([1, 6, 12, 8]):
        residual_part[offset] = add(residual_part[offset], scale(polynomial(-4 * offset - 2, -4), weight))
        residual_part[offset + 1] = add(residual_part[offset + 1], scale(polynomial(offset + 1, 1), weight))
    assert binomial_part == residual_part
    exponent = polynomial(0)
    affine = polynomial(0)
    for offset, coefficient in target.items():
        exponent = add(exponent, scale(coefficient, 2 ** offset))
        affine = add(affine, multiply(coefficient, polynomial(16 * offset + 40, 16)))
    assert exponent == polynomial(0)
    assert affine == polynomial(-312, -288)
    return {'operator_factorization': True, 'Bh_central_binomial_identity': True,
            'L_exponential_annihilation': True, 'L_affine_inhomogeneity': True}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--bfile', type=Path)
    parser.add_argument('--prefixes', type=Path)
    parser.add_argument('--limit', type=int, default=400)
    parser.add_argument('--output', type=Path)
    arguments = parser.parse_args()
    limit = arguments.limit
    assert limit >= 6
    values = [convolution(index) for index in range(limit + 1)]
    assert values == [closed(index) for index in range(limit + 1)]
    assert all(recurrence(values, index) == 0 for index in range(5, limit + 1))
    assert values[:5] == [1, 18, 150, 820, 3726]
    bfile_indices = []
    if arguments.bfile:
        for line in arguments.bfile.read_text().splitlines():
            if not line.strip() or line.lstrip().startswith('#'):
                continue
            index, value = map(int, line.split())
            assert convolution(index) == value
            bfile_indices.append(index)
    middle = {index: triangle(2 * index, index) for index in range(limit + 1)}
    odd_middle = {index: triangle(2 * index - 1, index - 1) for index in range(1, limit + 1)}
    near = {index: triangle(2 * index, index - 2) for index in range(2, limit + 1)}
    half = {index: sum(triangle(index, column) for column in range(index // 2 + 1))
            for index in range(limit + 1)}
    for index in range(limit + 1):
        central = comb(2 * index, index)
        assert middle[index] + 4 == Fraction(9 * index + 5, index + 1) * central
        if index >= 1:
            assert odd_middle[index] + 4 == Fraction(9 * index + 5, 2 * (index + 1)) * central
        if index >= 2:
            assert near[index] + 4 == Fraction(index * (9 * index ** 2 + 14 * index + 1),
                                             (index + 1) * (index + 2) * (index + 3)) * central
        even_part = (middle[index // 2] + 4) if index % 2 == 0 else 0
        assert half[index] == Fraction(9 * 2 ** index, 2) - 2 * index - 5 - (-1) ** index + Fraction(even_part, 2)
    assert all(middle_recurrence(middle, index) == 0 for index in range(2, limit + 1))
    assert all(middle_recurrence(odd_middle, index) == 0 for index in range(3, limit + 1))
    assert all(near_recurrence(near, index) == 0 for index in range(4, limit + 1))
    assert all(half_recurrence(half, index) == 0 for index in range(6, limit + 1))
    sequences = {'A027182': dict(enumerate(values)), 'A027171': middle,
                 'A027175': odd_middle, 'A027174': near, 'A027179': half}
    prefix_checks = {}
    if arguments.prefixes:
        for record in json.loads(arguments.prefixes.read_text()):
            for offset, value in enumerate(record['terms']):
                assert sequences[record['sequence']][record['offset'] + offset] == value
            prefix_checks[record['sequence']] = len(record['terms'])
    result = {'schema_version': 1, 'arithmetic': 'Python arbitrary-precision integers and exact rational polynomial coefficients',
              'closed_form_indices': [0, limit], 'recurrence_indices': [5, limit],
              'original_claim_indices_tested': [6, limit], 'bfile_indices': bfile_indices,
              'companion_recurrence_indices': {'A027171': [2, limit], 'A027175': [3, limit],
                                               'A027174': [4, limit], 'A027179': [6, limit]},
              'companion_initial_values': {name: [sequence[index] for index in sorted(sequence)[:8]]
                                          for name, sequence in sequences.items() if name != 'A027182'},
              'fresh_OEIS_prefix_terms_checked': prefix_checks,
              'initial_values': values[:11], 'source_example_corrected_value': values[2],
              'symbolic_checks': {**symbolic_checks(), **companion_symbolic_checks()},
              'scope': 'Finite sequence comparisons and exact symbolic operator algebra; the all-index proof is in note.tex.'}
    text = json.dumps(result, indent=2) + '\n'
    if arguments.output:
        arguments.output.write_text(text)
    print(text, end='')


if __name__ == '__main__':
    main()
