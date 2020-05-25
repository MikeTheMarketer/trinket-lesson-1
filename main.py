bitcoin_bank = 1000
days_in_week = 7
average_daily_increase = .12
new_total = 0

for day in range(days_in_week):
  daily_increase = bitcoin_bank * average_daily_increase
  bitcoin_bank = bitcoin_bank + daily_increase

text = "When we buy bitcoin with 1000 USD at the beginning of the week, we would earn {:.2f} USD at the end of the week, with an average gain 12%"

print(text.format(bitcoin_bank))



temp_user = input('Please enter current temp in Farenhiet: ')
celsius = (5/9) * (int(temp_user) - 32)
print(celsius)

user_input = input('Please enter a 3 digit number: ')
holder_1 = user_input[0]
holder_2 = user_input[1]
holder_3 = user_input[2]

print('Your total of the 3 digits equals', int(holder_1) + int(holder_2) + int(holder_3))


first_line = input('user --> first side lenght: ')
second_line = input('user --> second side length: ')
hypotenus = int(first_line)**2 + int(second_line)**2
sqrt = hypotenus**(1.0/2)
print(sqrt)