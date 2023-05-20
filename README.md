# Ivin-LLM_track_JTU23


## Milestone 1 - Prompt Engineering
Note: For this milestone, you’ll be using OpenAI’s APIs (GPT-3.5-turbo). All the prompts must be documented properly in a doc. Add relevant screenshots whenever possible.

### 1
Write a prompt to compress a large piece of text such that when the compressed piece is provided back to GPT, it is able to regenerate the original text.
### 2
Take a student's interest (e.g. harry potter) and a topic (e.g. 20 elements of the periodic table) and give an acronym for them to learn the topic. E.g. MRS GREN - https://basicbiology.net/biology-101/mrs-gren. Try to create 3 acronyms that are as effective as possible. 
### 3
Write a prompt to output all of the bad practices in a given piece of code, with explanations and line numbers. 
- Note that the direct output from GPT with a simple prompt might not be accurate. Do whatever you can to make it as accurate as possible. (You might have to use some advanced prompt engineering)
- To demonstrate the effectiveness of your prompt, Pick 3 findings from your best practices assignment submission and show how your prompt performs at least as well as you did.

## Milestone 2 - Langchain
Note: For this milestone, you’ll be using Langchain. Demonstrate results in a doc with at least 3 hard examples.

Implement a program that takes text as input and corrects all the math calculations in the text. You can assume the math calculations to be elementary mathematical operations such as addition, subtraction, multiplication, and division. 
Be careful to not change anything else in the text except math.
Note that even though GPT is capable of performing basic math, it occasionally struggles with large numbers even while doing elementary operations, so relying solely on GPT to correct math calculations is not a good idea.  

Example - 
“There are 5 items on the menu and each cost $10 on average. Even if we get all of them, We will have to pay $40”
Corrected - 
“There are 5 items on the menu and each cost $10 on average. Even if we get all of them, We will have to pay $50”



## Milestone 3 - Langchain
Note: For this milestone, you’ll be using Langchain. Demonstrate results in a doc with at least 3 examples of X and Y pairs.

Implement a program that takes a topic of debate as input (e.g. Messi vs Ronaldo, X vs Y) and makes two agents converse with each other(back and forth) to reach a conclusion (X wins). 
Note that the conversations might be more interesting if one agent is for X and against Y and vice-versa. Also, the agents might require real-time data to make the conversation and conclusion more relevant and accurate



