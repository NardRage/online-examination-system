from django import template

register = template.Library()

@register.filter
def has_group(user, group_name):
    if user.is_superuser:
        return True
    return user.groups.filter(name=group_name).exists()

@register.filter
def get_option_text(question, option):
    if option == 'A':
        return question.option_A
    elif option == 'B':
        return question.option_B
    elif option == 'C':
        return question.option_C
    elif option == 'D':
        return question.option_D

@register.filter
def bool_to_colour(value):
    if value:
        return 'success'
    return 'danger'

@register.filter
def bool_to_passing_status(value):
    if value:
        return 'PASS'
    return 'FAIL'

@register.filter
def bool_to_answer_status(value):
    if value:
        return 'Correct'
    return 'Incorrect'