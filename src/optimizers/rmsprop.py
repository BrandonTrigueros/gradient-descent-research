"""
RMSProp optimizer implementation.
"""

import numpy as np
from typing import Tuple, List
from .base_optimizer import BaseOptimizer


class RMSProp(BaseOptimizer):
    """
    RMSProp (Root Mean Square Propagation) optimizer.
    
    Adapts the learning rate for each parameter by dividing by a running
    average of the magnitudes of recent gradients.
    """
    
    def __init__(self, learning_rate: float = 0.05, rho: float = 0.9, epsilon: float = 1e-8):
        """
        Initialize RMSProp optimizer.
        
        Args:
            learning_rate (float): Learning rate for weight updates
            rho (float): Decay rate for the moving average (typically 0.9)
            epsilon (float): Small constant to prevent division by zero
        """
        super().__init__(learning_rate)
        self.rho = rho
        self.epsilon = epsilon
        self.name = "RMSProp"
    
    def optimize(self, X: np.ndarray, y: np.ndarray, epochs: int = 30) -> Tuple[np.ndarray, List[float]]:
        """
        Optimize weights using RMSProp.
        
        Args:
            X (np.ndarray): Training features (m x n)
            y (np.ndarray): Training labels (m,)
            epochs (int): Number of training epochs
            
        Returns:
            Tuple[np.ndarray, List[float]]: Final weights and cost history
        """
        m, n = X.shape
        w = np.random.normal(0, 0.01, n)  # Small random initialization
        E_grad2 = np.zeros(n)  # Initialize squared gradient accumulator
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
                
                # Update squared gradient accumulator
                E_grad2 = self.rho * E_grad2 + (1 - self.rho) * (grad ** 2)
                
                # RMSProp update
                w = w - (self.learning_rate / (np.sqrt(E_grad2) + self.epsilon)) * grad
            
            # Compute cost at end of epoch
            cost = self.compute_cost(w, X, y)
            costs.append(cost)
        
        self.costs_history = costs
        return w, costs
