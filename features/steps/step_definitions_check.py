from behave import given, when, then

@given(u'I have a check method')
def step_impl(context):
    return


@when(u'I give it permutation "{option}" and "{previous_option}" with "{reds:d}" reds and "{whites:d}" whites')
def step_impl(context, option, previous_option, reds, whites):
    context.current_perm = [int(num.strip()) for num in option.split(',')]
    context.previous_result_perm = [int(num.strip()) for num in previous_option.split(',')]
    print(context.current_perm)
    print(context.previous_result_perm)
    context.answer = True


@then(u'the result will be "{expected_answer}"')
def step_impl(context, expected_answer):
    assert context.answer == True if expected_answer.lower() == 'true' else False
