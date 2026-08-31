from google.adk.agents import Agent

billing_agent = Agent(
    name="billing_agent",
    model="gemini-...",
    instruction="""
    You are a billing specialist.

    Handle:
    - duplicate charges
    - invoices
    - subscription billing
    - payment issues
    """
)

technical_agent = Agent(
    name="technical_agent",
    model="gemini-...",
    instruction="""
    You are a technical support specialist.

    Handle:
    - bugs
    - login problems
    - API errors
    - product issues
    """
)

refund_agent = Agent(
    name="refund_agent",
    model="gemini-...",
    instruction="""
    You are a refund specialist.

    Handle:
    - refund requests
    - cancellation refunds
    - refund status
    """
)


manager_agent = Agent(
    name="support_manager",
    model="gemini-...",
    instruction="""
    You are the customer support manager.

    Understand the customer's request and delegate
    it to the appropriate specialist.

    - Billing issues → billing_agent
    - Technical issues → technical_agent
    - Refund issues → refund_agent

    Do not solve specialist problems yourself when
    a specialist is available.
    """,
    sub_agents=[
        billing_agent,
        technical_agent,
        refund_agent,
    ]
)