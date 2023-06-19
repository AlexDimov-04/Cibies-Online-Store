from django.forms import ValidationError

def alphanumeric_charcters_validator(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Your name must contains letters only!')
        
def first_letter_uppercase_validator(value):
    if value[0].islower():
        raise ValidationError('Your name must start with an uppercase letter!')
    