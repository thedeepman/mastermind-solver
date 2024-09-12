from behave import given, when, then

def example_method():
    return 0

@given('I have a method')
def step_impl(context):
    return


@when('I call it')
def step_impl(context):
    context.answer = example_method()


@then('the result should be 0')
def step_impl(context):
    assert context.answer == 0
