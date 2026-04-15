# test_app.py
import pytest
import pandas as pd
from app.main import get_ai_response
from evaluation.evaluator import evaluate_response

# Load test data
test_data = pd.read_csv("data/test_cases.csv")

# @pytest.mark.parametrize("query,expected_keyword", test_data[["query", "expected_keyword"]].values)
# def test_ai_responses(query, expected_keyword):
#     response = get_ai_response(query)
    
#     assert expected_keyword.lower() in response.lower()

@pytest.mark.parametrize("query", test_data["query"].values)
def test_ai_response_quality(query):
    response = get_ai_response(query)
    
    evaluation = evaluate_response(query, response)
    
    lines = evaluation.split("\n")

    # Extract final score
    final_score_line = [line for line in lines if "Final Score" in line][0]
    score = float(final_score_line.split(":")[1].strip())
    assert score >= 3.5

# Run again
# PYTHONPATH=. pytest