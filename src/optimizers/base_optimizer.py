"""
Base optimizer class for all gradient descent methods.
"""

import numpy as np
from abc import ABC, abstractmethod
from typing import Tuple, List


class BaseOptimizer(ABC):
    """
    Abstract base class for all optimizers.
    
    All optimizers should inherit from this class and implement the
    optimize method.
    """
    
    def __init__(self, learning_rate: float = 0.01):
        """
        Initialize the optimizer.
        
        Args:
            learning_rate (float): The learning rate for the optimizer
        """
        self.learning_rate = learning_rate
        self.costs_history = []
    
    @abstractmethod
    def optimize(self, X: np.ndarray, y: np.ndarray, epochs: int = 30) -> Tuple[np.ndarray, List[float]]:
        """
        Optimize the weights using the specific algorithm.
        
        Args:
            X (np.ndarray): Training features (including bias term)
            y (np.ndarray): Training labels
            epochs (int): Number of training epochs
            
        Returns:
            Tuple[np.ndarray, List[float]]: Final weights and cost history
        """
        pass
    
    def sigmoid(self, z: np.ndarray) -> np.ndarray:
        """Sigmoid activation function with overflow protection."""
        z = np.clip(z, -500, 500)
        return 1 / (1 + np.exp(-z))
    
    def compute_cost(self, w: np.ndarray, X: np.ndarray, y: np.ndarray) -> float:
        """
        Compute the logistic regression cost (cross-entropy).
        
        Args:
            w (np.ndarray): Current weights
            X (np.ndarray): Features
            y (np.ndarray): Labels
            
        Returns:
            float: The computed cost
        """
        m = len(y)
        z = X.dot(w)
        h = self.sigmoid(z)
        # Avoid log(0)
        h = np.clip(h, 1e-15, 1 - 1e-15)
        cost = -(1/m) * (y.dot(np.log(h)) + (1 - y).dot(np.log(1 - h)))
        return cost
    
    def evaluate_accuracy(self, w: np.ndarray, X: np.ndarray, y: np.ndarray) -> float:
        """
        Evaluate model accuracy.
        
        Args:
            w (np.ndarray): Model weights
            X (np.ndarray): Features
            y (np.ndarray): True labels
            
        Returns:
            float: Accuracy score
        """
        predictions = (self.sigmoid(X.dot(w)) >= 0.5).astype(int)
        accuracy = (predictions == y).mean()
        return accuracy
