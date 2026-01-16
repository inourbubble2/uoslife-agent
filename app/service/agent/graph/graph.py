from langgraph.graph import StateGraph

from app.service.agent.schema.state import GraphState

workflow = StateGraph(GraphState)
# TODO: add nodes & edges

graph = workflow.compile()
