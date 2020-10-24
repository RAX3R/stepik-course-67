def encryption_decryption(text: str, orig_char: str, cod_char: str):
    result = ""
    list_text = list(text)
    list_orig_char = list(orig_char)
    list_cod_char = list(cod_char)

    for i, ii in enumerate(list_text):
        for j, jj in enumerate(list_orig_char):
            if ii == jj:
                list_text[i] = list_cod_char[j]
        result += list_text[i]

    return result


if __name__ == '__main__':
    orig = input()
    cod = input()
    text_en = input()
    text_de = input()

    encryption = encryption_decryption(text_en, orig, cod)
    decryption = encryption_decryption(text_de, cod, orig)

    print(encryption)
    print(decryption)

