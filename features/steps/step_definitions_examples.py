from behave import given, when, then

import Main


@given(u'I have a new method')
def step_impl(context):
    return


@when(u'I give it "{num:d}" and "{operation}"')
def step_impl(context, num, operation):
    context.answer = Main.method_with_examples(num, operation)


@then(u'the result should be "{expected_answer:d}"')
def step_impl(context, expected_answer):
    print(expected_answer)
    print(context.answer)
    assert context.answer == expected_answer

