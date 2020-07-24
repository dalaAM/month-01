#面向对象    工资计算器
class SalaryCalculator:
    
    free_income = 5000

    def __init__(self,list_salary_before_tax,special_deduction=0,base_pay=3613):
        self.list_salary_before_tax = list_salary_before_tax
        self.special_deduction = special_deduction
        self.base_pay = base_pay
        self.__social_insurance = 0
        self.__list_tax = None
        self.__list_salary_after_tax = None
        self.get_salary()

    @property
    def list_salary_before_tax(self):
        return self.__list_salary_before_tax

    @list_salary_before_tax.setter
    def list_salary_before_tax(self,value):
        for i in range(len(value)):
            if value[i]<0:
                value[i] = 0
        self.__list_salary_after_tax = value

    @property
    def special_deduction(self):
        return self. __special_deduction

    @special_deduction.setter
    def special_deduction(self,value):
        if value<0:
            value = 0
        self.__special_deduction = value

    @property
    def base_pay(self):
        return  self.__base_pay

    @base_pay.setter
    def base_pay(self,value):
        if 3613<= value <= 23565:
            self.__base_pay = value
        else:
            raise Exception('社保缴费基数超过国家限制')
    
    @property
    def social_insurance(self):
        return self.__social_insurance
    
    @property
    def list_tax(self):
        return self.__list_tax
    
    @property
    def list_salary_after_tax(self):
        return self.__list_salary_after_tax

    def __calculate_personal_income_tax(self):
        self.__list_tax = []
        for i in range(len(self.list_salary_before_tax)):
            month = i+1
            salary_pay_tax = self.__get_salary_pay_tax(self.social_insurance,month)
            tax = self.__get_tax(salary_pay_tax,self.__list_tax)
            list_tax.append(tax)
        
    def __get_salary_pay_tax(self,social_insurance,month):
        return sum(self.list_salary_before_tax[:month]) - (SalaryCalculator.free_income+ self.special_deduction+social_insurance)*month
    
    def __get_tax(self,salary_pay_tax):
        deduction,tax_rate = self.__get_tax_rate_and_deduction(salary_pay_tax)
        tax = round(salary_pay_tax * tax_rate - deduction - sum(self.__list_tax),2)
        return tax
    
    def __get_tax_rate_and_deduction(self,salary_pay_tax): 
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

    def __calculate_salary_after_tax(self):
        self.__list_salary_after_tax = [self.__list_salary_before_tax[i] - self.__list_tax[i] - self.__social_insurance for i in range(len(self.__list_salary_before_tax))]

    def __calculate_social_insurance(self):
        self.__social_insurance = 3+self.__base_pay*(0.08+0.02+0.002+0.12)
    
    def get_salary(self):
        self.__calculate_social_insurance()
        self.__calculate_personal_income_tax()
        self.__calculate_salary_after_tax()
        return self.list_salary_after_tax 