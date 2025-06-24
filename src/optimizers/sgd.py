"""
Stochastic Gradient Descent (SGD) optimizer implementation.
"""

import numpy as np
from typing import Tuple, List
from .base_optimizer import BaseOptimizer


class SGD(BaseOptimizer):
    """
    Standard Stochastic Gradient Descent optimizer.
    
    This implementation performs updates using individual examples
    (true SGD) rather than mini-batches.
    """
    
    def __init__(self, learning_rate: float = 0.05):
        """
        Initialize SGD optimizer.
        
        Args:
            learning_rate (float): Learning rate for weight updates
        """
        super().__init__(learning_rate)
        self.name = "SGD"
    
    def optimize(self, X: np.ndarray, y: np.ndarray, epochs: int = 30) -> Tuple[np.ndarray, List[float]]:
        """
        Optimize weights using standard SGD.
        
        Args:
            X (np.ndarray): Training features (m x n)
            y (np.ndarray): Training labels (m,)
            epochs (int): Number of training epochs
            
        Returns:
            Tuple[np.ndarray, List[float]]: Final weights and cost history
        """
        m, n = X.shape
        w = np.random.normal(0, 0.01, n)  # Small random initialization
        costs = []
        
        for epoch in range(epochs):
            # Shuffle indices for each epoch
            indices = np.random.permutation(m)
            
            # Update for each individual example
            for i in indices:
                # Compute prediction for current example
                z = X[i].dot(w)
                h = self.sigmoid(z)
                
                # Compute gradient for current example
                grad = (h - y[i]) * X[i]
                
                # SGD update
                w = w - self.learning_rate * grad
            
            # Compute cost at end of epoch
            cost = self.compute_cost(w, X, y)
            costs.append(cost)
        
        self.costs_history = costs
        return w, costs
