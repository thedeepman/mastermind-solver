from behave import given, when, then

@given(u'I have a check method')
def step_impl(context):
    return


@when(u'I give it permutation "{option}" and "{previous_option}" with "{reds:d}" reds and "{whites:d}" whites')
def step_impl(context, option, previous_option, reds, whites):
    print(option)
    context.answer = True
    return


@then(u'the result will be "{expected_answer}"')
def step_impl(context, expected_answer):
    return context.answer == expected_answer
