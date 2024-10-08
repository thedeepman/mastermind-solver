from behave import given, when, then

from Mastermind import generate_all_possibilities


@given(u'I setup a game with "{slots:d}" slots and "{colors:d}" colors')
def step_impl(context, slots, colors):
    context.slots = slots
    context.colors = colors


@when(u'I generate all permutations with repeats')
def step_impl(context):
    context.possibilities = []
    generate_all_possibilities(True, context.colors, context.slots, context.possibilities)


@when(u'I generate all permutations without repeats')
def step_impl(context):
    context.possibilities = []
    generate_all_possibilities(False, context.colors, context.slots, context.possibilities)


@then(u'total possibilities should be "{answer:d}"')
def step_impl(context, answer):
    assert answer == len(context.possibilities)
