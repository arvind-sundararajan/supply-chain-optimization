```json
{
    "evaluation/evaluation_metrics.py": {
        "content": "
import logging
from typing import Dict, List
from langgraph import StateGraph
from deep_eval import ModelEvaluator
from letta import MemoryManager

logging.basicConfig(level=logging.INFO)

def calculate_non_stationary_drift_index(data: List[float]) -> float:
    """
    Calculate the non-stationary drift index for the given data.

    Args:
    data (List[float]): The input data.

    Returns:
    float: The non-stationary drift index.
    """
    try:
        # Initialize the StateGraph
        state_graph = StateGraph()
        # Calculate the non-stationary drift index
        non_stationary_drift_index = state_graph.calculate_drift_index(data)
        logging.info(f'Non-stationary drift index: {non_stationary_drift_index}')
        return non_stationary_drift_index
    except Exception as e:
        logging.error(f'Error calculating non-stationary drift index: {e}')
        return None

def evaluate_stochastic_regime_switch(model: ModelEvaluator, data: List[float]) -> Dict[str, float]:
    """
    Evaluate the stochastic regime switch for the given model and data.

    Args:
    model (ModelEvaluator): The model evaluator.
    data (List[float]): The input data.

    Returns:
    Dict[str, float]: The evaluation metrics.
    """
    try:
        # Initialize the MemoryManager
        memory_manager = MemoryManager()
        # Evaluate the stochastic regime switch
        evaluation_metrics = model.evaluate_stochastic_regime_switch(data, memory_manager)
        logging.info(f'Evaluation metrics: {evaluation_metrics}')
        return evaluation_metrics
    except Exception as e:
        logging.error(f'Error evaluating stochastic regime switch: {e}')
        return {}

def calculate_evaluation_metrics(data: List[float]) -> Dict[str, float]:
    """
    Calculate the evaluation metrics for the given data.

    Args:
    data (List[float]): The input data.

    Returns:
    Dict[str, float]: The evaluation metrics.
    """
    try:
        # Calculate the non-stationary drift index
        non_stationary_drift_index = calculate_non_stationary_drift_index(data)
        # Evaluate the stochastic regime switch
        evaluation_metrics = evaluate_stochastic_regime_switch(ModelEvaluator(), data)
        # Add the non-stationary drift index to the evaluation metrics
        evaluation_metrics['non_stationary_drift_index'] = non_stationary_drift_index
        logging.info(f'Evaluation metrics: {evaluation_metrics}')
        return evaluation_metrics
    except Exception as e:
        logging.error(f'Error calculating evaluation metrics: {e}')
        return {}

if __name__ == '__main__':
    # Simulate the 'Rocket Science' problem
    data = [1.0, 2.0, 3.0, 4.0, 5.0]
    evaluation_metrics = calculate_evaluation_metrics(data)
    logging.info(f'Evaluation metrics: {evaluation_metrics}')
",
        "commit_message": "feat: implement specialized evaluation_metrics logic"
    }
}
```