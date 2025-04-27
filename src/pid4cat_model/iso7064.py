"""
ISO/IEC 7064 Checksum Algorithms Implementation in Python

This module implements the eight generic check digit (character) systems for
numeric, alphabetic, and alphanumeric strings. ISO/IEC 7064 specifies two
types of systems that use the same algorithm with different parameters:
Pure systems (MOD 11-2, MOD 37-2, MOD 97-10, MOD 661-26, and MOD 1271-36)
and Hybrid systems (MOD 11,10, MOD 27,26, and MOD 37,36).

Author: David Linke, adapted from cdigit implementation
License: MIT

Inspired by JavaScript package: https://github.com/LiosK/cdigit (License: MIT)
"""

from typing import List, Tuple


class ISO7064Pure:
    """
    Implements the ISO 7064 pure system recursive method.
    """

    def __init__(self, mod: int, radix: int, alphabet: str, flavor: str) -> None:
        """
        Initialize the ISO 7064 pure system.

        Args:
            name (str): Short name of the algorithm.
            long_name (str): Full name of the algorithm.
            mod (int): Modulus used in the algorithm.
            radix (int): Radix (base) of the number system.
            alphabet (str): Character set used in the algorithm.
            flavor (str): Type of the algorithm ("EXTRA_CHAR" or "TWO_CCS").
        """
        self.name: str = f"mod_{mod}_{radix}"
        self.long_name: str = f"ISO/IEC 7064, MOD {int}-{radix}"
        self.mod: int = mod
        self.radix: int = radix
        self.alphabet: str = alphabet
        self.flavor: str = flavor  # "EXTRA_CHAR" or "TWO_CCS"

    def compute_from_num_vals(self, ns: List[int]) -> List[int]:
        """
        Compute the check character(s) from numerical values.

        Args:
            ns (list[int]): List of numerical values representing the input string.

        Returns:
            list[int]: List of numerical values representing the check character(s).

        Raises:
            ValueError: If the input is empty or contains invalid values.
        """
        max_num_val = (
            len(self.alphabet) - 1
            if self.flavor == "EXTRA_CHAR"
            else len(self.alphabet)
        )
        if not ns:
            raise ValueError("String to be protected is empty")
        if any(e < 0 or e >= max_num_val or not isinstance(e, int) for e in ns):
            raise ValueError("Invalid numerical value detected")

        c = 0
        for e in ns + [0, 0] if self.flavor == "TWO_CCS" else ns + [0]:
            if c > 0xFFF_FFFF_FFFF:  # ~2^44 at max
                c %= self.mod
            c = c * self.radix + e
        c = (self.mod + 1 - (c % self.mod)) % self.mod

        if self.flavor == "TWO_CCS":
            return [c // self.radix, c % self.radix]
        return [c]

    def compute(self, s: str) -> str:
        """
        Compute the check character(s) for the given string.

        Args:
            s (str): Input string without check characters.

        Returns:
            str: Check character(s) computed from the input string.
        """
        char_map = {
            c: i
            for i, c in enumerate(
                self.alphabet[:-1] if self.flavor == "EXTRA_CHAR" else self.alphabet
            )
        }
        ns = [char_map[c] for c in s if c in char_map]

        cc = self.compute_from_num_vals(ns)
        if self.flavor == "TWO_CCS":
            return self.alphabet[cc[0]] + self.alphabet[cc[1]]
        return self.alphabet[cc[0]]

    def parse(self, s: str) -> Tuple[str, str]:
        """
        Parse the input string into the bare string and check character(s).

        Args:
            s (str): Input string with check characters.

        Returns:
            tuple[str, str]: Bare string and check character(s).

        Raises:
            ValueError: If the check character(s) cannot be found.
        """
        char_map = {c: i for i, c in enumerate(self.alphabet)}
        n = 2 if self.flavor == "TWO_CCS" else 1
        cc = s[-n:]
        if len(cc) == n and all(c in char_map for c in cc):
            return s[:-n], cc
        raise ValueError("Could not find check character(s)")

    def generate(self, s: str) -> str:
        """
        Generate a protected string by appending check character(s).

        Args:
            s (str): Input string without check characters.

        Returns:
            str: Protected string with appended check character(s).
        """
        return f"{s}{self.compute(s)}"

    def validate(self, s: str) -> bool:
        """
        Validate the input string with check character(s).

        Args:
            s (str): Input string with check characters.

        Returns:
            bool: True if the string is valid, False otherwise.
        """
        bare, cc = self.parse(s)
        return self.compute(bare) == cc


class ISO7064Hybrid:
    """
    Implements the ISO 7064 hybrid system recursive method.
    """

    def __init__(self, alphabet: str) -> None:
        """
        Initialize the ISO 7064 hybrid system.

        Args:
            alphabet (str): Character set used in the algorithm.
        """
        self.alphabet: str = alphabet
        self.mod = len(self.alphabet)
        self.char_map = {c: i for i, c in enumerate(self.alphabet)}
        radix = self.mod - 1
        self.name: str = f"mod_{self.mod}_{radix}"
        self.long_name: str = f"ISO/IEC 7064, MOD {int}-{radix}"

    def compute_from_num_vals(self, ns: List[int]) -> List[int]:
        """
        Compute the check character(s) from numerical values.

        Args:
            ns (list[int]): List of numerical values representing the input string.

        Returns:
            list[int]: List of numerical values representing the check character(s).

        Raises:
            ValueError: If the input is empty or contains invalid values.
        """
        mod = len(self.alphabet)
        if not ns:
            raise ValueError("String to be protected is empty")
        if any(e < 0 or e >= mod or not isinstance(e, int) for e in ns):
            raise ValueError("Invalid numerical value detected")

        c = mod
        for e in ns:
            c = (c % (mod + 1)) + e
            c = (c % mod or mod) * 2
        c %= mod + 1

        return [(mod + 1 - c) % mod]

    def compute(self, s: str) -> str:
        """
        Compute the check character(s) for the given string.

        Args:
            s (str): Input string without check characters.

        Returns:
            str: Check character(s) computed from the input string.
        """
        ns = [self.char_map[c] for c in s if c in self.char_map]

        cc = self.compute_from_num_vals(ns)
        return self.alphabet[cc[0]]

    def parse(self, s: str) -> Tuple[str, str]:
        """
        Parse the input string into the bare string and check character(s).

        Args:
            s (str): Input string with check characters.

        Returns:
            tuple[str, str]: Bare string and check character(s).

        Raises:
            ValueError: If the check character(s) cannot be found.
        """
        char_map = {c: i for i, c in enumerate(self.alphabet)}
        cc = s[-1]
        if cc in char_map:
            return s[:-1], cc
        raise ValueError("Could not find check character(s)")

    def generate(self, s: str) -> str:
        """
        Generate a protected string by appending check character(s).

        Args:
            s (str): Input string without check characters.

        Returns:
            str: Protected string with appended check character(s).
        """
        return f"{s}{self.compute(s)}"

    def validate(self, s: str) -> bool:
        """
        Validate the input string with check character(s).

        Args:
            s (str): Input string with check characters.

        Returns:
            bool: True if the string is valid, False otherwise.
        """
        bare, cc = self.parse(s)
        return self.compute(bare) == cc


# ISO/IEC 7064 Implementations
mod11_2 = ISO7064Pure(11, 2, "0123456789X", "EXTRA_CHAR")
mod37_2 = ISO7064Pure(37, 2, "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ*", "EXTRA_CHAR")
mod97_10 = ISO7064Pure(97, 10, "0123456789", "TWO_CCS")
mod661_26 = ISO7064Pure(661, 26, "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "TWO_CCS")
mod1271_36 = ISO7064Pure(1271, 36, "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", "TWO_CCS")

mod11_10 = ISO7064Hybrid("0123456789")
mod27_26 = ISO7064Hybrid("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
mod37_36 = ISO7064Hybrid("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")


if __name__ == "__main__":
    import stdnum.iso7064.mod_97_10

    # Example usage of mod97_10
    number = "123456789"
    print(f"Number: {number}")

    # Appends checksum to the number
    generated = mod97_10.generate(number)
    print(f"Generated: {generated}")

    # Computes the check character
    computed = mod97_10.compute(number)
    stdnum_check_digit = stdnum.iso7064.mod_97_10.calc_check_digits(number)
    print(f"Computed Check Character: {computed}  ---  stdnum: {stdnum_check_digit}")

    # Validates the generated number
    is_valid = mod97_10.validate(generated)
    is_valid_stdnum = stdnum.iso7064.mod_97_10.is_valid(generated)
    print(f"Is valid: {is_valid}  ---  stdnum: {is_valid_stdnum}")

    # Parses the generated number
    bare, cc = mod97_10.parse(generated)
    print(f"Parsed Bare: {bare}, Check Character: {cc}")
