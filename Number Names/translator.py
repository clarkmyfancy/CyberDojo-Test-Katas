from translator_helpers import Helpers

class Translator:

    def translate(self, number):
        result = ""
        
        if number == 0:
            result = "zero"
        
        elif self.is_a_single_digit(number):
            result += self.translate_single_digit(number)
            
        elif self.is_a_teen(number):
            result += self.translate_teens(number)
            
        elif Helpers().number_of_digits(number) == 2:
            result += self.translate_last_two_digits(number)
            
        elif Helpers().number_of_digits(number) == 3:
            result += self.translate_three_digits(number)
 
        return result
    
    def is_a_single_digit(self, number):
        return number >= 0 and number < 10
    
    def is_a_teen(self, number):
        return number >= 10 and number < 20
    
    def translate_single_digit(self, number):
        result = ""
        if number == 1:
            result = "one"
        elif number == 2:
            result = "two"
        elif number == 3:
            result = "three"
        elif number == 4:
            result = "four"
        elif number == 5:
            result = "five"
        elif number == 6:
            result = "six"
        elif number == 7:
            result = "seven"
        elif number == 8:
            result = "eight"
        elif number == 9:
            result = "nine"
        return result
    
    def translate_teens(self, number):
        result = ""
        if number == 10:
            result = "ten"
        elif number == 11:
            result = "eleven"
        elif number == 12:
            result = "twelve"
        elif number == 13:
            result = "thirteen"
        elif number == 14:
            result = "fourteen"
        elif number == 15:
            result = "fifteen"
        elif number == 16:
            result = "sixteen"
        elif number == 17:
            result = "seventeen"
        elif number == 18:
            result = "eighteen"
        elif number == 19:
            result = "nineteen"
        return result
    
    def translate_last_two_digits(self, number):
        # number is in form: Yx
        result = ''
        first_digit = int(number / 10) * 10
        result += self.translate_first_digit_of_two_digit_number(first_digit)
        
        second_digit = number % 10
        if second_digit != 0:
            result += ' '
        result += self.translate_single_digit(second_digit)
        
        return result
        
    def translate_first_digit_of_two_digit_number(self, number):
        result = ""
        if number == 20:
            result = "twenty"
        elif number == 30:
            result = "thirty"
        elif number == 40:
            result = "fourty"
        elif number == 50:
            result = "fifty"
        elif number == 60:
            result = "sixty"
        elif number == 70:
            result = "seventy"
        elif number == 80:
            result = "eighty"
        elif number == 90:
            result = "ninety"
        return result
    
    def translate_three_digits(self, number):
        result = ""
        
        result += self.translate_single_digit(Helpers().get_first_digit(number))
        result += ' hundred'
        number = Helpers().left_shift(number)
        
        if number != 0:
            result += ' '
        
        if self.is_a_teen(number):
            result += self.translate_teens(number)
        elif Helpers().number_of_digits(number) == 2:
            result += self.translate_last_two_digits(number)
        return result
