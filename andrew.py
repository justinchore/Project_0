#This one organizes all accounts into a nested list
account_list = ['jeff,bezos,342352345345,43434.24,1234', 'justin,cho,53456346436,324334,4444']
oraganized_account_list = []
# for account_string in account_list:
#     oraganized_account_list.append(account_string.split(','))
#     # acc_list[0] would be firstname
#     # acc_list[1] would be last name
#     # acc_list[2] would be account number
#     # acc_list[3] would be balance
#     # acc_list[4] would be pin number
    

    
#OR

#This one organizes all accounts into a list of dictionaries
for account_string in account_list:
    acc_dict = {}
    acc_string_split = account_string.split(',')
    acc_dict['first_name'] = acc_string_split[0]
    acc_dict['last_name'] = acc_string_split[1]
    acc_dict['account_number'] = acc_string_split[2]
    acc_dict['balance'] = acc_string_split[3]
    acc_dict['pin'] = acc_string_split[4]
    oraganized_account_list.append(acc_dict)

print(oraganized_account_list)