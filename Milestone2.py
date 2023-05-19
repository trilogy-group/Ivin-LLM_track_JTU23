import os
import openai
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

llm = OpenAI(temperature=0.9)

prompt = PromptTemplate(
    input_variables=["product"],
    template="corrects all the math calculations in following text - {product}?",
)

query1 = prompt.format(product="If a recipe requires 2 cups of flour and I want to make 4 batches, I will need a total of 6.5 cups of flour.")
query2 = prompt.format(product="If each cup have 20 ml of beer in it, then if i drink 7 cups then i would have ingested 140ml of beer.")
query3 = prompt.format(product="If a store offers a discount of 25% on a $80 item, the discounted price will be $40.")

print(llm(query1),"\n\n")
print(llm(query2),"\n\n")
print(llm(query3))


# Output


# If a recipe requires 2 cups of flour and I want to make 4 batches, I will need a total of 8 cups of flour. 




# If each cup has 20 mL of beer in it, then if I drink 7 cups, I would have ingested 140 mL of beer. 




# If a store offers a discount of 25% on a $80 item, the discounted price will be $60.
