import pytest
from src.pid4cat_model.iso7064 import (
    mod11_2,
    mod37_2,
    mod97_10,
    mod661_26,
    mod1271_36,
    mod11_10,
    mod27_26,
    mod37_36,
)

# === Tests for pure systems ===


@pytest.mark.parametrize(
    "algo, input_str, expected_output, check_chars",
    [
        # mod11_2
        (mod11_2, "001175717748247", "0011757177482476", "6"),
        (mod11_2, "747633", "7476336", "6"),
        (mod11_2, "734404529805608", "7344045298056080", "0"),
        (mod11_2, "41812925", "418129259", "9"),
        (mod11_2, "986596515101003", "986596515101003x", "x"),
        # mod37_2
        (mod37_2, "j0ho3mgx3f8lkilhhh7", "j0ho3mgx3f8lkilhhh7o", "o"),
        (mod37_2, "iq", "iqp", "p"),
        (mod37_2, "sah538pzb", "sah538pzb3", "3"),
        # mod97_10
        (mod97_10, "794", "79444", "44"),
        (mod97_10, "0000", "000001", "01"),
        (mod97_10, "00001055949422872", "0000105594942287263", "63"),
        # mod661_26
        (mod661_26, "baisdlafk", "baisdlafkbm", "bm"),
        (mod661_26, "gcjfbciojtlvo", "gcjfbciojtlvour", "ur"),
        # mod1271_36
        (mod1271_36, "iso79", "iso793w", "3w"),
        (mod1271_36, "xvmzn7cd83796i1q65vvza", "xvmzn7cd83796i1q65vvza0j", "0j"),
        # leading/trailing whitespace is stripped before checksum
        (mod1271_36, "iso79 ", "iso793w", "3w"),
        (mod11_2, " 747633 ", "7476336", "6"),
    ],
)
def test_pure_systems_valid(algo, input_str, expected_output, check_chars):
    """
    Test ISO 7064 pure systems with valid data.
    """
    assert hasattr(algo, "flavor")
    # Test generate
    generated = algo.generate(input_str)
    assert generated == expected_output, f"Failed to generate for {algo.name}"

    # Test validate
    assert algo.validate(expected_output), f"Failed to validate for {algo.name}"

    # Test parse
    bare, cc = algo.parse(expected_output)
    assert bare == input_str.strip(), f"Failed to parse bare string for {algo.name}"
    assert cc == check_chars, f"Failed to parse check character for {algo.name}"
    assert algo.compute(input_str) == cc, (
        f"Failed to compute check character for {algo.name}"
    )


@pytest.mark.parametrize(
    "algo, input_str, invalid_output, invalid_check_chars",
    [
        # mod11_2
        (mod11_2, "001175717748247", "0011757177482477", "7"),
        (mod11_2, "97", "97x", "x"),
        # mod37_2
        (mod37_2, "tz25np", "tz25np5", "5"),
        (mod37_2, "r1wdrn9eq", "r1wdrn9eqk", "k"),
        # mod97_10
        (mod97_10, "794", "79445", "45"),
        (mod97_10, "5489482033978", "548948203397832", "32"),
        # mod661_26
        (mod661_26, "baisdlafk", "baisdlafkab", "ab"),
        (mod661_26, "gcjfbciojtlvo", "gcjfbciojtlvobi", "bi"),
        # mod1271_36
        (mod1271_36, "ermsin9w42jd", "ermsin9w42jd98", "98"),
        # leading/trailing whitespace is stripped before checksum
        (mod1271_36, "iso79 ", "iso7912", "12"),
        (mod11_2, " 97  ", "97x", "x"),
    ],
)
def test_pure_systems_invalid(algo, input_str, invalid_output, invalid_check_chars):
    """
    Test ISO 7064 pure systems with invalid data.
    """
    assert hasattr(algo, "flavor")
    # Test generate
    generated = algo.generate(input_str)
    assert generated != invalid_output

    # Test validate
    assert not algo.validate(invalid_output)

    # Test parse (the invalid output should still be parsed correctly)
    bare, cc = algo.parse(invalid_output)
    assert bare == input_str.strip()
    assert cc == invalid_check_chars
    assert algo.compute(input_str) != cc


# === Tests for hybrid systems ===


@pytest.mark.parametrize(
    "algo, input_str, expected_output, check_chars",
    [
        # mod11_10
        (mod11_10, "0794", "07945", "5"),
        (mod11_10, "003", "0032", "2"),
        (mod11_10, "86662765", "866627650", "0"),
        # mod27_26
        (mod27_26, "jejlmgj", "jejlmgjs", "s"),
        (mod27_26, "mufemstcatlit", "mufemstcatlitb", "b"),
        # mod37_36
        (mod37_36, "tbr", "tbr1", "1"),
        (mod37_36, "b3739u6cr", "b3739u6crk", "k"),
    ],
)
def test_hybrid_systems_valid(algo, input_str, expected_output, check_chars):
    """
    Test ISO 7064 hybrid systems with valid data.
    """
    assert not hasattr(algo, "flavor")

    generated = algo.generate(input_str)
    assert generated == expected_output, f"Failed to generate for {algo.name}"

    # Test validate
    assert algo.validate(expected_output), f"Failed to validate for {algo.name}"

    # Test parse
    bare, cc = algo.parse(expected_output)
    assert bare == input_str, f"Failed to parse bare string for {algo.name}"
    assert cc == check_chars, f"Failed to parse check character for {algo.name}"
    assert algo.compute(input_str) == cc, (
        f"Failed to compute check character for {algo.name}"
    )


