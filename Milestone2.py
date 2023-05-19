import os
import openai
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

llm = OpenAI(temperature=0)


text = "corrects all the math calculations in following text - "
text+="If a recipe requires 2 cups of flour and I want to make 4 batches, I will need a total of 6.5 cups of flour."
print(llm(text))
