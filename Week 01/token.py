
# Given total words
myprice = 5.00
User_Words =  44569
Chat_Words  = 87963

# Estimate total tokens (average of 0.75 tokens per word)
total_tokens_user = User_Words * 0.75
total_tokens_Chat = Chat_Words * 0.75

# # Split tokens equally for input and output
# input_tokens = total_tokens / 2  
# output_tokens = total_tokens / 2  

# Cost calculation for input and output tokens
input_cost = (total_tokens_user * 0.03)  / 1000 
output_cost = (total_tokens_Chat * 0.06) / 1000 # type: ignore

# Total cost for 976 words
total_cost = input_cost + output_cost
# total_tokens, input_cost, output_cost, total_cost
print(f'NewPrice is {total_cost}')