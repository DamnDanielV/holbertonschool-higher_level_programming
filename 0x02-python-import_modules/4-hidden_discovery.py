#!/usr/bin/python3
import hidden_4

def main():
    for element in dir(hidden_4):
        for char in element[:2]:
            if char != '_':
                print(element)
                break

if __name__ == '__main__':
    main()
