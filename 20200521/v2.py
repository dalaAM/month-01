#函数式   个税计算器

#税前工资列表
list_salary_before_tax = [30000] * 12
#特别纳税扣除金额
special_deduction = 1000
#免税金额
free_income = 5000
#基本薪资
base_pay = 30000
#社保
social_insurance = 0

salary_after_tax = None
#保存个税的列表
list_tax = None

#计算社保
def calculate_social_insurance():
    global social_insurance
    social_insurance = 3+base_pay*(0.08+0.02+0.002+0.12)

#计算个税
def calculate_personal_income_tax():
    global list_tax
    list_tax = []
    for i in range(len(list_salary_before_tax)):
        month = i+1
        #计算需要纳税的薪资
        salary_pay_tax = get_salary_pay_tax(social_insurance,month)
        #获取当月个税
        tax = get_tax(salary_pay_tax,list_tax)
        list_tax.append(tax)

#计算需要纳税的薪资
def get_salary_pay_tax(social_insurance,month):
    return sum(list_salary_before_tax[:month]) - (free_income+ special_deduction+social_insurance)*month

#获取当月个税
def get_tax(salary_pay_tax,list_tax):
    deduction,tax_rate = get_tax_rate_and_deduction(salary_pay_tax)
    tax = round(salary_pay_tax * tax_rate - deduction - sum(list_tax),2)
    return tax

#获取速算扣除数和预扣率
def get_tax_rate_and_deduction(salary_pay_tax):
    if salary_pay_tax < 36000:
        tax_rate = 0.03
        deduction = 0
    elif salary_pay_tax <= 144000:
        tax_rate = 0.1
        deduction = 2520
    elif salary_pay_tax <= 300000:
        tax_rate = 0.2
        deduction = 16920
    elif salary_pay_tax <= 420000:
        tax_rate = 0.25
        deduction = 31920
    elif salary_pay_tax <= 660000:
        tax_rate = 0.3
        deduction = 52920
    elif salary_pay_tax <= 960000:
        tax_rate = 0.35
        deduction = 85920
    else:
        tax_rate = 0.45
        deduction = 181920
    return deduction, tax_rate


def calculate_salary_after_tax():
    global salary_after_tax
    salary_after_tax = [list_salary_before_tax[i] - list_tax[i] - social_insurance for i in range(len(list_salary_before_tax))]


def get_salary():
    '''
        获取税后工资
    '''
    #社保?
    calculate_social_insurance()
    #个税?
    calculate_personal_income_tax()
    #计算税后工资
    calculate_salary_after_tax()
    return salary_after_tax

res = get_salary()
print(res)