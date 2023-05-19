import os
import openai
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

llm = OpenAI(temperature=0.9)

prompt = PromptTemplate(
    input_variables=["product"],
    template="corrects all the math calculations in following text - {product}?",
)


# Insert your text within the double quotes
query1 = prompt.format(product="If a recipe requires 2 cups of flour and I want to make 4 batches, I will need a total of 6.5 cups of flour.")

print(llm(query1))
