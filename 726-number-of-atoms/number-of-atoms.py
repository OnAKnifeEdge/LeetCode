class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def calculate_multipliers(formula):

            multipliers = []
            running_multiplier = 1
            stack = [1]
            num = ""

            for c in reversed(formula):
                if c.isdigit():
                    num = c + num
                elif c.isalpha():
                    num = ""  # Reset number for atoms
                elif c == ")":
                    multiplier = int(num) if num else 1
                    running_multiplier *= multiplier
                    stack.append(multiplier)
                    num = ""
                elif c == "(":
                    running_multiplier //= stack.pop()
                    num = ""

                multipliers.append(running_multiplier)

            return multipliers[::-1]  # Reverse to match formula order

        def parse_formula(formula, multipliers):
            """Parse the formula and count atoms."""
            atom_counts = defaultdict(int)
            i = 0
            while i < len(formula):
                if formula[i].isupper():
                    # Extract atom name
                    atom = formula[i]
                    i += 1
                    while i < len(formula) and formula[i].islower():
                        atom += formula[i]
                        i += 1

                    # Extract count
                    count = ""
                    while i < len(formula) and formula[i].isdigit():
                        count += formula[i]
                        i += 1

                    # Update atom count
                    count = int(count) if count else 1
                    atom_counts[atom] += count * multipliers[i - 1]
                else:
                    i += 1  # Skip parentheses

            return atom_counts

        def format_result(atom_counts):
            """Format the result string."""
            return "".join(
                atom + (str(count) if count > 1 else "")
                for atom, count in sorted(atom_counts.items())
            )

        multipliers = calculate_multipliers(formula)
        atom_counts = parse_formula(formula, multipliers)
        return format_result(atom_counts)
