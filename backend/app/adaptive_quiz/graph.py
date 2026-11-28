"""LangGraph orchestration for the adaptive quiz workflow."""

from typing import Literal

from langgraph.checkpoint.base import BaseCheckpointSaver
from langgraph.graph import END, START, StateGraph
from langgraph.graph.state import CompiledStateGraph

from app.adaptive_quiz.nodes import (
    collect_student_response,
    evaluate_answer,
    generate_question,
    initialize_mastery,
    load_student_context,
    select_difficulty,
    update_mastery,
    validate_question,
)
from app.adaptive_quiz.state import AdaptiveQuizState


def build_adaptive_quiz_graph(
    checkpointer: BaseCheckpointSaver,
    validation_retry_limit: int = 3,
) -> CompiledStateGraph:
    """Build the quiz graph with response checkpointing and bounded validation retries."""
    if validation_retry_limit < 0:
        raise ValueError("validation_retry_limit cannot be negative")

    workflow = StateGraph(AdaptiveQuizState)
    workflow.add_node("load_student_context", load_student_context)
    workflow.add_node("initialize_mastery", initialize_mastery)
    workflow.add_node("select_difficulty", select_difficulty)
    workflow.add_node("generate_question", generate_question)
    workflow.add_node("validate_question", validate_question)
    workflow.add_node("collect_student_response", collect_student_response)
    workflow.add_node("evaluate_answer", evaluate_answer)
    workflow.add_node("update_mastery", update_mastery)

    workflow.add_edge(START, "load_student_context")
    workflow.add_edge("load_student_context", "initialize_mastery")
    workflow.add_edge("initialize_mastery", "select_difficulty")
    workflow.add_edge("select_difficulty", "generate_question")
    workflow.add_edge("generate_question", "validate_question")

    def route_validation(
        state: AdaptiveQuizState,
    ) -> Literal["response", "retry", "error"]:
        if state.get("next_action") == "error":
            return "error"
        if state.get("question_is_valid"):
            return "response"
        if state.get("question_validation_attempts", 0) <= validation_retry_limit:
            return "retry"
        return "error"

    workflow.add_conditional_edges(
        "validate_question",
        route_validation,
        {
            "response": "collect_student_response",
            "retry": "generate_question",
            "error": END,
        },
    )
    workflow.add_edge("collect_student_response", "evaluate_answer")
    workflow.add_edge("evaluate_answer", "update_mastery")

    def route_session(
        state: AdaptiveQuizState,
    ) -> Literal["continue", "complete", "error"]:
        if (
            state.get("next_action") == "error"
            or state.get("session_status") == "error"
        ):
            return "error"
        if state.get("next_action") == "complete":
            return "complete"
        return "continue"

    workflow.add_conditional_edges(
        "update_mastery",
        route_session,
        {
            "continue": "select_difficulty",
            "complete": END,
            "error": END,
        },
    )

    return workflow.compile(checkpointer=checkpointer)
