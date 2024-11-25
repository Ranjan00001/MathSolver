

QUESTION_IMG_SIZE = 640

SYMBOLS_IMG_SIZE = 28

SYMBOLS = [
    # Numbers
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    # Basic Operators
    '+', '-', '*', '/', '=', '<', '>', '≤', '≥', '≠',
    # Punctuation & Separators
    '(', ')', '[', ']', '{', '}', ',', '.', '|',
    # Algebra & Geometry
    'θ', 'π', 'α', 'β', 'γ', 'Δ', '∠', '∥', '⊥',
    # Functions & Trigonometry
    'sin', 'cos', 'tan', 'cot', 'sec', 'cosec', 'log', 'ln',
    'sqrt', '∛', 'abs', 'floor', 'ceil',
    # Calculus
    'dx', 'dy', '∫', '∑', 'lim', '∞', 'Δx', 'Δy',
    # Set Theory & Logic
    '∈', '∉', '∪', '∩', '∅', '⊂', '⊃', '⊆', '⊇', '∃', '∀',
    # Additional Symbols
    '→', '≈', '≡', 'mod', '%', 'unk',
    # Uppercase English Alphabets
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 
    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    # Lowercase English Alphabets (excluding duplicates)
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y', 'z'
]


TOKEN_TYPE = {'NUMBERS':0, 'OPERATORS':1, 'SEPARATORS':2,
              'ALGEBRA': 3, 'FUNCTION': 4, 'CALCULUS':5,
              'SET_THEORY':6, 'ADDITIONAL':7, 'UPPERCASE':8,
              'LOWERCASE':9}

NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
OPERATORS = ['+', '-', '*', '/', '=', '<', '>', '≤', '≥', '≠']
SEPARATORS = ['(', ')', '[', ']', '{', '}', ',', '.', '|']
ALGEBRA = ['θ', 'π', 'α', 'β', 'γ', 'Δ', '∠', '∥', '⊥']
FUNCTION = ['sin', 'cos', 'tan', 'cot', 'sec', 'cosec', 'log',
            'ln', 'sqrt', '∛', 'abs', 'floor', 'ceil']
CALCULUS = ['d', 'dx', 'dy', '∫', '∑', 'lim', '∞', 'Δx', 'Δy']
SET_THEORY = ['∈', '∉', '∪', '∩', '∅', '⊂', '⊃', '⊆', '⊇', '∃', '∀']
ADDITIONAL = ['→', '↔', '≈', '≡', 'mod', '%', 'unk']
UPPERCASE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z']
LOWERCASE = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'y', 'z']