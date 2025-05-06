import random

def generate_hex_code(length=24):
    return ''.join(random.choices('0123456789ABCDEF', k=length))

def generate_codes(count=10):
    return [generate_hex_code() for _ in range(count)]

def save_to_file(codes, filename='code.txt'):
    with open (filename, 'w') as f :
        for code in codes:
            f.write(code + "\n")

if __name__ == "__main__":
    codes = generate_codes(10)
    save_to_file(codes)
    print(codes)

ali = ' dodolTala'