@pytest.mark.parametrize(
    "algo, input_str, invalid_output, invalid_check_chars",
    [
        # mod11_10
        (mod11_10, "82380342642", "823803426424", "4"),
        (mod11_10, "04088080371", "040880803711", "1"),
        # mod27_26
        (mod27_26, "jejlmgj", "jejlmgjx", "x"),
        (mod27_26, "mufemstcatlit", "mufemstcatlith", "h"),
        # mod37_36
        (mod37_36, "mr", "mrz", "z"),
        (mod37_36, "4kwl6bpn", "4kwl6bpnh", "h"),
    ],
)
def test_hybrid_systems_invalid(algo, input_str, invalid_output, invalid_check_chars):
    """
    Test ISO 7064 hybrid systems with invalid data.
    """
    assert not hasattr(algo, "flavor")

    generated = algo.generate(input_str)
    assert generated != invalid_output

    # Test validate
    assert not algo.validate(invalid_output)

    # Test parse (the invalid output should still be parsed correctly)
    bare, cc = algo.parse(invalid_output)
    assert bare == input_str
    assert cc == invalid_check_chars
    assert algo.compute(input_str) != cc


# === Tests for exceptions ===


def test_pure_systems_invalid_chars():
    """
    Test ISO 7064 systems with invalid check char.
    """
    with pytest.raises(ValueError) as excinfo:
        bare, cc = mod11_2.parse("AB123ß")
    assert "Could not find check character(s)" in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo:
        bare, cc = mod11_10.parse("AB123ß")
    assert "Could not find check character(s)" in str(excinfo.value)


@pytest.mark.parametrize("algo", [mod11_2, mod11_10])
def test_pure_systems_invalid_numbers(algo):
    """
    Test ISO 7064 hybrid systems with invalid input.
    """
    with pytest.raises(ValueError) as excinfo:
        _ = algo.compute_from_num_vals([])
    assert "String to be protected is empty" in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo:
        _ = algo.compute_from_num_vals([100])
    assert "Invalid numerical value detected" in str(excinfo.value)


@pytest.mark.parametrize(
    "algo, bad_input",
    [
        # pure systems
        (mod1271_36, "ISO 79"),  # internal space, alphabet is 0-9A-Z
        (mod97_10, "123-456"),  # hyphen not in 0-9
        (mod37_2, "FOO*BAR"),  # * is the extra check char, not input
        (mod11_2, "12a3"),  # a letter is not in 0-9
        # hybrid systems
        (mod11_10, "12 34"),  # internal space, alphabet is 0-9
        (mod27_26, "AB CD"),  # internal space, alphabet is A-Z
    ],
)
def test_compute_rejects_chars_outside_alphabet(algo, bad_input):
    """
    Characters outside the algorithm's input alphabet must raise ValueError.
    Since leading/trailing whitespace is stripped, only characters in the
    interior count.
    """
    with pytest.raises(ValueError, match="Invalid character"):
        algo.compute(bad_input)

    with pytest.raises(ValueError, match="Invalid character"):
        algo.generate(bad_input)

    # validate() must propagate the ValueError from compute(), not return False
    # — the bare prefix of the protected string is what compute() sees.
    bare_with_cc = bad_input + algo.alphabet[0]
    with pytest.raises(ValueError, match="Invalid character"):
        algo.validate(bare_with_cc)


@pytest.mark.parametrize(
    "algo, input_str, check_chars",
    [
        (mod11_2, "986596515101003", "x"),
        (mod37_2, "J0HO3MGX3F8LKILHHH7", "o"),
        (mod661_26, "GCJFBCIOJTLVO", "ur"),
        (mod1271_36, "ISO79", "3w"),
        (mod27_26, "JEJLMGJ", "s"),
        (mod37_36, "B3739U6CR", "k"),
    ],
)
def test_upper_case_gives_the_lower_case_check_chars(algo, input_str, check_chars):
    """
    Checksums are case-insensitive: upper-case input gives the check
    character(s) of the lower-case input, and validation accepts upper-case
    check character(s).
    """
    assert algo.compute(input_str) == check_chars
    assert algo.validate(input_str + check_chars.upper())
    assert algo.validate(input_str.lower() + check_chars.upper())
    assert algo.parse(input_str + check_chars.upper()) == (
        input_str,
        check_chars.upper(),
    )
