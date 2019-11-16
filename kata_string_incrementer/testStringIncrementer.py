from kata_string_incrementer.stringIncrementer import StringIncrementer


def add_number_after_character():
    test_string = StringIncrementer('Aap')
    assert test_string.return_string() == 'Aap1', "Nummer niet toegevoegd na alfabetisch karakter"


def add_incremented_number_after_number():
    test_string = StringIncrementer('A1B2')
    assert test_string.return_string() == 'A1B23', "Laatste nummer niet opgehoogd"


add_number_after_character()
add_incremented_number_after_number()
