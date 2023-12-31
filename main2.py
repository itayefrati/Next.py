def read_file(file):
    try:
        f = open(file, "r")

    except FileNotFoundError:
        print('__CONTENT_START__' + '\n' + "__NO_SUCH_FILE__" + '__CONTENT_END__')

    else:
        lines = f.read().split()
        print('__CONTENT_START__' + '\n' + str(lines) + '\n' + '__CONTENT_END__')
        f.close()

    
def main():
    file = open(r'C:\Users\איתי\OneDrive\מסמכים', encoding='utf-8')
    read_file(file)


if __name__ == '__main__':
    main()
