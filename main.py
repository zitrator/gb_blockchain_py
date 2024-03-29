import codecs
import hashlib

# Что нужно сделать:
# Параметры: n = 32 (биты),
# хэш-функция H = первые 4 байта SHA1 (sha1( input ).digest()[ : 4 ]),
# подпись - конкатенация 32 строк, каждая длины 4 байта.
#
# Для каких из следующих сообщений приведена корректная подпись (дан открытый ключ pk, сообщение message
# и его подпись signature):


pk1 = [[b'\xfb5\xadY', b'\xa5\xb6Q&'], [b'sP\x88\xe9', b'\xb1\xdaj\x9c'], [b'W\x7f3$', b'\xb5\xca}\x14'],
       [b'\x81\x06\xcb#', b'x]u*'], [b'\xe6\r\xba%', b'\x8a\x03\x8b\xee'], [b'%\x07\x84\xdf', b'\x9a_i^'],
       [b'\xe9\xe1\x05A', b'\xc8\xab\xfd\x18'], [b'\xe0W\x80\x83', b'\x9a4>f'], [b'\xaa\xba>\xf9', b'\xf40\x87G'],
       [b'\xd7\xf23\x02', b'\xbc\xf7\x89\xf6'], [b'Y\n,\x88', b'\xa2\xde@\xab'], [b'\xfbV*\x13', b'Qc\xb0q'],
       [b'\xeby]}', b'\xd5N\x9b\xe2'], [b'_\x9a\x17W', b'c8\xd4\x80'], [b'e)\xf1\xda', b'\xe1\x8e#\xca'],
       [b'P\xaf\xab\x97', b'd\xd2A#'], [b'_\xcf\xb4\x1b', b'<\x97\x8a\x13'], [b'\x9e\xc8[\xc4', b'.\xf2\xf9z'],
       [b'\xc1!\xd6\x1a', b'\xe9rI\xe0'], [b'\xcdW\xb9\xa8', b'@\x19\x9c\xf2'], [b'\x91\xfdyC', b'7\xdeFB'],
       [b'\xcd\x16\x050', b'Y/\x8f\xea'], [b'\xc3\xe7(\x05', b'[Q0\x16'], [b'!\x8cE\xde', b'\xf9J\xc4c'],
       [b'\x93%\x9f\\', b'\xcd\x97\xd5k'], [b'\xc6\x9ao{', b'\xff\xb2\x1bm'], [b'c\xb9C\x9f', b'\xd9\xaa\x7f0'],
       [b'\xf6\xad\xb0r', b'p\xfe\xe8\r'], [b'v\x83z\xe4', b'sr\x08\xdf'], [b'S\xe7U\x1b', b'!m\xbe2'],
       [b'\xdcy\x9a%', b'\xe2\xbev%'], [b'?^@n', b']\t\x1f\xca']]
message1 = b'Privet!!!'
signature1 = b'?\xad\xa8Z\xa3\xf3,\xfa\xdf@@ _\x8d\x9dO8\xc1\xf7\xf2\x15\xa9\x89\xb8\x92\x98q+P\x9e\x04\xf6\x05\xc7\xc0~\xab\xd4\xfdq!L\xce}\x18#DJ\x11\x0b"\x9c@\xdcQ\x9f\x9b\xe0\xac7\xa6\xe9\x91w\xc4\x94\xeb>\xab\xfa\x8e\xc0S\x93JH9\xc2\x93\xbcI\x0e=:\x98\xaf\xe9\x93\xcb\xe0\xf4mU\xdf\x8d\x9b\xd7\xa7\xe1\x0czVkpN\x14\x0e\x92\xf4\x07\x0b\xb7\x16\xd4<p\x92G9#\x02\xedI\xf4w\x9f\x1aq'

pk2 = [[b'\xfb5\xadY', b'\xa5\xb6Q&'], [b'sP\x88\xe9', b'\xb1\xdaj\x9c'], [b'W\x7f3$', b'\xb5\xca}\x14'],
       [b'\x81\x06\xcb#', b'x]u*'], [b'\xe6\r\xba%', b'\x8a\x03\x8b\xee'], [b'%\x07\x84\xdf', b'\x9a_i^'],
       [b'\xe9\xe1\x05A', b'\xc8\xab\xfd\x18'], [b'\xe0W\x80\x83', b'\x9a4>f'], [b'\xaa\xba>\xf9', b'\xf40\x87G'],
       [b'\xd7\xf23\x02', b'\xbc\xf7\x89\xf6'], [b'Y\n,\x88', b'\xa2\xde@\xab'], [b'\xfbV*\x13', b'Qc\xb0q'],
       [b'\xeby]}', b'\xd5N\x9b\xe2'], [b'_\x9a\x17W', b'c8\xd4\x80'], [b'e)\xf1\xda', b'\xe1\x8e#\xca'],
       [b'P\xaf\xab\x97', b'd\xd2A#'], [b'_\xcf\xb4\x1b', b'<\x97\x8a\x13'], [b'\x9e\xc8[\xc4', b'.\xf2\xf9z'],
       [b'\xc1!\xd6\x1a', b'\xe9rI\xe0'], [b'\xcdW\xb9\xa8', b'@\x19\x9c\xf2'], [b'\x91\xfdyC', b'7\xdeFB'],
       [b'\xcd\x16\x050', b'Y/\x8f\xea'], [b'\xc3\xe7(\x05', b'[Q0\x16'], [b'!\x8cE\xde', b'\xf9J\xc4c'],
       [b'\x93%\x9f\\', b'\xcd\x97\xd5k'], [b'\xc6\x9ao{', b'\xff\xb2\x1bm'], [b'c\xb9C\x9f', b'\xd9\xaa\x7f0'],
       [b'\xf6\xad\xb0r', b'p\xfe\xe8\r'], [b'v\x83z\xe4', b'sr\x08\xdf'], [b'S\xe7U\x1b', b'!m\xbe2'],
       [b'\xdcy\x9a%', b'\xe2\xbev%'], [b'?^@n', b']\t\x1f\xca']]
