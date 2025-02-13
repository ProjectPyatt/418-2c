import sys

def read_grammar():
    return {
        'S': [('A', 'B'), ('A', 'X')],
        'X': [('S', 'B')],
        'A': [('a',)],
        'B': [('b',)]
    }, 'S'

def cyk(grammar, start, s):
    n = len(s)
    dp = [[set() for _ in range(n)] for _ in range(n)]
    
    # Base case: Fill first row with terminal derivations
    for i, char in enumerate(s):
        for lhs, rhs in grammar.items():
            if (char,) in rhs:
                dp[i][i].add(lhs)
    
    # Recursive case: Filling the DP table for substrings of length 2 to n
    for l in range(2, n + 1):  # l is substring length
        for i in range(n - l + 1):  # i is start position
            j = i + l - 1  # j is end position
            for k in range(i, j):  # k is split position
                for lhs, rhs in grammar.items():
                    for r in rhs:
                        if len(r) == 2 and r[0] in dp[i][k] and r[1] in dp[k+1][j]:
                            dp[i][j].add(lhs)
    
    return 0 if start in dp[0][n-1] else 1

def main():
    grammar, start_symbol = read_grammar()
    input_str = "aabb"
    
    result = cyk(grammar, start_symbol, input_str)
    print(result)  # Print the result for visibility in Codespaces
    sys.exit(result)


if __name__ == "__main__":
    main()
