import re
import string
from typing import List
import argparse

LETTERS = string.ascii_uppercase

def test_permutation(table, check_fix=False):
    if len(table) != 26:
        raise Exception('Unexpected table length, expect 26 found', len(table))

    dup = []
    for i, c in enumerate(table):
        if c < 0 or c > 25:
            raise Exception('Unexpected number, expect between 0 and 25, found ', c)
        if c != table[i]:
            raise Exception('error on permutation ', c)
        if check_fix:
            if i == c:
                raise Exception('error on, no fix expected ', c)
        if c in dup:
            raise Exception('Unexpected duplicate', c,table)
        dup.append(c)


def letter_to_index_in_alphabet(letter):
    return LETTERS.index(letter)


def reverse_rotor(rotor) -> List[int]:
    x = [0] * 26
    for i, r in enumerate(rotor):
        x[r] = i
    return x


def create_rotor(initiale):
    if initiale > 25 or initiale < 0:
        raise Exception("Unexpected initalie value ", initiale)


    return [((initiale + x) % 26) for x in range(0, 26)]

def encode(letter, i):
    index = letter_to_index_in_alphabet(letter)
    connection_index = CONNECTION[index]
    rotor_index1 = ROTOR1[(connection_index + i) % 26]
    rotor_index2 = ROTOR2[(rotor_index1 + (i // 26 % 26)) % 26]
    rotor_index3 = ROTOR3[(rotor_index2 + ((i // 26) // 26 % 26)) % 26]
    reflecteur_index = REFLECTEUR[rotor_index3]

    return LETTERS[reflecteur_index]


def decode(letter, i):
    index = letter_to_index_in_alphabet(letter)
    reflecteur_index = REFLECTEUR[index]
    r_rotor_index3 = REVERSE_ROTOR3[reflecteur_index - ((i // 26) // 26 % 26)]
    r_rotor_index2 = REVERSE_ROTOR2[r_rotor_index3 - (i // 26 % 26)]
    r_rotor_index1 = (REVERSE_ROTOR1[r_rotor_index2] - i) % 26
    r_permut_index = CONNECTION[r_rotor_index1]

    return LETTERS[r_permut_index]

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="input")
    parser.add_argument("--connection", help="")
    parser.add_argument("--reflecteur", help="")
    parser.add_argument("--rotor1", help="")
    parser.add_argument("--rotor2", help="")
    parser.add_argument("--rotor3", help="")
    args = parser.parse_args()

    input = args.input
    if not input:
        raise Exception('Unexpected empty input')

    if args.connection:
        CONNECTION = args.connection
    else:
        CONNECTION = [22, 17, 25, 11, 16, 19, 15, 23, 13, 12, 21, 3, 9, 8, 20, 6, 4, 1, 24, 5, 14, 10, 0, 7, 18, 2]
    test_permutation(table=CONNECTION)

    if  args.reflecteur:
        REFLECTEUR = args.reflecteur
    else:
        REFLECTEUR = [16, 14, 19, 25, 21, 17, 23, 18, 15, 12, 22, 24, 9, 20, 1, 8, 0, 5, 7, 2, 13, 4, 10, 6, 11, 3]

    test_permutation(table=REFLECTEUR, check_fix=True)

    if   args.rotor1:
        ROTOR1 = create_rotor(int(args.rotor1))
    else:
        ROTOR1 = create_rotor(3)

    if args.rotor2:
        ROTOR2 = create_rotor(int(args.rotor2))
    else:
        ROTOR2 = create_rotor(11)
    if args.rotor3:
        ROTOR3 = create_rotor(int(args.rotor3))
    else:
        ROTOR3 = create_rotor(22)

    REVERSE_REFLECTEUR = reverse_rotor(rotor=REFLECTEUR)
    REVERSE_ROTOR1 = reverse_rotor(rotor=ROTOR1)
    REVERSE_ROTOR2 = reverse_rotor(rotor=ROTOR2)
    REVERSE_ROTOR3 = reverse_rotor(rotor=ROTOR3)



    # input = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    # input = "URUZGTKIXTSCNWSRZCUFUBLJLAAXXCJXGCXTQMRUEPJSEWEVGUBGNTOGORALEUDFDIMBPOHBZZXQQOECJXVQVPCOLAGLXLYIOSHCGCNVCRGKPZWKNWXLAXDCTRZGARHDNPGWFQDEPVTBQREKLQNTWYDTRRHXKSBORCELNPFVHBFWYOFRROPHXESADWNMXBSFEKLFWZZXSLJKQLROQUDIVQAHUYHTNUYEMKQMZOCYCIUDHJQBEXBWPLEMGSBYRNQUNPGPHYOTYSITHJQHBNALQMWZKNZUEKUWRGKKMFCIHYSVSARHOFYFVAMRMRZKADTAMTYVLWQBTMJRWWEMDKCKIRDDCNWVXTFISDEOGRNJNWVMVGBWPDTZTKLSXCGKPAXHPHWZOQFQBSQIEVTUZAFQVFTBBROMCAAZQGZCSHOGVJEDWCWVXQBBWKMRGTIUAJNAGMSGRNYPPCYCMZPTEJP"
    input_letters = re.sub(r'[^a-zA-Z]', '', input).upper()

    encoded = ''
    decoded = ''
    decoded_only = ''
    for i, letter in enumerate(input_letters):
        l = encode(letter, i)
        encoded += l

        decoded += decode(l, i)
        decoded_only += decode(letter, i)

    print("encoded ", encoded)
    print("decoded ", decoded)
    print("decoded_only ", decoded_only)
    print("input ", input_letters)
    assert decoded == input_letters, 'fail encode'


