import gradio as gr

from agent_service import handler


def run(query: str):
    if not query or not query.strip():
        return {"answer": "Pose une question.", "accepted": False}
    return handler(query.strip())


demo = gr.Interface(
    fn=run,
    inputs=gr.Textbox(
        label="Question",
        placeholder="Explique le risque de prompt injection en production",
        lines=3,
    ),
    outputs=gr.JSON(label="Reponse + metriques"),
    title="Agentic AI Lab 4 - Production & Safety",
    description=(
        "Agent avec outils, garde-fous, evaluation et observabilite "
        "(latence, tokens, cout, traces)."
    ),
    examples=[
        "Explique le risque de prompt injection",
        "Combien font (256 * 1.5) + 12 ?",
        "Quels guardrails faut-il pour un agent en production ?",
    ],
)


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