message2 = b'Hello!!!'
signature2 = b'\xe0/\xcc"h\xdc>\xc0R\x0f6c/\x88\x00\xbb\xfa\xc3\xdd\x99w\x15\xc37%\xb9\xe8\xcb\xa3\xbab\xf2\x8c\xdd\x95$\xdf\x01\x8ba\'\xe9\xe0T\x82 \xa5\xe8\x9cs\xfaC_xr\xca\xedK\x03\xbb\xb0\x9a\xd77\xf3u\xf0;\xbf+\x0e\xff\xa6\xf8?F\xdc\x94\xe6\xf4\xefc\x8e\xd14\x9b<\x94q\x97\xb7M\x1c&r58\x8d^2\xaa\xc1\xac\xdd\x04\xe7z|$I2\xa9\xce\x81\xccU\xd8\xaa\xfa\xc8$\x1f\x1bM\x99[\x19\x11'

pk3 = [[b'\xe3+\xbf\xec', b'm\xb42\xea'], [b'\xa2\xb8AY', b'N\xd3\x17^'], [b'\xc2\xb2\x0c\xa8', b's\xde\xcdE'],
       [b'n\xf0$\x9c', b'\xf1\xc0?\xbc'], [b'\xbc\xb4\x95\xf0', b'D_\xc3\xb8'], [b'\x11\x12\r\x94', b'=\xa7\x80\xd1'],
       [b'\x9c\xd2L\x95', b'jC\xf2\xad'], [b'\xf5\xc7*\xd0', b'\xdef\x0f\x9f'], [b'\x88\x96{\xae', b'\xee$\x96\xd0'],
       [b'\xf7\xef\x8d"', b'\x87\x8c\xe6\x8a'], [b'\x17\xb6H\xa4', b'd\xc6\x9d\x7f'], [b'Q0\xa6\xc8', b'\xcf;;\x1c'],
       [b'\x9d\x03\xb3K', b'z\xd9\x11\xa0'], [b';|/\xb3', b'\xb4\x96\x0e&'], [b'\x90\xbe\x05\xbc', b'\x9d_\x9cE'],
       [b'P\xdc\xc0\xa4', b'?\x88\xb5z'], [b'\x1e\x0e\xe5\xc4', b'\x97\x1c\x166'], [b')P\xacZ', b'\x0b\xac\x9f\x1f'],
       [b'\xfef|\xdc', b'\xea\x0b\x85\xe4'], [b'\xec\xee\n\x8e', b'I\x9d+\x87'], [b'A\x91\x91J', b'n\x85I;'],
       [b'\x1a\t\xf9C', b'\xe0\x7f\xd7H'], [b'\x90+\xc8\x85', b'\xf2RIM'], [b't\xe7\\\xc5', b'\xc4\xe9PO'],
       [b'\x83\xe4\x1a2', b'^\xb9:F'], [b'\x13\xb1t.', b'\x9a.]\xb6'], [b'd\xdf\x0e\xd5', b'v\xf8\xe3\xac'],
       [b'\x84\xc4*U', b'\xb6I\xc3\xe2'], [b'G\xff\xbf\xca', b'\xf8;\x8fc'], [b'\x91 \xcf\x00', b'/D\x0eB'],
       [b'\x7fK\xd5j', b'~\x15rk'], [b'\xb0\xd9\xf8\xac', b'\xd3\xaet5']]
message3 = b'Blockchain!'
signature3 = b'\xad\x9e9i\x82jM\x86 UP72\x0b\xc1w\xb1\x08\x8a$q\xe1\xf4\x17\x19\xb0\xa0n\xe46\x19\xbd\xc6\xeb\xad\xe8d\xc0\xfdPZ\x14\x01\n\xaf\x8a\x18UP\xaf>"\xe3\x906?\xc2T\xe5\x08\x86j\xbau\xfd\xe2\xd0w\xf0\x14Q\xf8\x04}T\x81uz*s\xda\x99\xc4">5\xb3\xc0\x8f\x81\x18\xe4\xbe\x06=2\xde!\x17\xaf&\xd8\xf0\xdb\xf1|D\x1f\x14\xa2\x8c\xd5\x86\xaf\x1f\x89\x08\xac\x96\x00w\x1d\xb9\xceq\x04\x88D'


def check_signature(msg, pk, signature):
    hash_msg = hashlib.sha1(msg).digest()[:4]
    current_bit = 0
    while current_bit < 32:
        hashed_sk_part = hashlib.sha1(signature[current_bit * 4: current_bit * 4 + 4]).digest()[:4]
        i = current_bit // 8
        j = current_bit % 8
        if (hash_msg[i] << j & 128) != 0:
            if pk[current_bit][1] != hashed_sk_part:
                return False
        else:
            if pk[current_bit][0] != hashed_sk_part:
                return False
        current_bit += 1
    return True


def task_three():
    print(check_signature(message1, pk1, signature1))
    print(check_signature(message2, pk2, signature2))
    print(check_signature(message3, pk3, signature3))


if __name__ == '__main__':
    task_three()
