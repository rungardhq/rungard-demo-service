"""Normalise the e-mail address a project owner signs up with."""


def normalize_email(address: str) -> str:
    """`address` with surrounding whitespace removed and its domain in lower case.

    The address is split at its last "@": the part before it is kept exactly as
    given, since a mail server may treat it as case-sensitive. An address with
    no "@" is only stripped.
    """
    local, at, domain = address.strip().rpartition("@")
    return local + at + domain.lower() if at else domain
