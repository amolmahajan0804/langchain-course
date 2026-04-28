from langchain_core.prompts import PromptTemplate
from langchain_ollama.chat_models import ChatOllama


def main():
    interested_stock = "ADANIENT"
    summary_template = (
        "Give available information about stock {interested_stock}. "
    )

    prompt_obj = PromptTemplate(
        template=summary_template, input_variables=["interested_stock"]
    )

    llm_obj = ChatOllama(temperature=0.3, model="llama3.2:3b")

    chain = prompt_obj | llm_obj
    response = chain.invoke(input={"interested_stock": interested_stock})
    print(response.content)


if __name__ == "__main__":
    main()
