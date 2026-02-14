import numpy as np
import math

def svd_2x2_singular_values(A: np.ndarray) -> tuple:
    """
    Compute SVD of a 2x2 matrix using one Jacobi rotation.
    
    Args:
        A: A 2x2 numpy array
    
    Returns:
        Tuple (U, S, Vt) where A ≈ U @ diag(S) @ Vt
        - U: 2x2 orthogonal matrix
        - S: length-2 array of singular values
        - Vt: 2x2 orthogonal matrix (transpose of V)
    """

    # switch A to float type
    A = A.astype(float)

    # create Symmetric Matrix AT.A

    B = A.T @ A

    # jacobi rotation
    theta = np.pi/4 if B[0, 0] == B[1, 1] else 1/2 * np.arctan((2 * B[0, 1]) / (B[0, 0] - B[1, 1]))
    # R = V, Rt = Vt = eigenvectors
    R = np.array(
        [
            [np.cos(theta), -np.sin(theta)], 
            [np.sin(theta), np.cos(theta)]
        ]
    )

    D = R.T @ B @ R
    sigma = np.sqrt(np.diagonal(D)) # eigenvalues

    # sort sigma value descending
    descending_indices = np.argsort(sigma)[::-1]
    sigma = sigma[descending_indices]
    # swap columns synchronously with sigma value
    R = R[:, descending_indices]
    
    # calculate inverse sigma matrix from sigma
    inv_sigma = np.zeros(D.shape)
    np.fill_diagonal(inv_sigma, 1/sigma)
    
    U = A @ R @ inv_sigma

    return (U, sigma, R.T) # (U, sigma, Vt)

if __name__ == "__main__":
    A = np.array([[1, 2], [3, 4]])
    U, S, Vt = svd_2x2_singular_values(A)
    A_reconstructed = U @ np.diag(S) @ Vt
    print(A_reconstructed)
    print(U @ U.T)
    # test case 4, the hardest
    print(f'U orthogonal: {np.allclose(U @ U.T, np.eye(2))}')
    