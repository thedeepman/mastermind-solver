from behave import given, when, then

import Mastermind
from Result import Result


@given(u'I give it permutation "{option}" and previous result "{previous_option}" with "{reds:d}" reds and "{whites:d}" whites')
def step_impl(context, option, previous_option, reds, whites):
    context.current_perm = [int(num.strip()) for num in option.split(',')]
    context.previous_result = Result([int(num.strip()) for num in previous_option.split(',')], reds, whites)
    context.previous_result_perm = [int(num.strip()) for num in previous_option.split(',')]

@when(u'I check if this permutation is valid')
def step_impl(context):
    context.answer = Mastermind.check_if_valid(context.previous_result, context.current_perm)


@then(u'the result will be "{expected_answer}"')
def step_impl(context, expected_answer):
    assert context.answer == (True if expected_answer.lower() == 'true' else False)

@given(u'I have a guess "{guess}" for a game with answer "{answer}"')
def step_impl(context, guess, answer):
    context.guess = [int(num.strip()) for num in guess.split(',')]
    context.answer = [int(num.strip()) for num in answer.split(',')]


@when(u'I check if my guess is correct')
def step_impl(context):
    context.result = Mastermind.get_result(context.answer, context.guess)


@then(u'the result is "{reds:d}" reds and "{whites:d}" whites')
def step_impl(context, reds, whites):
    assert context.result.reds == reds and context.result.whites == whites

