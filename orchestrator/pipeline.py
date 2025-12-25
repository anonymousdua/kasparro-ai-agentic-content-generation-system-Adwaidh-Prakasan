from agents import (
    input_agent,
    parser_agent,
    question_agent,
    faq_agent,
    product_page_agent,
    comparison_agent
)

def run_pipeline():
    state = input_agent.run()
    state = parser_agent.run(state)
    state = question_agent.run(state)
    state = faq_agent.run(state)
    state = product_page_agent.run(state)
    state = comparison_agent.run(state)
