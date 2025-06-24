"""
Utility functions for data preparation and model evaluation.
"""

import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from typing import Tuple


def prepare_iris_data() -> Tuple[np.ndarray, np.ndarray]:
    """
    Prepare Iris dataset for binary classification.
    
    Returns:
        Tuple[np.ndarray, np.ndarray]: Features (with bias) and labels
    """
    # Load Iris dataset
    iris = load_iris()
    X = iris.data
    y = iris.target
    
    # Take only Versicolor (1) and Virginia (2) for binary classification
    mask = (y == 1) | (y == 2)
    X = X[mask]
    y = y[mask]
    
    # Convert labels to 0 and 1
    y = (y == 2).astype(int)  # Virginia = 1, Versicolor = 0
    
    # Standardize features
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    
    # Add bias term
    X = np.c_[np.ones(X.shape[0]), X]
    
    return X, y


def split_data(X: np.ndarray, y: np.ndarray, test_size: float = 0.2, 
               random_state: int = 42) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Split data into training and testing sets.
    
    Args:
        X (np.ndarray): Features
        y (np.ndarray): Labels
        test_size (float): Proportion of data to use for testing
        random_state (int): Random state for reproducibility
    
    Returns:
        Tuple: X_train, X_test, y_train, y_test
    """
    return train_test_split(X, y, test_size=test_size, random_state=random_state, stratify=y)


def sigmoid(z: np.ndarray) -> np.ndarray:
    """
    Sigmoid activation function with overflow protection.
    
    Args:
        z (np.ndarray): Input values
        
    Returns:
        np.ndarray: Sigmoid output
    """
    z = np.clip(z, -500, 500)
    return 1 / (1 + np.exp(-z))


def evaluate_model(w: np.ndarray, X: np.ndarray, y: np.ndarray) -> float:
    """
    Evaluate model accuracy.
    
    Args:
        w (np.ndarray): Model weights
        X (np.ndarray): Features
        y (np.ndarray): True labels
        
    Returns:
        float: Accuracy score
    """
    predictions = (sigmoid(X.dot(w)) >= 0.5).astype(int)
    accuracy = (predictions == y).mean()
    return accuracy
