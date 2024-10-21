def get_enum_key_by_value(enum_class, value):
    for member in enum_class:
        if member.value == value:
            return member.name
    return None
