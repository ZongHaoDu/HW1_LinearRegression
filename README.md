# Simple Linear Regression with Outlier Detection

This is a simple web application built with Streamlit that demonstrates linear regression. It allows you to generate data based on a linear equation, visualize the data, the true line, and the fitted line, and identify outliers.

## Demo

You can try the live application here: [https://hw1linearregression-goyqskagjpwrflnky4axey.streamlit.app/](https://hw1linearregression-goyqskagjpwrflnky4axey.streamlit.app/)

## Features

*   **Interactive Parameters:** Adjust the slope (`a`), noise variance, and the number of data points.
*   **Linear Regression:** Automatically performs linear regression on the generated data to find the best-fit line.
*   **Visualization:** Displays a scatter plot of the data, the original line, and the fitted line.
*   **Outlier Detection:** Identifies and highlights the top 5 points with the largest residuals (outliers).
*   **Outlier Table:** Shows a table with details of the top 5 outliers, including their index, x/y values, and residuals.

## How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/ZongHaoDu/HW1_LinearRegression.git
    cd HW1_LinearRegression
    ```

2.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```
