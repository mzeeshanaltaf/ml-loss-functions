import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def plot_loss_functions(delta):

    # Define the error range
    errors = np.linspace(-5, 5, 400)

    # Compute losses
    mse_loss = errors ** 2 / 2  # Mean Squared Error (MSE)
    mae_loss = np.abs(errors)  # Mean Absolute Error (MAE)

    # Huber loss calculation
    huber_loss = np.where(np.abs(errors) <= delta,
                          0.5 * errors ** 2,
                          delta * (np.abs(errors) - 0.5 * delta))
    # Create the plot
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(errors, mse_loss, label="MSE (Mean Squared Error)", linestyle='dashed', color='red')
    ax.plot(errors, mae_loss, label="MAE (Mean Absolute Error)", linestyle='dotted', color='blue')
    ax.plot(errors, huber_loss, label="Huber Loss (δ = 1.0)", linewidth=2, color='green')

    # Add labels and styling
    ax.set_xlabel("Error")
    ax.set_ylabel("Loss")
    ax.set_title("Comparison of MSE, MAE, and Huber Loss")
    ax.axvline(0, color='black', linewidth=0.5, linestyle='--')
    ax.legend()
    ax.grid(True)

    # Display in Streamlit
    st.pyplot(fig)


def display_footer():
    footer = """
    <style>
    /* Ensures the footer stays at the bottom of the sidebar */
    [data-testid="stSidebar"] > div: nth-child(3) {
        position: fixed;
        bottom: 0;
        width: 100%;
        text-align: center;
    }

    .footer {
        color: grey;
        font-size: 15px;
        text-align: center;
        background-color: transparent;
    }
    </style>
    <div class="footer">
    Made with ❤️ by <a href="mailto:zeeshan.altaf@gmail.com">Zeeshan</a>.
    </div>
    """
    st.sidebar.markdown(footer, unsafe_allow_html=True)