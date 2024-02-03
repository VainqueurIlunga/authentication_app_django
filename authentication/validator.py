from django.core.exceptions import ValidationError


class ContainsLetterValidator:  # la classe verifie si le mot de passe contient une lettre
    def validate(self, password, user=None):
        if not any(char.isalpha() for char in password):  # verifier les alphabets dans le password
            raise ValidationError('le mot de passe doit contenir une lettre', code='password_no_letters')

    @staticmethod
    def get_help_text():
        return 'le mot de passe doit contenir au moins une lettre majuscule ou minuscule'


class ContainsNumberValidator:  # la classe verifie si le mot de passe contient un chiffre
    def validate(self, password, user=None):
        if not any(character.isdigit() for character in password):
            raise ValidationError('le mot de passe doit contenir au moin un chiffre de 0 à 9', code='password_no_digit')

    @staticmethod
    def get_help_text():
        return 'le mot de passe doit contenir au moins un chiffre'
