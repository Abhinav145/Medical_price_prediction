{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "e1b5dfdf-094b-4ee7-b5aa-72f4e5588a47",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pickle\n",
    "import numpy as np\n",
    "\n",
    "# Load model\n",
    "pipe = pickle.load(open('pipe.pkl', 'rb'))\n",
    "\n",
    "st.set_page_config(\n",
    "    page_title=\"Medical Cost Prediction\",\n",
    "    page_icon=\"💊\",\n",
    "    layout=\"centered\",\n",
    ")\n",
    "\n",
    "st.markdown(\"\"\"\n",
    "    <h1 style='text-align:center; color:#4CAF50;'>💊 Medical Cost Prediction App</h1>\n",
    "    <p style='text-align:center;'>Enter patient details below to estimate medical insurance charges.</p>\n",
    "\"\"\", unsafe_allow_html=True)\n",
    "\n",
    "st.write(\"\")\n",
    "\n",
    "# --- Sidebar\n",
    "st.sidebar.header(\"About\")\n",
    "st.sidebar.info(\"\"\"\n",
    "This app predicts medical insurance cost using a trained Machine Learning model  \n",
    "(Linear Regression / SGD Regression).\n",
    "\"\"\")\n",
    "\n",
    "# ---- Input Form ----\n",
    "age = st.number_input(\"Age\", min_value=1, max_value=100, step=1)\n",
    "bmi = st.number_input(\"BMI\", min_value=10.0, max_value=60.0, step=0.1)\n",
    "children = st.number_input(\"Number of Children\", min_value=0, max_value=10, step=1)\n",
    "\n",
    "sex = st.selectbox(\"Sex\", [\"male\", \"female\"])\n",
    "smoker = st.selectbox(\"Smoker?\", [\"yes\", \"no\"])\n",
    "region = st.selectbox(\"Region\", [\"southwest\", \"southeast\", \"northwest\", \"northeast\"])\n",
    "\n",
    "# Prepare input for prediction\n",
    "input_data = np.array([[age, bmi, children, sex, smoker, region]])\n",
    "\n",
    "if st.button(\"Predict Medical Cost 💵\"):\n",
    "    pred = pipe.predict(input_data)[0]\n",
    "    st.success(f\"Predicted Medical Cost: **₹{pred:,.2f}**\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ee355e2a-1af9-4bd8-99c8-0c96b4b12bd9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
