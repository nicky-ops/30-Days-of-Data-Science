def main():
    open("/path/to/mars.jpg")

if __name__ == '__main__':
    main()


try:
    open("mars.jpg")
except FileNotFoundError as err:
    print("got a problem trying to read the file:", err)