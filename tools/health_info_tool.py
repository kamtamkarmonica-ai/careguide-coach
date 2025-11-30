"""
tools/health_info_tool.py

Simple custom tool that returns patient-friendly information
for a few common chronic conditions.

Later you can replace the in-memory DB with a real Healthcare API call.
"""

from typing import Dict


# Tiny in-memory "database" for demo / local testing.
_CONDITION_DB: Dict[str, Dict[str, str]] = {
    "high blood pressure": {
        "summary": (
            "High blood pressure (hypertension) means the force of blood "
            "pushing against your artery walls is consistently too high."
        ),
        "key_points": (
            "- It usually has no symptoms.\n"
            "- It increases the risk of heart disease, stroke, and kidney problems.\n"
            "- Regular check-ups and lifestyle changes are very important."
        ),
        "lifestyle_tips": (
            "- Eat less salt and more fruits/vegetables.\n"
            "- Exercise regularly.\n"
            "- Maintain a healthy weight.\n"
            "- Avoid smoking and limit alcohol."
        ),
    },
    "diabetes": {
        "summary": (
            "Diabetes is a condition where your body has trouble using or "
            "making insulin, causing blood sugar levels to stay too high."
        ),
        "key_points": (
            "- There are different types (Type 1, Type 2, gestational).\n"
            "- Long-term high sugar can affect eyes, kidneys, nerves, and heart.\n"
            "- Monitoring sugar levels and regular follow-up with a doctor are essential."
        ),
        "lifestyle_tips": (
            "- Follow your meal plan and portion sizes.\n"
            "- Stay active most days of the week.\n"
            "- Take medications as prescribed.\n"
            "- Do not change treatment without talking to your doctor."
        ),
    },
}


def get_condition_info(condition: str) -> Dict[str, str]:
    """
    Fetches patient-friendly info about a chronic condition.

    Args:
        condition: Example: "high blood pressure", "diabetes".

    Returns:
        Dict with summary, key_points, lifestyle_tips.
        This is JSON-serializable so ADK can use it as tool output.
    """
    key = condition.strip().lower()
    info = _CONDITION_DB.get(key)

    if not info:
        # Generic fallback if we don't have this condition in the local DB.
        info = {
            "summary": (
                f"{condition} is a health condition. I don't have specific "
                "structured details in my local knowledge yet."
            ),
            "key_points": (
                "- It is best to speak with a qualified healthcare professional "
                "for accurate information.\n"
                "- Use trusted health websites or government health portals "
                "for more details."
            ),
            "lifestyle_tips": (
                "- Maintain a healthy lifestyle (diet, exercise, sleep).\n"
                "- Avoid self-medication; follow medical advice.\n"
                "- Get regular check-ups as recommended."
            ),
        }

    return {"condition": condition, **info}
