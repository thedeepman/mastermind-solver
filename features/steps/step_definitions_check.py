from behave import given, when, then

from Mastermind import check_if_valid
from Result import Result


@given(u'I give it permutation "{option}" and previous result "{previous_option}" with "{reds:d}" reds and "{whites:d}" whites')
def step_impl(context, option, previous_option, reds, whites):
    context.current_perm = [int(num.strip()) for num in option.split(',')]
    context.previous_result = Result([int(num.strip()) for num in previous_option.split(',')], reds, whites)
    context.previous_result_perm = [int(num.strip()) for num in previous_option.split(',')]

@when(u'I check if this permutation is valid')
def step_impl(context):
    context.answer = check_if_valid(context.previous_result, context.current_perm)


@then(u'the result will be "{expected_answer}"')
def step_impl(context, expected_answer):
    assert context.answer == (True if expected_answer.lower() == 'true' else False)
