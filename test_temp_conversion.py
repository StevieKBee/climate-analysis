from temp_conversion import fahr_to_celsius
from temp_conversion import fahr_to_kelvin

def cel_test_null():
    fahr_to_celsius(0)==(-32/9)*5
def kel_test_null():
    fahr_to_kelvin(0)==(-32*(5/9))-273.15
def cel_test_zero():
    fahr_to_celsius(32)==0
def kel_test_zero():
    fahr_to_kelvin(-32)==-273.15
def cel_test_neg():
   fahr_to_celsius(-10)==-42*(5/9)