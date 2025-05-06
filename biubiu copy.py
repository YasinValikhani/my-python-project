import random

def generate_hezar_code(length=10):
    return ''.join(random.choices('6789ABCDEF', k=length))

def generate_codes(count=5):
    return [generate_hezar_code() for _ in range(count)]

def save_to_file(codes, filename='code.txt'):
    with open (filename, 'w') as f :
        for code in codes:
            f.write(code + "\n")

if __name__ == "__main__":
    codes = generate_codes(5)
    save_to_file(codes)
    print(codes)

ali = ' dodolTala'