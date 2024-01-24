def safe_print_division(a, b):
    """Returns the division of a by b."""
    try:
        div_result = a / b
    except (TypeError, ZeroDivisionError):
        div_result = None
    finally:
        print("Inside result: {}".format(div_result))
    return (div_result)
