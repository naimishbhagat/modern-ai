#chain of through prompt
from openai import OpenAI
from dotenv import load_dotenv
import requests
import json
from pydantic import BaseModel, Field
from typing import Optional

load_dotenv()

client = OpenAI()

def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"
    return "Something went wrong"

available_tools = {
    "get_weather": get_weather
}

# Zero shot prompt: Directly giving the instruction to the model
SYSTEM_PROMPT ="""
    You're an expert AI assistant in resolving user queries using chain of thought.
    You work on START, PLAN and OUTPUT steps.
    You need to first PLAN what needs to be done. The PLAN can be multiple steps.
    Once you think enough PLAN has been done, finally you can give an OUTPUT.
    You can also call a tool if required from the list of available tools.
    For every tool call wait for the observe step which is the output from the called tool.

    Rules:
    - Strictly Follow the given JSON output format.
    - Only run one step at a time.
    - The sequence of steps in START (Where user gives an input),
    PLAN (That can be multiple times) and finally OUTPUT (which
    is going to be displayed to the user.)

    Output JSON Format:
    { "step": "START" | "PLAN" | "OUTPUT" | "TOOL" , "content": "string", "tool": "string", "input": "string"}

    Available Tools:
    - get_weather(city): Takes city name as an input string and retruns the weather info about the city.

    Example 1:
    Q: Hey, can you solve 2 + 3 * 5 /10
    PLAN: {"step": "PLAN" : "content":"Seems like user is interested in math problem"}
    PLAN: {"step": "PLAN" : "content":"Looking at the problem, we should solve this using BODMAS method"}
    PLAN: {"step": "PLAN" : "content":"Yes, The BODMAS is correct thing to be done here"}
    PLAN: {"step": "PLAN" : "content":"first we must multiply 3 * 5 which is 15"}
    PLAN: {"step": "PLAN" : "content":"Now the new equation is  2 + 15 / 10"}
    PLAN: {"step": "PLAN" : "content":"We must perform divide that is 15/10 = 1.5"}
    PLAN: {"step": "PLAN" : "content":"Now the new equation is 2 + 1.5"}
    PLAN: {"step": "PLAN" : "content":"Now finally lets perfrom the addition 3.5"}
    PLAN: {"step": "PLAN" : "content":"Great , we have solved and finally left with 3.5 as answer"}
    OUTPUT: {"step": "OUTPUT" : "content":"3.5"}

    Example 2:
    Q: Hey, what is the current weather of Delhi?
    PLAN: {"step": "PLAN" : "content":"Seems like user is interested in getting weather of Delhi in India"}
    PLAN: {"step": "PLAN" : "content":"Lets see if we have any available tool from the list of available tools"}
    PLAN: {"step": "PLAN" : "content":"Great, we have get_weather tool available for this query."}
    PLAN: {"step": "PLAN" : "content":"I need to call get_weather tool for delhi as input for city"}
    PLAN: {"step": "TOOL" : "tool": "get_weather", "input":"delhi"}
    PLAN: {"step": "OBSERVE" : "tool": "get_weather", "output":"The temperature of delhi is cloudy with 20 C"}
    PLAN: {"step": "PLAN" : "content":"Great, I got the weather info about delhi"}
    OUTPUT: {"step": "OUTPUT" : "content":"The current weather in delhi is 20 C with some cloudy sky."}

"""
class MyOutputFormat(BaseModel):
    step: str = Field(..., description="The ID of the step. Example: PLAN, OUTPUT, TOOL, etc ")
    content: Optional[str] = Field(None, description="The optional string content fpr the step")
    tool: Optional[str] = Field(None, desciption="The ID of the tool to call.")
    input: Optional[str] = Field(None, description="The input params for the tool.")


message_history = [
    {"role": "system", "content": SYSTEM_PROMPT},
]

while True:
    user_query = input("> ")
    message_history.append({"role": "user", "content": user_query})
    print("\n\n\n")
    while True:
        response = client.chat.completions.parse(
            model="gpt-4o", 
            response_format= MyOutputFormat,
            messages = message_history
        )
        parsed_result = (response.choices[0].message.parsed)
        message_history.append({"role":"assistant", "content":parsed_result.model_dump_json()})
       
        if parsed_result.step == "START":
            print("", parsed_result.content)
            continue

        if parsed_result.step == "PLAN":
            print(" ", parsed_result.content)
            continue

        if parsed_result.step == "TOOL":
            tool_to_call = parsed_result.tool
            tool_input = parsed_result.input
            print(f": {tool_to_call} ({tool_input})")
            tool_response = available_tools[tool_to_call](tool_input)
            print(f": {tool_to_call} ({tool_input}) = {tool_response}")
            message_history.append({ "role": "developer", "content": json.dumps(
                { "step" : "OBSERVE", "tool": tool_to_call, "input" : tool_input, "output": tool_response}
            )})
            continue

        if parsed_result.step == "OUTPUT":
            print(" ", parsed_result.content)
            break

print("\n")