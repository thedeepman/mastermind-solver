from behave import given, when, then

def method_with_examples(num, operation):
    if operation == 'add':
        return num + num
    elif operation == 'multiply':
        return num * num
    else:
        return Exception("Not a valid operation")

@given(u'I have a new method')
def step_impl(context):
    return


@when(u'I give it "{num:d}" and "{operation}"')
def step_impl(context, num, operation):
    context.answer = method_with_examples(num, operation)


@then(u'the result should be "{expected_answer:d}"')
def step_impl(context, expected_answer):
    print(expected_answer)
    print(context.answer)
    assert context.answer == expected_answer

