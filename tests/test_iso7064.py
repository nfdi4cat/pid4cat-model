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
        (mod11_2, "986596515101003", "986596515101003X", "X"),
        # mod37_2
        (mod37_2, "J0HO3MGX3F8LKILHHH7", "J0HO3MGX3F8LKILHHH7O", "O"),
        (mod37_2, "IQ", "IQP", "P"),
        (mod37_2, "SAH538PZB", "SAH538PZB3", "3"),
        # mod97_10
        (mod97_10, "794", "79444", "44"),
        (mod97_10, "0000", "000001", "01"),
        (mod97_10, "00001055949422872", "0000105594942287263", "63"),
        # mod661_26
        (mod661_26, "BAISDLAFK", "BAISDLAFKBM", "BM"),
        (mod661_26, "GCJFBCIOJTLVO", "GCJFBCIOJTLVOUR", "UR"),
        # mod1271_36
        (mod1271_36, "ISO 79", "ISO 793W", "3W"),
        (mod1271_36, "XVMZN7CD83796I1Q65VVZA", "XVMZN7CD83796I1Q65VVZA0J", "0J"),
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
    assert bare == input_str, f"Failed to parse bare string for {algo.name}"
    assert cc == check_chars, f"Failed to parse check character for {algo.name}"
    assert algo.compute(input_str) == cc, (
        f"Failed to compute check character for {algo.name}"
    )


@pytest.mark.parametrize(
    "algo, input_str, invalid_output, invalid_check_chars",
    [
        # mod11_2
        (mod11_2, "001175717748247", "0011757177482477", "7"),
        (mod11_2, "97", "97X", "X"),
        # mod37_2
        (mod37_2, "TZ25NP", "TZ25NP5", "5"),
        (mod37_2, "R1WDRN9EQ", "R1WDRN9EQK", "K"),
        # mod97_10
        (mod97_10, "794", "79445", "45"),
        (mod97_10, "5489482033978", "548948203397832", "32"),
        # mod661_26
        (mod661_26, "BAISDLAFK", "BAISDLAFKAB", "AB"),
        (mod661_26, "GCJFBCIOJTLVO", "GCJFBCIOJTLVOBI", "BI"),
        # mod1271_36
        (mod1271_36, "ISO 79", "ISO 7912", "12"),
        (mod1271_36, "ERMSIN9W42JD", "ERMSIN9W42JD98", "98"),
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
    assert bare == input_str
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
        (mod27_26, "JEJLMGJ", "JEJLMGJS", "S"),
        (mod27_26, "MUFEMSTCATLIT", "MUFEMSTCATLITB", "B"),
        # mod37_36
        (mod37_36, "TBR", "TBR1", "1"),
        (mod37_36, "B3739U6CR", "B3739U6CRK", "K"),
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
        (mod27_26, "JEJLMGJ", "JEJLMGJX", "X"),
        (mod27_26, "MUFEMSTCATLIT", "MUFEMSTCATLITH", "H"),
        # mod37_36
        (mod37_36, "MR", "MRZ", "Z"),
        (mod37_36, "4KWL6BPN", "4KWL6BPNH", "H"),
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
