import isbn_validator

def test_isbn_valid(isbn):
  isbn_validator.is_valid_isbn("80-8592-17-4")
  isbn_validator.is_valid_isbn("978-80-86056-31-9")
  isbn_validator.is_valid_isbn("978-80-904248-2-55555")


def test_isbn_valid_10format(isbn):
  isbn_validator.is_isbn10_valid.is_isbn10("0-7167-0344-0")
  isbn_validator.is_isbn10_valid.is_isbn10("0-7167-0344-0")
  isbn_validator.is_isbn10_valid.is_isbn10("978-0-7167-0344-0")

  def test_isbn_valid_13format(isbn):
  isbn_validator.is_isbn10_valid.is_isbn13("388-0-53-101-3")
  isbn_validator.is_isbn10_valid.is_isbn13("978-3-16-148410-0")
  isbn_validator.is_isbn10_valid.is_isbn13("978-0-7167-0344-0")
  


