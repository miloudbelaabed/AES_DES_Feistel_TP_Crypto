
def Feistel(message_clair, function):
    message_bin_blocs = []
    for m in message_clair:
        msg = bin(ord(m)).replace('0b', '')
        if len(msg) < 8:
            for i in range(8-len(msg)):
                msg = "0"+msg
        message_bin_blocs.append(msg)
    message_chiffre = []
    for bloc in message_bin_blocs:
        left = bloc[:4]
        right = bloc[4:]
        result_right = function(right)
        left = "".join([str(int(left[i]) ^ int(result_right[i]))for i in range(len(left))])
        message_chiffre.append(left+right)
    text_chiffre = ''

    for m in message_chiffre:
        text_chiffre += chr(int(m, 2))
    return text_chiffre

    # return left+right


def FeistelForExo2(bloc,function):
  left = bloc[:4]
  right = bloc[4:]
  result_right = function(right)
  
  left = "".join([str(int(left[i])^int(result_right[i])) for i in range(len(left))])
  return left+right

def reverse_miroire(x):
    return x[::-1]


def FeistelFunction1(bloc):
    key = "1011"
    return "".join([str(int(bloc[i]) ^ int(key[i])) for i in range(len(bloc))])


def FeistelFunction2(bloc):
    key = "0101"
    rev_bloc = "".join(["0" if i == "1" else "1" for i in range(len(bloc))])
    return "".join([str(int(rev_bloc[i]) ^ int(key[i])) for i in range(len(bloc))])


def CryptRound(message_clair, rounds_function):
    for function in rounds_function:
        message_bin_blocs = []
        for m in message_clair:
            msg = bin(ord(m)).replace('0b', '')
            if len(msg) < 8:
                for i in range(8-len(msg)):
                    msg = "0"+msg
            message_bin_blocs.append(msg)
        message_chiffre = []
        for bloc in message_bin_blocs:
            message_chiffre.append(FeistelForExo2(bloc, function))
        text_chiffre = ''
        for m in message_chiffre:
            text_chiffre += chr(int(m, 2))
        print("le Text chiffré est:  "+text_chiffre)
        print("le Text chiffré en binaire est:  "+"".join(message_chiffre))
        message_clair = text_chiffre
    return text_chiffre

# crypt = CryptRound("test message clairË",[FeistelFunction1,FeistelFunction2])
