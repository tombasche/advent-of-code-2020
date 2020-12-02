from one import fix_expense_report

def test_fix_expense_report():
    inputs = [1955, 65, 2019, 123, 543, 2123]
    assert fix_expense_report(inputs) ==  127075

def test_fix_expense_report_part_two():
    inputs = [1955, 64, 1, 123, 543, 2123]
    assert fix_expense_report(inputs) ==  127075