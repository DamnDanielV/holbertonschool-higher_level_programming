#!/usr/bin/python3
import sys


def add_q(a, row, sol_p):
    """add one queen of b digit if is save"""
    n_sol = []
    for c in sol_p:
        for b in range(row):
            if safe_mode(a, b, c):
                n_sol.append(c + [b])
    return n_sol


def safe_mode(a, b, c):
    """queen is unique and not in a diag"""
    if b not in c:
        return all(abs(c[col] - b) != a - col for col in range(a))
    else:
        return False


def queens():
    """initiates nqueens"""
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)
    if sys.argv[1].isdigit() is not True:
        print("N must be a number")
        sys.exit(1)
    else:
        n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solut = [[]]
    for a in range(n):
        solut = add_q(a, n, solut)
    for arr in solut:
        fo = []
        for a, b in enumerate(arr):
            fo.append([a, b])
        print(fo)

if __name__ == "__main__":
    """entry point"""
    queens()
