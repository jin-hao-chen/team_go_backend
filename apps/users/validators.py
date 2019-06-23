import re

from django.core.validators import ValidationError


def validate_username(value):
    pattern = re.compile(r'^\d{10}$')
    if not pattern.match(value):
        raise ValidationError('学号必须是 10 个 0-9 的数字')
